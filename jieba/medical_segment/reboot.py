#encoding=utf-8
import sys
import os
import time
import signal

Max_process = 2
log_index = 0

def stopSession():
    sessionamelist = ['segment_service']
    for sessioname in sessionamelist:
        parentList = os.popen("ps -ef|grep %s|grep -v grep|awk '{print $2}'" %sessioname).readlines()
        if parentList:
            print ("kill--",sessioname)
            for pid in parentList:
                os.kill(int(pid),signal.SIGKILL)
                time.sleep(1)

stopSession()