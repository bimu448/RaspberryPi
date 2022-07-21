#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import datetime

class lcd1602:
    def __init__(self):
        # GPIO to LCD mapping
        self.lcd_rs = 14
        self.lcd_e = 15
        self.lcd_d4 = 17
        self.lcd_d5 = 18
        self.lcd_d6 = 27
        self.lcd_d7 = 22
        self.channel_list = [self.lcd_d4, self.lcd_d5, self.lcd_d6, self.lcd_d7]
        # Device constants
        self.lcd_char_mode = True    # Character mode
        self.lcd_cmd_mode = False   # Command mode
        self.lcd_line_width = 16    # Characters per line (16 max)
        self.lcd_line1 = 0x80  # LCD memory location for 1st line
        self.lcd_line2 = 0xC0  # LCD memory location 2nd line

        self.port_init()
        self.lcd_init()
        #self.message()

    def port_init(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
        GPIO.setup(self.lcd_e, GPIO.OUT)  # Set GPIO's to output mode
        GPIO.setup(self.lcd_rs, GPIO.OUT)
        GPIO.setup(self.channel_list, GPIO.OUT)

    def lcd_init(self):
        self.lcd_write_cmd(0x33)  # Initialize
        self.lcd_write_cmd(0x32)  # Set to 4-bit mode
        self.lcd_write_cmd(0x06)  # Cursor move direction
        self.lcd_write_cmd(0x0C)  # Turn cursor off
        self.lcd_write_cmd(0x28)  # 2 line display
        self.lcd_write_cmd(0x01)  # Clear display
        time.sleep(0.0005)        # Delay to allow commands to process

    def lcd_write_cmd(self, cmd):
        GPIO.output(self.lcd_rs, self.lcd_cmd_mode)  # RS
        self.write_bits(cmd)

    def lcd_write_chars(self, chars):
        GPIO.output(self.lcd_rs, self.lcd_char_mode)  # RS
        self.write_bits(chars)

    def write_bits(self, bits):
        # High bits
        GPIO.output(self.channel_list, False)
        if bits & 0x10 == 0x10:
            GPIO.output(self.lcd_d4, True)
        if bits & 0x20 == 0x20:
            GPIO.output(self.lcd_d5, True)
        if bits & 0x40 == 0x40:
            GPIO.output(self.lcd_d6, True)
        if bits & 0x80 == 0x80:
            GPIO.output(self.lcd_d7, True)
        self.lcd_toggle_enable()# Toggle 'Enable' pin
        # Low bits
        GPIO.output(self.channel_list, False)
        if bits & 0x01 == 0x01:
            GPIO.output(self.lcd_d4, True)
        if bits & 0x02 == 0x02:
            GPIO.output(self.lcd_d5, True)
        if bits & 0x04 == 0x04:
            GPIO.output(self.lcd_d6, True)
        if bits & 0x08 == 0x08:
            GPIO.output(self.lcd_d7, True)
        self.lcd_toggle_enable()# Toggle 'Enable' pin

    def lcd_toggle_enable(self):
        time.sleep(0.0005)
        GPIO.output(self.lcd_e, True)
        time.sleep(0.0005)
        GPIO.output(self.lcd_e, False)
        time.sleep(0.0005)

    def lcd_text(self, message, line):
        if line == 1:
            line = self.lcd_line1
        else:
            line = self.lcd_line2
        self.lcd_write_cmd(line)

        # Send text to display
        message = message.ljust(self.lcd_line_width, ' ') #align left
        for i in range(self.lcd_line_width):
            self.lcd_write_chars(ord(message[i]))
