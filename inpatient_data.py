from log_helpers import log_helpers as log
import datetime as dt
import time

from demo_data_module import EmptyDataset

start = time.time()
log.setSysOut(f'inpatient_data_{dt.date.today()}.log')

class InpatientData(EmptyDataset):
    def __init(self):
        super().__init__()
    
    def dataLayout(self):
        self.addColumn('Hispanic', {'Y':484, 'N':1882, 'U':106},str)
        self.addColumn('Sex', {'M':1220,'F':1252}, str)
        self.uniqueID('ID',2472)

if __name__ == "__main__":
    dataset = InpatientData('ALAMEDA HOSPITAL')
    dataset.buildData()
    



log.printSectionHeader('Section Number 1')
log.printSectionSubHeader('Section SubHeader')
log.printElapsedTime(start)
