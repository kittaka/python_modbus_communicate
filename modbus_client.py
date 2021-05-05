#!/usr/bin/env python
# coding: utf-8

# In[2]:


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# read_register
# read 10 registers and print result on stdout
# you can use the tiny modbus server "mbserverd" to test this code
# mbserverd is here: https://github.com/sourceperl/mbserverd
# the command line modbus client mbtget can also be useful
# mbtget is here: https://github.com/sourceperl/mbtget
#SERVER_HOST = "127.0.0.1"
#SERVER_PORT = 502

# uncomment this line to see debug message
#c.debug(True)
# define modbus server host, port
from pyModbusTCP.client import ModbusClient
import time

def modbus_com(SERVER_HOST,SERVER_PORT,function_code,start_register,amount_of_registers):
    c = ModbusClient()
    c.host(SERVER_HOST)
    c.port(SERVER_PORT)
    cnt=0
    while True:
        # open or reconnect TCP to server
        if not c.is_open():
            if not c.open():
                print("unable to connect to "+SERVER_HOST+":"+str(SERVER_PORT))
        # if open() is ok, read register (modbus function 0x03)
        if c.is_open():
            if function_code == "3":
                    # Read the amount_of_registers from start_register
                regs = c.read_holding_registers(int(start_register), int(amount_of_registers))
                # if success display registers
                if regs:
                    print("reg address" +str(start_register)+ "to" +str(int(start_register)+int(amount_of_registers)-1)+":"+str(regs))
            elif function_code == "16":
                #Future support
                pass
            
        cnt+=1
        if cnt>=2:
            print("クライアント通信終了")
            c.close()
            break
        # sleep 1s before next polling
        time.sleep(1)
        


# In[ ]:




