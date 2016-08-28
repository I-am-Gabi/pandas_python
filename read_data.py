import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)


class ReadData:
    def __init__(self, file_name):
        self.file_name = file_name
        self.initialize()

    def initialize(self):
        self.zika_data = pd.read_csv(self.file_name)

    def access_data(self):
        # number of rows
        print len(self.zika_data)
        #  get the column names
        print self.zika_data.columns  # .tolist()
        # access columns like a dictionary with string keys
        print self.zika_data['location']
        # get multiple columns out at the same time by passing in a list of strings
        print self.zika_data[['location', 'value']]
        # access columns is using the dot syntax
        print self.zika_data.location

    def util(self):
        # head function: gives us the first 5 rows in the DataFrame
        print self.zika_data.head()
        # Passing in a number n gives us the first n items in the column
        print self.zika_data.head(10)
        # This also works with the dictionary syntax
        print self.zika_data.location.head()

    def filtering(self):
        mask_brazil = self.zika_data['location'] == "Brazil"
        # This is a pandas Series object, which is the one-dimensional equivalent of a DataFrame.
        # Because our DataFrame uses datetime objects for the index, we have a specialized TimeSeries object
        print type(mask_brazil)
        brazil_frame = self.zika_data[mask_brazil]
        # print brazil_frame.country.unique()
        # Removing colums I dont need
        # Brazil reports locations at the state level
        brazil_frame = brazil_frame.drop(
            ['location_type', 'data_field_code', 'time_period_type', 'time_period', 'unit'], axis=1)
        #print brazil_frame

read = ReadData('data/cdc_zika.csv')
read.filtering()
