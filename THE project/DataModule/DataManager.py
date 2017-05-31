

class DataManager:
    _mainDirectoryPath = ""

    def VerifyPath(self):
        """
        verifys the path is valid, and contains 3 directories: 
        Eye-tracking data, Behavioral data, Images
        :return: bool True/False
        """
        raise NotImplementedError

    def VerifyData(self):
        """
        checks the folders content.
        expects the same number of edf and txt files,
        with appropriately fitting file names for each couple.
        (do we need to test the files aren't empty?)
        :return: bool True/False
        """

    def BrowseDirectory(self, path):
        """
        Button "Browse" gets a directory path, and sends it to this function.
        """
        rc = True
        _mainDirectoryPath = path

        # Verify Data
        if(!VerifyPath(self)):
            error = "Bad data path.\n Eye-Predict expects the main folder to contain 3 subfolders:\n Eye-tracking data, Behavioral data, Images"
            rc = False
        if(rc && !VerifyData(self)):
            error = "..."
        if(!rc):
            Error(self, error)
            return -1

        # Load Data


        raise NotImplementedError

    def Error(self, errorString):
        """
        pops a gui error dialog box
        :param errorString: the error to prompt
        :return: non
        """





