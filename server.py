#!/bin/python

from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
from random import uniform
import snap7
from snap7.util import *

# Create an instance of ModbusServer
def run_server():
    server = ModbusServer("0.0.0.0", 502, no_block=True)
    plc_ip = '172.23.71.254'
    rack = 0
    slot = 2
    plc = snap7.client.Client()
    plc.connect(plc_ip, rack, slot)

    try:
        print("Start server...")
        server.start()
        print("Server is online")
        state = [0]
        
        while True:
            data = plc.db_read(40, 68, 24)
            
            # Make sure there are an even number of elements in the data list
            if len(data) % 2 != 0:
                data.append(0)  # Add a padding zero if the number of elements is odd
            
            for i in range(0, len(data), 4):
                high_byte1 = data[i]
                low_byte1 = data[i + 1]
                high_byte2 = data[i + 2]
                low_byte2 = data[i + 3]
                
                # Combine the high byte and low byte to form the 16-bit word
                word_value1 = (high_byte1 << 8) | low_byte1
                word_value2 = (high_byte2 << 8) | low_byte2
                
                # Set the 16-bit word value in the DataBank
                DataBank.set_words(i // 2, [word_value2])  # Divide by 2 to get the correct index in DataBank
                DataBank.set_words((i // 2) + 1, [word_value1])
                
            sleep(1)

    except Exception as e:
        print("An exception occurred:", e)
        print("Shutdown server ...")
        server.stop()
        print("Server is offline")
        print("Restarting in 5 seconds...")
        sleep(5)
        run_server()
        
run_server()
