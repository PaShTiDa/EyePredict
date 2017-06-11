from parsing.ibehavioralparser import IBehavioralParser
import pandas as pd

class BehaviorlParser(IBehavioralParser):

    def parse(self, file):
        return pd.read_csv(file, delim_whitespace=True, index_col=False)
