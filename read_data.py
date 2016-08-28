import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import logging

logging.basicConfig(filename='trace.log', level=logging.DEBUG)


class ReadData:
    def __init__(self, file_name):
        self.file_name = file_name
        self.__initialize()

    def __initialize(self):
        """
        Read csv file
        """
        self.zika_data = pd.read_csv(self.file_name,low_memory=False)

    def access_data(self):
        # number of rows
        logging.info('data size: ' + str(len(self.zika_data)))
        #  get the column names
        logging.info('columns: ' + str(self.zika_data.columns.tolist()))
        # access columns like a dictionary with string keys
        print self.zika_data['location']
        # get multiple columns out at the same time by passing in a list of strings
        print self.zika_data[['location', 'value']]
        # access columns is using the dot syntax
        print self.zika_data.location
        # head function: gives us the first 5 rows in the DataFrame
        print self.zika_data.head()
        # Passing in a number n gives us the first n items in the column
        print self.zika_data.head(10)
        # This also works with the dictionary syntax
        print self.zika_data.location.head()

    def filtering(self):
        #
        self.zika_data['country'] = self.zika_data['location']
        self.zika_data['country'] = self.zika_data['country'].astype(str)
        self.zika_data['country'] = self.zika_data['country'].apply(lambda x: pd.Series(x.split('-')))
        print self.zika_data['country']
        # filter
        mask_brazil = self.zika_data['country'] == "Brazil"
        # This is a pandas Series object, which is the one-dimensional equivalent of a DataFrame.
        print type(mask_brazil)
        # the filter is nothing more than a Series with a boolean value for every item in the index.
        print mask_brazil
        # pandas lines up the rows of the DataFrame and the filter using the index
        # and then keeps the rows with a True filter value.
        brazil_frame = self.zika_data[mask_brazil]
        print brazil_frame.location.unique()

        # Removing colums I dont need
        # Brazil reports locations at the state level
        brazil_frame = brazil_frame.drop(
            ['location_type', 'data_field_code', 'time_period_type', 'time_period', 'unit'], axis=1)
        print brazil_frame

        # Creating state/city column
        foo = lambda x: pd.Series([i for i in reversed(x.split('-'))])
        brazil_frame['location'] = brazil_frame.location.apply(foo)
        brazil_frame.rename(columns={'location': 'state_city'}, inplace=True)

read = ReadData('data/cdc_zika.csv')
read.filtering()
