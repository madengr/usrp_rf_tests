#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 20:28:23 2014
USRP generates one tones with swept gain and frequency
Tone power measured with spectrum analyzer
@author: madengr
"""
import instruments
import numpy as np
import time
from gnuradio import gr
from gnuradio import uhd
from gnuradio import analog
import matplotlib.pyplot as plt

class MyTopBlock(gr.top_block):
    """ Class for one tone output from USRP """

    def __init__(self):

        # Call the initialization method from the parent class
        gr.top_block.__init__(self)

        # Default constants
        # Tone amplitude is -3 dBFS
        uhd_args = "type=b200"
        self.sample_rate = 250E3
        self.center_freq = 3E9
        self.gain = 60
        self.sig0_freq = 100E3
        self.sig_amp = 1/np.sqrt(2)

        # Setup the signal generator source
        sig0 = analog.sig_source_c(self.sample_rate,
                                   analog.GR_SIN_WAVE,
                                   self.sig0_freq,
                                   self.sig_amp)

        # Setup the USRP sink, using self so USRP methods are accesible
        self.usrp = uhd.usrp_sink(uhd_args, uhd.io_type_t.COMPLEX_FLOAT32, 1)
        self.usrp.set_clock_source("external", 0)
        self.usrp.set_samp_rate(self.sample_rate)
        self.usrp.set_center_freq(self.center_freq)
        self.usrp.set_gain(self.gain)

        # Connect the source to sink
        self.connect(sig0, self.usrp)


def main():
    """ Sweep through frequency and gain, and measure power """

    # Create instances of the spectrum analyzer and GR flow
    specan = instruments.SpecAn8566B(18)
    tb = MyTopBlock()

    # Start the flow and wait a little
    tb.start()
    time.sleep(1)

    # Setup the spectrum analyzer
    specan.preset()
    specan.set_ref_level(30)
    specan.set_span(tb.sample_rate)
    specan.set_rbw(3000)
    specan.set_vbw(1000)

    # Create a list of center frequencies and append some more
    center_freq_list = [100E6, 500E6, 1E9]
    center_freq_start = 2E9
    center_freq_stop = 6E9
    center_freq_step = 2E9
    center_freq = center_freq_start
    while center_freq <= center_freq_stop:
        center_freq_list.append(center_freq)
        center_freq = center_freq + center_freq_step

    # Create a list of gains
    gain_start = 70
    gain_stop = 89
    gain_step = 1.0
    gain_list = []
    gain = gain_start
    while gain <= gain_stop:
        gain_list.append(gain)
        gain = gain + gain_step

   # Create arrays to hold the measured tone power
    tone_power = np.zeros((len(center_freq_list), len(gain_list)))

    # Sweep through frequency and gain lists, and measure tone power
    for freq_index, center_freq in enumerate(center_freq_list):
        tb.usrp.set_center_freq(center_freq)
        specan.set_center_freq(center_freq)
        specan.set_mkr_freq(center_freq + tb.sig0_freq)
        print ""
        print "Center Frequency = " + str(center_freq/1E6) + " MHz"

        for gain_index, gain in enumerate(gain_list):
            tb.usrp.set_gain(gain)
            specan.sweep()
            tone_power[freq_index][gain_index] = specan.get_mkr_amp()
            print "Gain = %1.1f dB, SIG0 Power = % 1.1f dBm" % \
                (gain, tone_power[freq_index][gain_index])

    # Stop the flow and wait for it to finish
    tb.stop()
    tb.wait()

    # Save the data to file
    #np.savetxt('data.txt', tone_power, fmt='%+2.2f')

    # Plot the data
    plt.figure(num=0, figsize=(8, 6), dpi=150)
    for freq_index, center_freq in enumerate(center_freq_list):
        freq_label = str(int(center_freq/1E6)) + " MHz"
        plt.plot(gain_list[:], tone_power[freq_index, :], label=str(freq_label))
    plt.legend(loc='upper left')
    plt.xlabel('Gain (dB)')
    plt.ylabel('Power (dBm)')
    plt.grid()
    plt.title("B200 Single Tone TX Test over Frequency and Gain")
    plt.suptitle("%1.3f Tone Amplitude @ %i kHz Offset" % \
        (tb.sig_amp, tb.sig0_freq/1E3))
    plt.savefig('usrp_one_tone_tx_power_graph.png')
    plt.show()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
