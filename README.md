# siemens-modbus
Get siemens s7 PLC data and pass onto a modbus server for easy access from other devices.

## What is this for? 
This code will take data from a siemens PLC and post it on a modbus server for access from other devices. The data read is in blocks of 4 bytes, which are then
rearranged to form a 32 bit float. In this way, other devices can use this program as an interface for the S7 protocol (siemens) indirectly via modbus.

## Usage
Set the address of your modbus server on the localhost and its desired port. Change the PLC IP, slot and rack values to that which corresponds with the target PLC. 
On the db_read() function, set the addresses of the data that is to read from the PLC. 

## Dependencies
- Snap7 library
- pyModbusTCP library
