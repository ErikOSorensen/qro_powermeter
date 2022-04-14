# QRO powermeter

The plan is to build a power meter that can work for my amateur radio operation for HF and maybe 6m. 
The sensor hardware is the 
[U02 - Power / SWR measuring coupler](https://www.dj0abr.de/english/technik/dds/epwrswrV2.htm), 
using two AD8307 chips to measure the incident and reflected power with a voltage
out about 25mV/dBm. This is the same approach as Larry Phipps, N8LP, used in the original 
LP100 meter, as documented in his [QEX paper](http://www.telepostinc.com/Files/phipps-1.pdf).

I aim to measure between 1mW an 400W, and want to build a board with code that can take care of:

- Measure forward power and return loss with reasonable accuracy based on the voltage output of the AD8307 chips. 
- Report forward power and return loss to an LCD screen on a box.
- Ethernet connection (with DPCP) and logging of measurements to an MQTT server whenever the board determines there is a transmission.
- Allow for future modification to  include a frequency counter such that the log automatically can detect which band is being used.

In terms of technology, I have decided that I want to use a Raspberry Pi PICO, and I want to program it in 
one of the microcontroller Python dialects available. These boards don't have ethernet built in, and I hope 
to interface with something like a Wiznet 5500 (I have a couple of these on hand). In part these decisions were
made with an eye to technologies I would like to learn as much as what is technically necessary (the microcontroller
should be way over-powered for the purpose, a simple Arduino would probably work).

There are two Python dialects for microcontrollers. There is [MicroPython](https://micropython.org/), and there
is [CircuitPython](https://circuitpython.org/) (which is a fork of MicroPython). For this first attempt at 
programming microcontrollers in Python, I'll leave aside the philosophical differences between the two dialects and 
focuse on what is easiest to get started with. It seems that CircuitPython is more likely to be able to talk
to the Wiznet 5500 ethernet adapter, so I'll start out with that.

# Prototyping setup

To get started, I have made up a breadboard with the following ingredients: 

- The Raspberry Pi PICO, which will be USB bus powered. 
- A 16x2 LCD display with an I2C interface hat.
- Two 10k potentiometer and a voltage reference to provide 0-2.5V to the ADC on the Pico.
- The Wiznet adapter (an "ARCELI W5500 Ethernet Network Module")  available online from many sources.

I plan to use the ADC of the Raspberry Pi (at least initially). It provides 12 bit ADCs, and the voltage ref can be 
supplied externally if one removes an onboard resistor divider. 12 bit ADC on a 2.5V range should be 0.6 mV per count, 
and with the AD8307 providing 25mV/dBm, this should be plenty of accuracy. 






