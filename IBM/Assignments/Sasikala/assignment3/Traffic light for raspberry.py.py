import wiringpi2 as wiringpi
import time

# initialize
wiringpi.wiringPiSetup()

# define GPIO mode
GPIO18 = 1
GPIO23 = 4
GPIO24 = 5
LOW = 0
HIGH = 1
OUTPUT = 1
wiringpi.pinMode(GPIO18, OUTPUT)
wiringpi.pinMode(GPIO23, OUTPUT)
wiringpi.pinMode(GPIO24, OUTPUT)


# make all LEDs off
def clear_all():
    wiringpi.digitalWrite(GPIO18, LOW)
    wiringpi.digitalWrite(GPIO23, LOW)
    wiringpi.digitalWrite(GPIO24, LOW)

# turn on LED sequentially
try:
    while 1:
        clear_all()
        print("turn on LED 1")
        wiringpi.digitalWrite(GPIO18, HIGH)
        time.sleep(2)
        clear_all()
        print("turn on LED 2")
        wiringpi.digitalWrite(GPIO23, HIGH)
        time.sleep(2)
        clear_all()
        print("turn on LED 3")
        wiringpi.digitalWrite(GPIO24, HIGH)
        time.sleep(2)

except KeyboardInterrupt:
    clear_all()

print("done")