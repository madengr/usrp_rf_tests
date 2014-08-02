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
- Ettus Research B200 (http://www.ettus.com)
- GNU Radio 3.7.5 (https://github.com/gnuradio/gnuradio)

The purpose of these tests is to generate graphs that are useful for setting the TX and RX gain stages of the USRP.  They also serve as an experiment to mix the GNU Radio flow graph with real-time measurements via GPIB.

![Alt text](https://github.com/madengr/usrp_rf_tests/blob/master/apps/usrp_one_tone_tx_power_graph.png)

![Alt text](https://github.com/madengr/usrp_rf_tests/blob/master/apps/usrp_two_tone_tx_power_graph.png)

![Alt text](https://github.com/madengr/usrp_rf_tests/blob/master/apps/usrp_two_tone_tx_imd3_graph.png)
