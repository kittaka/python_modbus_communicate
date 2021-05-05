#!/usr/bin/env python
# coding: utf-8

# In[5]:


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Modbus/TCP server

import argparse
from pyModbusTCP.server import ModbusServer
from pyModbusTCP.server import DataBank
def server_start(host,port):
    # parse args
    #parser = argparse.ArgumentParser()
    #parser.add_argument('-H', '--host', type=str, default='localhost', help='Host')
    #parser.add_argument('-p', '--port', type=int, default=502, help='TCP port')
    #args = parser.parse_args()
    #print("humo")
    
    # start modbus server
    server = ModbusServer(host, int(port),no_block=True)
    server.start()

def server_stop(host,port):
    # parse args
    #parser = argparse.ArgumentParser()
    #parser.add_argument('-H', '--host', type=str, default='localhost', help='Host')
    #parser.add_argument('-p', '--port', type=int, default=502, help='TCP port')
    #args = parser.parse_args()
    # start modbus server
    #print("humo")
    server = ModbusServer(host, int(port),no_block=False)
    server.stop()
    
def server_wordset(address,wordlist):
    DataBank.set_words(address,wordlist)


# In[ ]:




