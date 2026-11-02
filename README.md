# Air quality detector with OLED screen

<img width="301" height="628" alt="image" src="https://github.com/user-attachments/assets/e9a105b3-bd2e-412a-98af-3ef517314b64" />

A custom CO2 detector that displays the information on an OLED screen and has a LED Alarm. Made for Half Life W4! #YSWS

## Features 

* Uses the MQ-135 air quality sensor to detect the ppm os different nocive gases present in the air surrounding the device
* Has an 0.96 inches OLED screen to display the sensor's information and recommendations
* Has an alarm feature, where if the ppm exceed a certain threshold, an LED starts blinking and the screen shows a warning
* It also has a button the user can click to snooze the alarm for a minute. After that time passes, the sensor may trigger the alarm again if the ppm hadn't dropped below the predefined threshold
* It uses a XIAO-ESP32-C3 as the microcontroller

## Firmware

The firmware is a python script designed to run in MicroPython. It uses the standard libraries, together with an [external libaray](https://github.com/rubfi/MQ135) to get the readings from the MQ-135 module, and MicroPython's official [ssd1306](https://github.com/micropython/micropython-lib/blob/master/micropython/drivers/display/ssd1306/ssd1306.py) library. 

All the firmware can be found in `/firmware`.

The firmware was written in VSCode, using the `micropython-stubs` pip package, installed in a venv, with some special settings found in `/.vscode/settings.json`

## Production

Gerbers were generated using `Fabrication Toolkit`, a KiCad plugin that generates gerbers and drill files following JLCPCB guidelines and requirements.

They can be found inside `/co2-detector/production` as files, and compressed in `/gerbers.zip`.

## BOM Table

Pending

## Screenshots

<img width="301" height="557" alt="image" src="https://github.com/user-attachments/assets/c052180a-9c99-4a70-bc3b-48809762e296" />

_The PCB Layout_

<img width="317" height="619" alt="image" src="https://github.com/user-attachments/assets/bf9aac76-e12a-428d-8b0a-52eb29eb2ed9" />

_Front render_

<img width="317" height="619" alt="image" src="https://github.com/user-attachments/assets/eacea559-a2a5-4bd0-a9b3-4f9dfd060a31" />

_Back render_

<img width="671" height="563" alt="image" src="https://github.com/user-attachments/assets/60454a33-70f6-4fe0-86df-60096d663758" />

_The schematic_


