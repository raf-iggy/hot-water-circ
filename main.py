import time
import board
#import adafruit_ds3231
import busio
import rtc
import idiot_light

#i2c = busio.I2C(board.SCL, board.SDA)
#ds3231 = adafruit_ds3231.DS3231(i2c)
#rtc.set_time_source(ds3231)

#t = ds3231.datetime
#print(t)
#print(time.localtime())

#timeTuple = time.struct_time((2020, 2, 14, 21, 34, 45, 5, 46, -1))
#ds3231.datetime = timeTuple


# For Trinket M0, Gemma M0, ItsyBitsy M0 Express and ItsyBitsy M4 Express
# import adafruit_dotstar
# led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)

# For Feather M0 Express, Metro M0 Express, Metro M4 Express and Circuit Playground Express
#import neopixel
#led1 = neopixel.NeoPixel(board.NEOPIXEL, 1)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return 0, 0, 0
    if pos < 85:
        return int(255 - pos * 3), int(pos * 3), 0
    if pos < 170:
        pos -= 85
        return 0, int(255 - pos * 3), int(pos * 3)
    pos -= 170
    return int(pos * 3), 0 , int(255 - (pos * 3))


#led.brightness = 0.01

i = 0

t = time.mktime((2020,2,20,14,10,01,1,1,-1))
t_now = time.monotonic()

while True:
    i = (i * 1 + 85 + 7) % 256  # run from 0 to 255
    #led.fill(wheel(i))
    print(int(i), wheel(i), end = " ")
    time.sleep(.25)
    #led.fill((0,0,0))  #blanking
    #time.sleep(.2)
    idiot_light.fill_led(i)

    print(time.localtime(t))
    del_t = time.monotonic() - t_now
    print(del_t)
    t= t + del_t