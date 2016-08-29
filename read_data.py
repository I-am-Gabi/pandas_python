import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)


def initialize(file):
    return pd.read_csv(file, low_memory=False)


def access_data(zika_data):
    # number of rows
    print 'data size: ' + str(len(zika_data))
    #  get the column names
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


def filtering(self):
    self.zika_data['country'] = self.zika_data['location']
    self.zika_data['country'] = self.zika_data['country'].astype(str)
    self.zika_data['country'] = self.zika_data['country'].apply(lambda x: pd.Series(x.split('-')))
    # filter
    mask_brazil = self.zika_data['country'] == "Brazil"
    # This is a pandas Series object, which is the one-dimensional equivalent of a DataFrame.
    print type(mask_brazil)
    # the filter is nothing more than a Series with a boolean value for every item in the index.
    print mask_brazil
    # pandas lines up the rows of the DataFrame and the filter using the index
    # and then keeps the rows with a True filter value.
    brazil_frame = self.zika_data[mask_brazil]

    # Removing columns I don't need
    # Brazil reports locations at the state level
    brazil_frame = brazil_frame.drop(
        ['location_type', 'data_field_code', 'time_period_type', 'time_period', 'unit'], axis=1)

    # Creating state/city column
    foo = lambda x: pd.Series([i for i in reversed(x.split('-'))])
    brazil_frame['location'] = brazil_frame.location.apply(foo)
    brazil_frame.rename(columns={'location': 'state_city'}, inplace=True)


read = initialize('data/cdc_zika.csv')
read.filtering()
