#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import print_function
import sys
import main
if True:
    ACCOUNTCHANNEL=0
    Live=0
    AccName="MexUIPublic"
    SERVER="None"
    TAG="Public"
    PUBLICSCRIPT=True
    for ARG in sys.argv[1:]:
        if 'API_KEY=' in str(ARG):
            API_KEY=str(ARG.replace('API_KEY=', ''))
        elif 'API_SECRET=' in str(ARG):
            API_SECRET=str(ARG.replace('API_SECRET=', ''))
        elif 'LiveNET=True' in str(ARG):
            Live = 1
        elif 'LiveNET=False' in str(ARG):
            Live = 0
        elif 'AccName=' in str(ARG):
            AccName=str(ARG.replace('AccName=', ''))
        elif 'ServerName=' in str(ARG):
            SERVER=ARG.replace('ServerName=', '')
        elif 'ACCOUNTCHANNEL=' in str(ARG):
            ACCOUNTCHANNEL=ARG.replace('ACCOUNTCHANNEL=','')
        elif 'TAG=' in str(ARG):
            TAG=ARG.replace('TAG=','')
        elif 'help' in str(ARG):
            print ("Help menu here  ")
        elif 'SERVERMODE=True' in str(ARG):
            SERVERMODE = True
            PUBLICSCRIPT = False
        else:
            print (" Unrecognized option '{0}' Restart script with correct input".format(ARG))
            exit(0)
    if Live == 1:
        print("=== Using BiteEx Live Net === ")
    else:
        print ("=== Using BiteEx Test net ===")

main.Run(API_KEY,API_SECRET,Live,AccName,SERVER,ACCOUNTCHANNEL,TAG,PUBLICSCRIPT)

