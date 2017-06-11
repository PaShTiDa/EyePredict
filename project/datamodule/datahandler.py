class DataHandler:
    """
    Object. contains a combined data structure for 2 object types:
    Eye-Tracker parsed data objects, and behavioral parsed data
    
    On Load, gets config and loads the specified parts.
    """
    def __init__(self, config):
        self.config = config
        self.Load()

    def Load(self):
        raise NotImplementedError