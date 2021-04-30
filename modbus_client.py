#!/usr/bin/env python
# coding: utf-8

# In[3]:


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# read_register
# read 10 registers and print result on stdout
# you can use the tiny modbus server "mbserverd" to test this code
# mbserverd is here: https://github.com/sourceperl/mbserverd
# the command line modbus client mbtget can also be useful
# mbtget is here: https://github.com/sourceperl/mbtget
from pyModbusTCP.client import ModbusClient
import time
SERVER_HOST = "127.0.0.1" # 接続先ホスト
SERVER_PORT = 502
c = ModbusClient()
# uncomment this line to see debug message
#c.debug(True)
# define modbus server host, port
c.host(SERVER_HOST)
c.port(SERVER_PORT)

def modbus_com():
    cnt=0
    while True:
        # open or reconnect TCP to server
        if not c.is_open():
            if not c.open():
                print("unable to connect to "+SERVER_HOST+":"+str(SERVER_PORT))
        # if open() is ok, read register (modbus function 0x03)
        if c.is_open():
            # read 10 registers at address 0, store result in regs list
            regs = c.read_holding_registers(0, 10)
            # if success display registers
            if regs:
                print("reg ad #0 to 9: "+str(regs))
        # sleep 2s before next polling
        time.sleep(2)
        cnt+=1
        if cnt>=2:
            print("通信終了")
            c.close()
            break
    


# In[ ]:




