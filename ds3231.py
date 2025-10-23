# ds3231.py - Simple DS3231 RTC library for MicroPython

from machine import I2C
import time

class DS3231:
    def __init__(self, i2c, address=0x68):
        self.i2c = i2c
        self.address = address

    def _bcd2dec(self, b):
        return (b // 16) * 10 + (b % 16)

    def _dec2bcd(self, d):
        return (d // 10) * 16 + (d % 10)

    def datetime(self, dt=None):
        if dt is None:
            data = self.i2c.readfrom_mem(self.address, 0x00, 7)
            ss = self._bcd2dec(data[0] & 0x7F)
            mm = self._bcd2dec(data[1])
            hh = self._bcd2dec(data[2])
            wday = self._bcd2dec(data[3])
            dd = self._bcd2dec(data[4])
            mmn = self._bcd2dec(data[5])
            yy = self._bcd2dec(data[6]) + 2000
            return (yy, mmn, dd, hh, mm, ss, wday)
        else:
            yy, mmn, dd, hh, mm, ss, wday = dt
            data = bytes([
                self._dec2bcd(ss),
                self._dec2bcd(mm),
                self._dec2bcd(hh),
                self._dec2bcd(wday),
                self._dec2bcd(dd),
                self._dec2bcd(mmn),
                self._dec2bcd(yy - 2000)
            ])
            self.i2c.writeto_mem(self.address, 0x00, data)
