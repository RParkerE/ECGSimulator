#######################################################
#Engineering World ECG Simulator Display
#RParkerE
#Python code for RPI ecg simulator display
#ecg_simulator.py
#######################################################

#! /usr/bin/python
 
import RPi.GPIO as GPIO
import time
 
import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

import Image
import ImageDraw
import ImageFont

# Raspberry Pi hardware SPI config:
DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0

# Raspberry Pi software SPI config:
# SCLK = 4
# DIN = 17
# DC = 23
# RST = 24
# CS = 8

# Hardware SPI usage:
disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

# Software SPI usage (defaults to bit-bang SPI interface):
#disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)

points = {}
for x in range (1, 85):
	points[x] = 0
column = 0

# Initialize library.
disp.begin(contrast=60)

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
	
def display(value):  # Code to display information to LCD
	# Get drawing object to draw on image.
	draw = ImageDraw.Draw(image)

	# Draw a white filled box to clear the image.
	draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
	
	for key in points:
		if key < 84:
			draw.line((key, points[key], key+1, points[key+1]), fill=0)
	
	# Write Text
	draw.text((8, 10), 'ECG Wave:', font=font)
	
	# This displays image.
	disp.image(image)
	disp.display()
	
def main():
	ecg_pin_1 = 17   # GPIO Pin Number
	ecg_pin_2 = 22   
	ecg_pin_3 = 25
	ecg_pin_4 = 21
	ecg_pin_5 = 18
	GPIO.setmode(GPIO.BCM) # Sets GPIO mode as GPIO pins
	GPIO.setup(ecg_pin_1, GPIO.IN) # Makes heart_rate_pin read as input
	GPIO.setup(ecg_pin_2, GPIO.IN)
	GPIO.setup(ecg_pin_3, GPIO.IN)
	GPIO.setup(ecg_pin_4, GPIO.IN)
	GPIO.setup(ecg_pin_5, GPIO.IN)	
	
	while True:
		global column
		# Reads GPIO input
		reading_1 = GPIO.input(ecg_pin_1)
		reading_2 = GPIO.input(ecg_pin_2)
		reading_3 = GPIO.input(ecg_pin_3)
		reading_4 = GPIO.input(ecg_pin_4)
		reading_5 = GPIO.input(ecg_pin_5)
		if reading_1 == False and reading_2 == False and reading_3 == False and reading_4 == False and reading_5 == False:
			row = 48 - int(30 * 0) + 1
			column = (column + 1) % 83
			points[column+1] = row
			display('.')
			time.sleep(0.024)
		if reading_1 == True and reading_2 == False and reading_3 == False and reading_4 == False and reading_5 == False:
			row = 48 - int(30 * .033) + 1
			column = (column + 1) % 83
			points[column+1] = row
			display('.')
			time.sleep(0.024)
		if reading_1 == True and reading_2 == True and reading_3 == False and reading_4 == False and reading_5 == False:
			row = 48 - int(30 * .066) + 1
			column = (column + 1) % 83
			points[column+1] = row
			display('.')
			time.sleep(0.024)
		if reading_1 == False and reading_2 == False and reading_3 == True and reading_4 == False and reading_5 == False:
			row = 48 - int(30 * .099) + 1
			column = (column + 1) % 83
			points[column+1] = row
			display('.')
			time.sleep(0.024)
		if reading_1 == True and reading_2 == False and reading_3 == True and reading_4 == False and reading_5 == False:
			row = 48 - int(30 * .132) + 1
			column = (column + 1) % 83
			points[column+1] = row
			display('.')
			time.sleep(0.024)
		if reading_1 == False and reading_2 == True and reading_3 == True and reading_4 == False and reading_5 == False:
			row = 48 - int(30 * .165) + 1
			column = (column + 1) % 83
			points[column+1] = row
			display('.')
			time.sleep(0.024)
		if reading_1 == True and reading_2 == True and reading_3 == True and reading_4 == False and reading_5 == False:
			row = 48 - int(30 * .198) + 1
			column = (column + 1) % 83
			points[column+1] = row
			display('.')
			time.sleep(0.024)
		if reading_1 == False and reading_2 == False and reading_3 == False and reading_4 == True and reading_5 == False:
			row = 48 - int(30 * .231) + 1
			column = (column + 1) % 83
			points[column+1] = row
			display('.')
			time.sleep(0.024)
		if reading_1 == True and reading_2 == False and reading_3 == False and reading_4 == True and reading_5 == False:
			row = 48 - int(30 * .264) + 1
			column = (column + 1) % 83
			points[column+1] = row
			display('.')
			time.sleep(0.024)
		if reading_1 == False and reading_2 == True and reading_3 == False and reading_4 == True and reading_5 == False:
			row = 48 - int(48 * .297) + 1
			column = (column + 1) % 83
			points[column+1] = row
			display('.')
			time.sleep(0.024)
		if reading_1 == True and reading_2 == True and reading_3 == False and reading_4 == True and reading_5 == False:
			row = 48 - int(30 * .33) + 1
			column = (column + 1) % 83
			points[column+1] = row
			display('.')
			time.sleep(0.024)
		if reading_1 == False and reading_2 == False and reading_3 == True and reading_4 == True and reading_5 == False:
			row = 48 - int(30 * .363) + 1
			column = (column + 1) % 83
			points[column+1] = row
			display('.')
			time.sleep(0.024)
		if reading_1 == True and reading_2 == False and reading_3 == True and reading_4 == True and reading_5 == False:
			row = 48 - int(30 * .396) + 1
			column = (column + 1) % 83
			points[column+1] = row
			display('.')
			time.sleep(0.024)
		if reading_1 == False and reading_2 == True and reading_3 == True and reading_4 == True and reading_5 == False:
			row = 48 - int(30 * .429) + 1
			column = (column + 1) % 83
			points[column+1] = row
			display('.')
			time.sleep(0.024)
		if reading_1 == True and reading_2 == True and reading_3 == True and reading_4 == True and reading_5 == False:
			row = 48 - int(30 * .462) + 1
			column = (column + 1) % 83
			points[column+1] = row
			display('.')
			time.sleep(0.024)
		if reading_1 == False and reading_2 == False and reading_3 == False and reading_4 == False and reading_5 == True:
			row = 48 - int(30 * .495) + 1
			column = (column + 1) % 83
			points[column+1] = row
			display('.')
			time.sleep(0.024)
		if reading_1 == True and reading_2 == False and reading_3 == False and reading_4 == False and reading_5 == True:
			row = 48 - int(30 * .528) + 1
			column = (column + 1) % 83
			points[column+1] = row
			display('.')
			time.sleep(0.024)
		if reading_1 == False and reading_2 == True and reading_3 == False and reading_4 == False and reading_5 == True:
			row = 48 - int(30 * .561) + 1
			column = (column + 1) % 83
			points[column+1] = row
			display('.')
			time.sleep(0.024)
		if reading_1 == True and reading_2 == True and reading_3 == False and reading_4 == False and reading_5 == True:
			row = 48 - int(30 * .594) + 1
			column = (column + 1) % 83
			points[column+1] = row
			display('.')
			time.sleep(0.024)
		if reading_1 == False and reading_2 == False and reading_3 == True and reading_4 == False and reading_5 == True:
			row = 48 - int(30 * .627) + 1
			column = (column + 1) % 83
			points[column+1] = row
			display('.')
			time.sleep(0.024)
		if reading_1 == True and reading_2 == False and reading_3 == True and reading_4 == False and reading_5 == True:
			row = 48 - int(30 * .66) + 1
			column = (column + 1) % 83
			points[column+1] = row
			display('.')
			time.sleep(0.024)
		if reading_1 == False and reading_2 == True and reading_3 == True and reading_4 == False and reading_5 == True:
			row = 48 - int(30 * .693) + 1
			column = (column + 1) % 83
			points[column+1] = row
			display('.')
			time.sleep(0.024)
		if reading_1 == True and reading_2 == True and reading_3 == True and reading_4 == False and reading_5 == True:
			row = 48 - int(30 * .726) + 1
			column = (column + 1) % 83
			points[column+1] = row
			display('.')
			time.sleep(0.024)
		if reading_1 == False and reading_2 == False and reading_3 == False and reading_4 == True and reading_5 == True:
			row = 48 - int(30 * .759) + 1
			column = (column + 1) % 83
			points[column+1] = row
			display('.')
			time.sleep(0.024)
		if reading_1 == True and reading_2 == False and reading_3 == False and reading_4 == True and reading_5 == True:
			row = 48 - int(30 * .792) + 1
			column = (column + 1) % 83
			points[column+1] = row
			display('.')
			time.sleep(0.024)
		if reading_1 == False and reading_2 == True and reading_3 == False and reading_4 == True and reading_5 == True:
			row = 48 - int(30 * .825) + 1
			column = (column + 1) % 83
			points[column+1] = row
			display('.')
			time.sleep(0.024)
		if reading_1 == True and reading_2 == True and reading_3 == False and reading_4 == True and reading_5 == True:
			row = 48 - int(30 * .858) + 1
			column = (column + 1) % 83
			points[column+1] = row
			display('.')
			time.sleep(0.024)
		if reading_1 == False and reading_2 == False and reading_3 == True and reading_4 == True and reading_5 == True:
			row = 48 - int(30 * .891) + 1
			column = (column + 1) % 83
			points[column+1] = row
			display('.')
			time.sleep(0.024)
		if reading_1 == True and reading_2 == False and reading_3 == True and reading_4 == True and reading_5 == True:
			row = 48 - int(30 * .924) + 1
			column = (column + 1) % 83
			points[column+1] = row
			display('.')
			time.sleep(0.024)
		if reading_1 == False and reading_2 == True and reading_3 == True and reading_4 == True and reading_5 == True:
			row = 48 - int(30 * .957) + 1
			column = (column + 1) % 83
			points[column+1] = row
			display('.')
			time.sleep(0.024)
		if reading_1 == True and reading_2 == True and reading_3 == True and reading_4 == True and reading_5 == True:
			row = 48 - int(30 * 1) + 1
			column = (column + 1) % 83
			points[column+1] = row
			display('.')
			time.sleep(0.024)
main()
