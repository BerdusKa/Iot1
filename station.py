import time
import thingspeak
import seeed_dht
from grove_light_sensor_v1_2 import GroveLightSensor

import RPi.GPIO as GPIO

channel_id = 2805668
write_key = 'ZTJF6UHFXBC9P1W4'
read_key = 'YQBOZKSPX1DLO93V'

pin = 4

def main(channel):
    from grove.helper import helper
    # for DHT11/DHT22
    sensor = seeed_dht.DHT("11", 5)
    
    pin = 12
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

    # create PWM instance
    pwm = GPIO.PWM(pin, 10)

    light_sensor = GroveLightSensor(0)

    while True:
        humi, temp = sensor.read()
        light = light_sensor.light
        print('DHT{0}, humidity {1:.1f}%, temperature {2:.1f}*'.format(sensor.dht_type, humi, temp))
        print('Light value: {0}'.format(light_sensor.light))    

        #write
        response = channel.update({'field1': temp, 'field2': humi, 'field3': light})  
        
        if(temp > 25):
            pwm.start(5) 
            time.sleep(5)
            pwm.stop()

        time.sleep(10)


if __name__ == '__main__':
    channel = thingspeak.Channel(id=channel_id, api_key=write_key)
    while True:
        main(channel)
        time.sleep(15)
