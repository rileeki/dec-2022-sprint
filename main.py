from log_helpers import log_helpers as log
import datetime as dt
import time

start = time.time()
log.setSysOut(f'main_{dt.date.today()}.log')
log.printSectionHeader('Section Number 1')
log.printSectionSubHeader('Section SubHeader')
time.sleep(5.5)
log.printElapsedTime(start)
