import pandas as pd
import datetime as dt
import random

class EmptyDataset:
    def __init__(self, hospital_nm):
        self.cols = dict()
        self.today = dt.date.today()
        self.hospital_nm = hospital_nm
        self.df = pd.DataFrame()
        

    def add Column(self, colName, distribution_dict, data_type):
        combined = list()
        for key in distribution_dict.keys():
            temp_list = [key] * distribution_dict[key]
            combined = combined + temp_list
        random.shuffle(combined)
        self.df[colName] = combined
        print(self.df[colName].value_counts())

    def uniqueID(self,id_nm, total_rows):#,  id_dtype, id_length):
        self.total_rows = total_rows
        self.id_nm = id_nm
        #self.dtype = id_dtype
        #self.id_length = id_length

    def dataLayout(self):
        pass

    def buildData(self):
        self.dataLayout()
        cols = self.cols.keys()
        self.df[self.id_nm] = list(range(1,self.total_rows+1))
        self.df['FACILITY'] = self.hospital_nm
        self.df.set_index(['FACILITY',self.id_nm], inplace=True)
        self.df.to_csv(f'qa_file_{self.today}.csv')
        print(self.df.head())
        print(self.df.head().dtypes)

