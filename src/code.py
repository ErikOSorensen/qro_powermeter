import time
import board
import analogio
import busio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from lcd.lcd import CursorMode


pot1 = analogio.AnalogIn(board.GP26)
pot2 = analogio.AnalogIn(board.GP27)
i2c = busio.I2C(board.GP21, board.GP20)

lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)


def voltage(pot):
    return 3.3/65535 * pot.value

lcd.clear()
while True:
    lcd.set_cursor_pos(0, 0)

    results = "V1=%3.2f, V2=%3.2f" % (voltage(pot1), voltage(pot2))
    lcd.print(results)
    print(results)
    time.sleep(1)
