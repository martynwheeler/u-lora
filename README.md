# u-lora
raspi-lora for micropython

I have ported raspi-lora (https://pypi.org/project/raspi-lora/) to micropython.

I have currently only tested on raspberry pi pico.

Example usage (server mode):

Create a file main.py with the following contents and copy it across together with the library ulora.py to your microcontroller

```
from time import sleep
from ulora import LoRa, ModemConfig

# This is our callback function that runs when a message is received
def on_recv(payload):
    print("From:", payload.header_from)
    print("Received:", payload.message)
    print("RSSI: {}; SNR: {}".format(payload.rssi, payload.snr))

# Lora Parameters (this is on the raspberry pi pico)
RFM95_RST = 27 # wire gpio 27 to RST
RFM95_CS = 0 # use the spi0 (pins 4 (MOSI), 5 (CS), 6 (SCK), 7 (MISO))
RFM95_INT = 28 # wire gpio 27 to D0
RF95_FREQ = 868.0 # RF for Europe
RF95_POW = 20
SERVER_ADDRESS = 2

# initialise radio
lora = LoRa(RFM95_CS, RFM95_INT, SERVER_ADDRESS, reset_pin=RFM95_RST, freq=RF95_FREQ, tx_power=RF95_POW, acks=True)

# set callback
lora.on_recv = on_recv

# set to listen continuously
lora.set_mode_rx()

# loop and wait for data
while True:
    sleep(0.1)
```

Example usage (client mode):
Create a file main.py with the following contents and copy it across together with the library ulora.py to your microcontroller

```
from time import sleep
from ulora import LoRa, ModemConfig

# Lora Parameters
RFM95_RST = 27
RFM95_CS = 0
RFM95_INT = 28
RF95_FREQ = 868.0
RF95_POW = 20
CLIENT_ADDRESS = 1
SERVER_ADDRESS = 2

# initialise radio
lora = LoRa(RFM95_CS, RFM95_INT, CLIENT_ADDRESS, reset_pin=RFM95_RST, freq=RF95_FREQ, tx_power=RF95_POW, acks=True)

# loop and send data
while True:
    lora.send_to_wait("This is a test message", SERVER_ADDRESS)
    print("sent")
    sleep(10)
```
