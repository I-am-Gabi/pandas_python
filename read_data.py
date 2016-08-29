"""
Source: https://www.kaggle.com/majacaci00/d/cdc/zika-virus-epidemic/zika-and-microcephaly-cases-in-brazil/notebook
        http://synesthesiam.com/posts/an-introduction-to-pandas.html
        https://www.kaggle.com/cdc/zika-virus-epidemic/kernels
"""

import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)


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
    print type(mask_brazil)
    # the filter is nothing more than a Series with a boolean value for every item in the index.
    print mask_brazil
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

    # Keeping microcephaly confirmed and microcephaly fatal_confirmed
    mask_conf = (brazil_frame['data_field'] == "microcephaly_confirmed") | (
        brazil_frame['data_field'] == "microcephaly_fatal_confirmed")
    brazil_frame = brazil_frame[mask_conf]
    print (brazil_frame.data_field.value_counts())
    print ("++++++++++++++")


data = initialize('data/simple_zika.csv')
filtering(data)
