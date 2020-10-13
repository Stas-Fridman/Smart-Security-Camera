import RPi.GPIO as GPIO
import time

# We use this line of code to avoid warning messages.
GPIO.setwarnings(False)
Pir_Pin = 7
# The GPIO.BCM option means that we are referring to the pins by the “Broadcom SOC channel” number, these are the
# numbers after “GPIO”
GPIO.setmode(GPIO.BOARD)
# We define the PIR-pin (= 7) as an input pin
GPIO.setup(Pir_Pin, GPIO.IN)


def motion_check(Pir_Pin):
    # is an infinitive loop (until we stop the program)
    while True:
        input_state = GPIO.input(Pir_Pin)
        # if the PIR-pin is high (sensor has detected movement)
        if input_state:
            # print('motion_detected')
            # 0.3 ---> is the min value
            time.sleep(0.3)
            # break
            return True


try:
    # callback if it detects some motion
    GPIO.add_event_detect(Pir_Pin, GPIO.RISING, callback=motion_check)
except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
