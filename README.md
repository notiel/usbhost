# usbhost

UsbHost is a device for manupulating Ostranna devices from PC using radio. 
[Repo with hardware and c++ code](https://github.com/Kreyl/UsbHost)


Protocol described [here](https://docs.google.com/document/d/1Enq7OxXN71MnZqI4T44DpILLiYlTNmURxSFmcvyZTgg/)

[List of commands](https://docs.google.com/document/d/1xTNT9nXQbrqk0kijIyspimRIQRoJOtMbkZyYuiGS3eA/) in Russian

USB2Radio devices displays itself as virtual COM-port, you may user Terminal app to send commands or send commands from your code to serial port object for example with this module. 

Commands list:

* get_port_list() function returns list of available comports as ['COM3', 'COM5', 'COM20' ...];
* get_device_port function returns first found port with Ostranna device (answer 'Ack 0' to 'Ping\r\n') as 'COM4';
* get_all_device_ports() returns list of comports with Ostranna devices connected (answer 'Ack 0' to 'Ping\r\n') as ['COM4', ...];
* open_port(port_id: str) takes comport as str parameter (open_port('COM4') and returns open port or None;
* send command(ser, command, parameters) send command with parameters to ser port, returns send status ("ok", "Bad data", "Unknown command" or "No device port");
* send query(ser, command, parameters) send query with parameters to ser port and returns answer;
* close_port(ser) gets result of open_port(port_id) as parameter and closes it .
