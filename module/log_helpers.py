########################################
# Functions to help with logging prints
########################################
import os
import datetime as dt
import sys
import time

def setSysOut(logname):
    log_file = open(f'{logname}','w')
    sys.stdout = log_file
    sys.stderr = log_file
    printLogDetails(logname)

def printLogDetails(logname):
    print('#'*72)
    print('# Log: ', logname)
    print('# User: ',os.getlogin())
    print('# Date: ', dt.datetime.now())
    print('#'*72,'\n'*2)

def printSectionHeader(section_nm):
    print('','*'*72,section_nm.upper().center(72, '*'),'*'*72, sep='\n')

def printSectionSubHeader(subhead_nm):
    print('','-'*72,subhead_nm.upper().center(72, '-'), sep='\n')

def printElapsedTime(start_time, statement='Elapsed Time: '):
    elapsedTime = time.time() - start_time
    minutes, seconds = divmod(elapsedTime,60)
    hours, minutes = divmod(minutes, 60)
    print('\n',statement, 
            f'{hours} hrs ' * (hours>0), 
            f'{minutes} mins ' * (minutes>0), 
            f'{round(seconds,2)} secs.' * (seconds>0))