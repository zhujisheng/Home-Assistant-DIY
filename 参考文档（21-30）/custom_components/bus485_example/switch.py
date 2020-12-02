"""本程序仅供参考"""

import logging
import threading
import time

from homeassistant.components.switch import SwitchEntity

_LOGGER = logging.getLogger(__name__)


def crc_modbus(input_buffer):
    import crcmod
    crc16 = crcmod.mkCrcFun(0x18005, rev=True, initCrc=0xFFFF, xorOut=0x0000)
    crc_output=crc16(input_buffer)
    return crc_output.to_bytes(2, byteorder='little')

def setup_platform(hass, config, add_entities, discovery_info=None):
    """"""
    import serial
    socket=serial.Serial(port='/dev/ttyUSB0',
                         timeout=3,
                         bytesize=8,
                         stopbits=1,
                         baudrate=9600,
                         parity='N')

    devices = []
    switch=my_switch(socket, 1, 0)
    devices.append(switch)

    switch=my_switch(socket, 1, 1)
    devices.append(switch)

    switch=my_switch(socket, 1, 2)
    devices.append(switch)

    switch=my_switch(socket, 1, 3)
    devices.append(switch)

    add_entities(devices)

    return True


class my_switch(SwitchEntity):
    """"""

    def __init__(self, socket, address, coil):
        """Initialize"""
        self._lock = threading.Lock()
        self._socket = socket
        self._address = address
        self._coil = coil
        self._is_on = False
        self._name = 'my_relay_' + str(address) + '_' + str(coil)

    @property
    def is_on(self):
        """Return true if device is on."""
        return self._is_on

    @property
    def name(self):
        """Return the name of the switch."""
        return self._name

    @property
    def supported_features(self):
        """Flag supported features."""
        return 0

    def turn_on(self, **kwargs):
        """Turn on a light."""
        with self._lock:
            command = bytes([self._address]) + \
                      b'\x05\x00' + \
                      bytes([self._coil]) + \
                      b'\xFF\x00'
            crc = crc_modbus(command)
            self._socket.write(command + crc)
            time.sleep(0.1)
            _LOGGER.info("turn on：{}".format(command+crc))

    def turn_off(self, **kwargs):
        """Turn off a light."""
        with self._lock:
            command = bytes([self._address]) + \
                      b'\x05\x00' + \
                      bytes([self._coil]) + \
                      b'\x00\x00'
            crc = crc_modbus(command)
            self._socket.write(command + crc)
            time.sleep(0.1)
            _LOGGER.info("turn off：{}".format(command+crc))

    def update(self):
        """"""
        with self._lock:
            command = bytes([self._address]) + \
                      b'\x01\x00\x00\x00\x10'
            crc = crc_modbus(command)

            self._socket.reset_input_buffer()
            self._socket.write(command + crc)
            _LOGGER.info("read status：{}".format(command+crc))
            read_buffer = self._socket.read(7)
            _LOGGER.info("get status：{}".format(read_buffer))

        if len(read_buffer) != 7 or \
           read_buffer[0] != self._address or \
           read_buffer[1] != 0x01 or \
           read_buffer[2] != 0x02:
            _LOGGER.warning("read status get error feedback")
            return

        status = read_buffer[3] & (0x01<<self._coil)
        self._is_on = (status!=0)
        time.sleep(0.1)

