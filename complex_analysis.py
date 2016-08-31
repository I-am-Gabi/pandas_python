"""
Source: https://www.kaggle.com/majacaci00/d/cdc/zika-virus-epidemic/zika-and-microcephaly-cases-in-brazil/notebook
        http://synesthesiam.com/posts/an-introduction-to-pandas.html
        https://www.kaggle.com/cdc/zika-virus-epidemic/kernels
"""

import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import numpy as np  # linear algebra


def initialize(file_name):
    return pd.read_csv(file_name, low_memory=False)


def access_data(zika_data):
    # number of rows
    print 'data size: ' + str(len(zika_data))
    # get the column names
    print 'columns: ' + str(zika_data.columns.tolist())
    # access columns like a dictionary with string keys
    print zika_data['location']
    # get multiple columns out at the same time by passing in a list of strings
    print zika_data[['location', 'value']]
    # access columns is using the dot syntax
    print zika_data.location
    # head function: gives us the first 5 rows in the DataFrame
    print zika_data.head()
    # Passing in a number n gives us the first n items in the column
    print zika_data.head(10)
    # This also works with the dictionary syntax
    print zika_data.location.head()


def filtering(zika_data):
    # remove state/city from country
    zika_data['country'] = zika_data['location']
    zika_data['country'] = zika_data['country'].astype(str)
    zika_data['country'] = zika_data['country'].apply(lambda x: pd.Series(x.split('-')))
    # filter
    mask_brazil = zika_data['country'] == "Brazil"
    # This is a pandas Series object, which is the one-dimensional equivalent of a DataFrame.
    #### print type(mask_brazil)
    # the filter is nothing more than a Series with a boolean value for every item in the index.
    #### print mask_brazil
    # pandas lines up the rows of the DataFrame and the filter using the index
    # and then keeps the rows with a True filter value.
    brazil_frame = zika_data[mask_brazil]

    # Removing columns I don't need
    # Brazil reports locations at the state level
    brazil_frame = brazil_frame.drop(
        ['location_type', 'data_field_code', 'time_period_type', 'time_period', 'unit'], axis=1)

    # Creating state/city column
    foo = lambda x: pd.Series([i for i in reversed(x.split('-'))])
    brazil_frame['location'] = brazil_frame.location.apply(foo)
    brazil_frame.rename(columns={'location': 'state_city'}, inplace=True)
    # print brazil_frame

    # Cleaning the state city column
    brazil_frame.state_city = brazil_frame.state_city.map(lambda x: x.replace('_', ' '))
    brazil_frame = brazil_frame[brazil_frame.state_city != 'Brazil']
    print brazil_frame.state_city.value_counts()
    return brazil_frame

## Changing the order of the columns
def order(frame,var):
    varlist =[w for w in frame.columns if w not in var]
    frame = frame[var+varlist]
    return frame


def plot_num_ts(df, seq_col, seq):
    cat = df[seq_col].unique()
    fig = plt.figure(figsize=(12,8))
    ax = fig.gca()
    for i in cat:
        df_ = df[df[seq_col] == i]
        df_ = df_.set_index('date')
        df_ = df_.resample(seq).sum()
        ax.plot(df_['microcephaly_confirmed'], lw=1.5, linestyle='dashed', marker='o',
                markerfacecolor='red', markersize=5,
                label="Confirmed cases in %s"%i)

    plt.legend(loc='best', fontsize=10, bbox_to_anchor=(0., 1.02, 1., .102),ncol=3)
    plt.xlabel('\nTime progression in %s'%seq)
    plt.ylabel("Total Microcephaly Cases\n")
    plt.show()


def int_replace(x):
    try:
        return int(x)
    except:
        return np.nan_to_num(x)


data = initialize('data/simple_zika.csv')
brazil_frame = filtering(data)
brazil_frame = order(brazil_frame,['report_date','country', 'state_city'])

