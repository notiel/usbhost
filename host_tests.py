import unittest
import Usbhost
device_port = 'COM4'
device_connected = True

class TestHost(unittest.TestCase):

    def test_OpenPortNotExists(self):
        self.assertIsNone(Usbhost.open_port('COM234'))

    # only for system with 'com3' default port
    def test_OpenPortExists(self):
        if device_connected:
            self.assertIsNotNone(Usbhost.open_port(device_port))
        else:
            self.assertIsNotNone(Usbhost.open_port('COM3'))

    def test_PortList(self):
        if device_connected:
            self.assertEqual(Usbhost.get_ports_list(), ['COM3', 'COM4'])
        else:
            self.assertEqual(Usbhost.get_ports_list(), ['COM3'])

    def test_NoOurDevice(self):
        if not device_connected:
            self.assertIsNone(Usbhost.get_device_port())

    def test_NoOurDeviceList(self):
        if not device_connected:
            self.assertEqual(Usbhost.get_all_device_ports(), [])


class TestCommands(unittest.TestCase):

    def test_NoParams(self):
        self.assertEqual(Usbhost.create_command("Ping"), 'Ping\r\n')

    def test_OneParam(self):
        self.assertEqual(Usbhost.create_command('WritePill', 5), 'WritePill 5\r\n')

    def test_ManyParams(self):
        self.assertEqual(Usbhost.create_command('SetClr', 1, 255, 0, 0), 'SetClr 1 255 0 0\r\n')

    def test_CommandWrongPort(self):
        ser = Usbhost.open_port('COM3')
        self.assertEqual(Usbhost.send_command(ser, 'Ping'), "Bad data")
        Usbhost.close_port(ser)

    def test_QueryWrongPort(self):
        ser = Usbhost.open_port('COM3')
        self.assertEqual(Usbhost.send_query(ser, 'SetClr', 1, 255, 0, 0), '')
        Usbhost.close_port(ser)

    def test_CommandNoParam(self):
        if device_connected:
            ser = Usbhost.open_port(Usbhost.get_device_port())
            self.assertEqual(Usbhost.send_command(ser, 'Ping'), "Ok")
            Usbhost.close_port(ser)

    def test_UnknownCommand(self):
        if device_connected:
            ser = Usbhost.open_port(Usbhost.get_device_port())
            self.assertEqual(Usbhost.send_command(ser, 'SomeCommand'), "Unknown command")
            Usbhost.close_port(ser)

    # for USB Host for Brain Ring, change to other command for other devices
    def test_BadDataCommand(self):
        if device_connected:
            ser = Usbhost.open_port(Usbhost.get_device_port())
            self.assertEqual(Usbhost.send_command(ser, 'SetClr'), "Bad data")
            Usbhost.close_port(ser)

    def test_ManyParamCommand(self):
        if device_connected:
            ser = Usbhost.open_port(Usbhost.get_device_port())
            self.assertEqual(Usbhost.send_command(ser, 'SetClr', 1, 255, 0, 0), "Ok")
            Usbhost.close_port(ser)

    def test_QueryNoParam(self):
        if device_connected:
            ser = Usbhost.open_port(Usbhost.get_device_port())
            self.assertEqual(Usbhost.send_query(ser, 'GetBtns'), 'Btns: 1 0 2 0')

def main():
    unittest.main()


if __name__ == '__main__':
    main()
