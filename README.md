usrp_rf_tests
======

Automated RF tests for the Ettus USRP using GNU Radio and Linux GPIB

Author: Louis Brown KD4HSO

Homepage: https://github.com/madengr/usrp_rf_tests

Features:
- One tone transmit test over swept frequency and gain. 
- Two tone transmit test over swept frequency and gain.
- Tone and IMD3 measurements with 8566B spectrum analyzer
- Instrument control via Linux GPIB (http://linux-gpib.sourceforge.net/)

Tested with:
- Ettus B200 (http://www.ettus.com)
- Ettus UHD 3.7.2 (https://github.com/EttusResearch/uhd)
- GNU Radio 3.7.5 (https://github.com/gnuradio/gnuradio)

The purpose of these tests is to generate graphs for setting the TX and RX gain of the USRP.  They also serve as an experiment to mix the GNU Radio flow with real-time measurements via GPIB.  Note the USRP should be locked to the 10 MHz reference of the spectrum analyzer.  

The one tone TX test consists of a 0.707 amplitude tone at 100 kHz offset from the center frequency.  The tone amplitude is -3 dBFS, which is half power from full scale of the DAC.  The center frequency and hardware gain are swept while recording the tone power on the spectrum analyzer.  The resulting graph may be used to choose a gain setting for desired output power while avoiding gain compression. 

![Alt text](https://github.com/madengr/usrp_rf_tests/blob/master/apps/usrp_one_tone_tx_power_graph.png)

The two tone TX test consists of 0.304 amplitude tones with 25 kHz spacing, offset at 62.5 kHz from the center frequency.  Each tone amplitude is -9 dBFS, thus a combined average power at -6 dBFS, and peak instantaneous power at -3 dBFS.  The center frequency and hardware gain are swept while recording the lower tone power on the spectrum analyzer, as well as the lower IMD3 product.  The resulting graph may be used to choose a gain setting for desired output power while avoiding high levels of IMD3; typically greater than -30 dBc.

![Alt text](https://github.com/madengr/usrp_rf_tests/blob/master/apps/usrp_two_tone_tx_power_graph.png)

![Alt text](https://github.com/madengr/usrp_rf_tests/blob/master/apps/usrp_two_tone_tx_imd3_graph.png)
