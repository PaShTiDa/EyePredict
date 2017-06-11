
class BehavioralDataHandler:

    def ExtractConfigurationOptions(self, path):
        '''
        :param path: path to a valid behavioral data file
        :return: list of titles
        '''
        fd = open(path)
        titles = fd.readline()
        return titles.split('\t')

    def ExecuteQuery(self, string):
        # 1. load all behavioral files to one DataFrame table: data
        # 1.5 for each file add to the table, add a new colums: trialNumber
        # 2. filteredData = data.query(string)
        # 3. data handel module wiil get the first two coloms of that table
        # 4. filteredData is now displayed
        raise NotImplementedError


    def BehavioralDataToDataFrame(self, path):
        '''
        :param path: path to behavioral data folder 
        :return: one DataFrame table containing all behavioral files
        '''
        self.path = path

        # do the loading thing, creating df
        df=None
        self.raw_data = df

        raise NotImplementedError


    def FilterBehavioralData(self, query):
        '''
        :param query: a configurations string query 
        :return:  DataFrame table with the filtered behavioral data
        '''

        if self.raw_data == None:
            # No data loaded, quit
            raise NotImplementedError

        self.filtered_data = self.raw_data.query(query)
        return self.filtered_data

