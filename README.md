# Air quality sensor with OLED screen

<img width="327" height="645" alt="image" src="https://github.com/user-attachments/assets/00966d71-af70-4a95-bff6-935fe28a88d2" />

A custom CO2 detector that displays the information on an OLED screen and has a LED Alarm. Made for Half Life W4! #YSWS

## Features 

* Uses the MQ-135 air quality sensor to detect the ppm os different nocive gases present in the air surrounding the device
* Has an 0.96 inches OLED screen to display the sensor's information and recommendations
* Has an alarm feature, where if the ppm exceed a certain threshold, an LED starts blinking and the screen shows a warning
* The alarm includes a buzzer that makes sounds at the same time the LED blinks (not added to the firmware yet)
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

| **Item**                 | **Qty** | **Supplier**  | **Cost/item** | **Total Cost** | **link**                                                                                                                                            | **Note**                                                                    |
|--------------------------|---------|---------------|---------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| 0.96 OLED                | 1       | Temu          | $5.00         | $5.00          | https://www.temu.com/ec/2-piezas--de-pantalla-oled-de-0-96-pulgadas-12864-128x64--vcc-start-----pantalla-de--compatible-con--g-605685932739878.html |                                                                             |
| XIAO-ESP32-C3            | 1       | Seeed Studio  | $4.90         | $4.90          | https://www.seeedstudio.com/Seeed-XIAO-ESP32C3-p-5431.html                                                                                          |                                                                             |
| MQ-135                   | 1       | Novatronic EC | $4.50         | $4.50          | https://novatronicec.com/index.php/product/mq-135-sensor-calidad-de-aire/                                                                           | In person order, so no shipping                                             |
| PCB                      | 1       | Novatronic EC | $3.00         | $3.00          | https://novatronicec.com/index.php/product/fabricacion-de-circuitos-impresos-pcb/                                                                   | In person order, so no shipping                                             |
| Red LED                  | 1       | Local store   | $0.05         | $0.05          | N/A                                                                                                                                                 | I already have it                                                           |
| Small button             | 1       | Local store   | $0.05         | $0.05          | N/A                                                                                                                                                 | I already have it                                                           |
| Buzzer                   | 1       | Temu          | $2.46         | $2.46          | https://www.temu.com/ec/10-piezas---3v-5v-12v--magnetico--con--de-pitido-largo-y--12095-12-9-5mm-tmb12a03-tmb12a05-tmb12a12-g-605865197328055.html  | I may be able to buy this in person, but in case I can't I'm putting a link |
|                          |         |               |               |                |                                                                                                                                                     |                                                                             |
| Estimated total shipping | 1       |               |               | $8.73          |                                                                                                                                                     |                                                                             |

## Screenshots

<img width="290" height="533" alt="image" src="https://github.com/user-attachments/assets/bf96ceef-4ebf-40c7-96b7-212aad4d320a" />

_The PCB Layout_

<img width="327" height="645" alt="image" src="https://github.com/user-attachments/assets/00966d71-af70-4a95-bff6-935fe28a88d2" />

_Front render_

<img width="365" height="644" alt="image" src="https://github.com/user-attachments/assets/067c485d-3c8c-473e-a9b5-2fb1e2f80a7d" />

_Back render_

<img width="685" height="550" alt="image" src="https://github.com/user-attachments/assets/e7f725ed-6d22-4b6b-a60c-42785ba20b11" />

_The schematic_


