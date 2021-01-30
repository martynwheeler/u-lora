from time import sleep
from ulora import LoRa, ModemConfig

# This is our callback function that runs when a message is received
def on_recv(payload):
    print("From:", payload.header_from)
    print("Received:", payload.message)
    print("RSSI: {}; SNR: {}".format(payload.rssi, payload.snr))

# Lora Parameters
RFM95_RST = 27
RFM95_CS = 0
RFM95_INT = 28
RF95_FREQ = 868.0
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