# Keeping microcephaly confirmed and microcephaly fatal_confirmed
mask_conf = (brazil_frame['data_field'] == "microcephaly_confirmed") | (
    brazil_frame['data_field'] == "microcephaly_fatal_confirmed")
brazil_frame = brazil_frame[mask_conf]
print (brazil_frame.data_field.value_counts())
print ("++++++++++++++")

brazil_frame.value = brazil_frame.value.map(int_replace)
brazil_frame.value = brazil_frame.value.astype(int)

print ("Shape of data:", brazil_frame.shape)
print ("++++++++++++++\n")
print ("Missing values:\n")
print (brazil_frame.isnull().sum())
print ("++++++++++++++\n")
print (brazil_frame.info())
print ("++++++++++++++\n")

# Reshaping the Data
brazil_zika = pd.pivot_table(brazil_frame,
                             index=['country','state_city','report_date'],
                             columns=['data_field'],values=['value'],
                             aggfunc=sum)
brazil_zika = brazil_zika['value'].reset_index()

## Making Report date the index
print (brazil_zika.report_date.dtype )
print ("++++++++++++++")
brazil_zika.sort_values("report_date", inplace=True)
brazil_zika.set_index("report_date", inplace=True)
brazil_zika.index = brazil_zika.index.to_datetime()

## Now creating a year, month and day column
brazil_zika['year'] = brazil_zika.index.year
brazil_zika['month'] = brazil_zika.index.month
brazil_zika['day'] = brazil_zika.index.day

brazil_zika['microcephaly_fatal_confirmed'].fillna(0, inplace=True)
brazil_zika['microcephaly_confirmed'].fillna(0, inplace=True)
brazil_zika['microcephaly_confirmed'] = brazil_zika.microcephaly_confirmed.astype(int)
brazil_zika['microcephaly_fatal_confirmed'] = brazil_zika.microcephaly_fatal_confirmed.astype(int)

print (brazil_zika.info())
print ("++++++++++++++\n")
print (brazil_zika.shape)

## Creting Data Frame for graphs by state and date
brazil_zika_ = brazil_zika.reset_index()
brazil_zika_ = brazil_zika_.rename(columns={'index':'date'})
brazil_gb = brazil_zika_.groupby(['state_city','date']).sum()

brazil_gb = brazil_gb.reset_index()

print (brazil_gb.columns)
print (brazil_gb.head(3))

plot_num_ts(brazil_gb, 'state_city', 'W')

grouped = brazil_zika.groupby(['state_city'])
##
grouped_val_1 = grouped['microcephaly_confirmed']
category_group_1=grouped_val_1.sum()
##
grouped_val_2 = grouped['microcephaly_fatal_confirmed']
category_group_2=grouped_val_2.sum()
##


plt.figure(figsize=(10,7))
braz_microc_conf_1 = category_group_1.plot(kind='bar', color='green',
                                           alpha=0.7,
                                           title= "Microcephaly Confirmed Cases 2016\n")
braz_microc_conf_1.set_xlabel("States\n")
braz_microc_conf_1.set_ylabel("Sum of Cases\n")
plt.show()

grouped = brazil_zika.groupby(['month'])
##
grouped_val = grouped['microcephaly_confirmed']
category_group=grouped_val.sum()
#
grouped_val_1 = grouped['microcephaly_fatal_confirmed']
category_group_1=grouped_val_1.sum()


plt.figure(figsize=(10,6))

braz_graph= category_group.plot(kind='bar', color='green', alpha=0.7,
                                title= "Microcephaly Cases 2016\n",
                                label="microcephaly_confirmed")
braz_graph_1= category_group_1.plot(kind='bar', color='red', alpha=0.7)

braz_graph.set_xlabel("Months\n")
braz_graph.set_ylabel("Total Cases\n")

plt.tick_params(labelsize=14)
plt.legend(loc='upper left')
plt.show()