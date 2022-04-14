import time
import board
import analogio
import busio
import digitalio
import adafruit_requests as requests
from adafruit_wiznet5k.adafruit_wiznet5k import WIZNET5K
import adafruit_wiznet5k.adafruit_wiznet5k_socket as socket


from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from lcd.lcd import CursorMode


pot1 = analogio.AnalogIn(board.GP26)
pot2 = analogio.AnalogIn(board.GP27)
i2c = busio.I2C(board.GP21, board.GP20)

lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

# From wiznet5k_simpletest.py
TEXT_URL = "http://wifitest.adafruit.com/testwifi/index.html"
JSON_URL = "http://api.coindesk.com/v1/bpi/currentprice/USD.json"
cs  = digitalio.DigitalInOut(board.GP13)
rst = digitalio.DigitalInOut(board.GP15)
spi_bus = busio.SPI(board.GP10, MOSI=board.GP11, MISO=board.GP12)

# Initialize ethernet interface with DHCP
eth = WIZNET5K(spi_bus, cs, debug = True)
# Initialize a requests object with a socket and ethernet interface
requests.set_socket(socket, eth)
print("Chip Version:", eth.chip)
print("MAC Address:", [hex(i) for i in eth.mac_address])
print("My IP address is:", eth.pretty_ip(eth.ip_address))


def voltage(pot):
    return 3.3/65535 * pot.value

lcd.clear()
lcd.set_cursor_pos(1,0)
lcd.print("ip: %s" % eth.pretty_ip(eth.ip_address))
print("Wiznet5k WebClient Test")
while True:
    lcd.set_cursor_pos(0, 0)
    results = "V1=%3.2f, V2=%3.2f" % (voltage(pot1), voltage(pot2))
    lcd.print(results)
    # print(results)
    time.sleep(1)
