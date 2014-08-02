#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 11:31:46 2014
RF instrument library for Linux GPIB
@author: madengr
"""

import gpib

class SpecAn8566B():
    """HP 8566B spectrum analyzer class with GPIB control"""

    def __init__(self, address):
        """Initialize the object

        Keyword arguments:
        device -- GPIB address of the instrument
        """
        self.device = gpib.dev(0, address)

    def preset(self):
        """Preset the instrument"""
        gpib.write(self.device, "IP")
        return()

    def sweep(self):
        """Take a sweep"""
        gpib.write(self.device, "TS")
        return()

    def set_center_freq(self, center_freq):
        """Set center frequency

        Keyword arguments:
        center_freq -- Center frequency in Hz
        """
        cmd = "CF" + str(center_freq) + "HZ"
        gpib.write(self.device, cmd)
        return()

    def set_span(self, span):
        """Set span

        Keyword arguments:
        span -- Span in Hz
        """
        cmd = "SP" + str(span) + "HZ"
        gpib.write(self.device, cmd)
        return()

    def set_rbw(self, rbw):
        """Set resolution bandwidth

        Keyword arguments:
        rbw -- RBW in Hz
        """
        cmd = "RB" + str(rbw) + "HZ"
        gpib.write(self.device, cmd)
        return()

    def set_vbw(self, vbw):
        """Set video bandwidth

        Keyword arguments:
        vbw -- VBW in Hz
        """
        cmd = "VB" + str(vbw) + "HZ"
        gpib.write(self.device, cmd)
        return()

    def set_ref_level(self, ref_level):
        """Set reference level

        Keyword arguments:
        ref_level -- Reference level in dBm
        """
        cmd = "RL" + str(ref_level)
        gpib.write(self.device, cmd)
        return()

    def set_mkr_freq(self, mkr_freq):
        """Set marker frequency

        Keyword arguments:
        mkr_freq -- Marker frequency in Hz
        """
        cmd = "MKF" + str(mkr_freq) + "HZ"
        gpib.write(self.device, cmd)
        return()

    def get_mkr_amp(self):
        """Get marker amplitude

        Return marker value in dBm
        """
        gpib.write(self.device, "MA")
        result = gpib.read(self.device, 8)
        return float(result)

def test():
    """Test to run through all 8566B methods"""
    specan = SpecAn8566B(18)
    specan.preset()
    specan.set_center_freq(1E9)
    specan.set_span(500E3)
    specan.set_rbw(1E3)
    specan.set_vbw(1E3)
    specan.set_ref_level(30)
    specan.set_mkr_freq(1E9)
    specan.sweep()
    print "Marker at " +  str(specan.get_mkr_amp()) + " dBm"

if __name__ == '__main__':
    try:
        test()
    except KeyboardInterrupt:
        pass
