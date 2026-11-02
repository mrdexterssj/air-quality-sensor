from machine import Pin, I2C
from mq135 import MQ135
import ssd1306
import time

mq135 = MQ135(3)
i2c = I2C(sda=Pin(7), scl=Pin(6))
display = ssd1306.SSD1306_I2C(128, 64, i2c)
led = Pin(4, Pin.OUT)
button = Pin(10, Pin.IN, Pin.PULL_UP)

alarm_on = False
last_sensor_read = 0
last_led_blink = 0
led_on = False
last_snooze_time = 0
alarm_snooze = False

while True:
    now = time.ticks_ms()

    if time.ticks_diff(now, last_sensor_read) > 10000: # Done every 10 s
        current_ppm = mq135.get_ppm()
        display.fill(0)
        display.text(f"Air ppm: {current_ppm}", 0, 0, 1)
        if current_ppm < 300:
            display.text("Invalid readings or Too low", 0, 12)
        elif current_ppm <= 600:
            display.text("Air quality: Excelent", 0, 12)
        elif current_ppm <= 1000:
            display.text("Air quality: Acceptable", 0, 12)
        elif current_ppm <= 1500:
            display.text("Air quality: Moderate", 0, 12)
            display.text("You should open a window", 0 , 24)
        else:
            display.text("Air quality: Poor", 0, 12)
            display.text("Please ventilate the area!", 0, 24)
            if not alarm_snooze:
                alarm_on = True
            elif time.ticks_diff(now, last_snooze_time) > 60000: #Checks if a minute has passed
                alarm_snooze = False
            else:
                display.fill_rect(0, 36, 128, 8, 0)
                display.text("ALARM SNOOZED FOR A MINUTE!", 0, 36)
        last_sensor_read = now
        display.show()

    if button.value() == 0:
        alarm_snooze = True
        last_snooze_time = now
        alarm_on = False
        led_on = False
        led.off()
        last_led_blink = 0
        display.text("ALARM SNOOZED FOR A MINUTE!", 0, 36)
        display.show()

    if alarm_on and time.ticks_diff(now, last_led_blink) > 500: # Done every 0.5 s
        if not led_on:
            led_on = True
            led.on()
        else:
            led_on = False
            led.off()
        last_led_blink = now