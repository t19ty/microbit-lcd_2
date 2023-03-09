from microbit import*
from machine import PIN, SPI
from Pin import framebuf
from LCD1IN8 import LCD_Driver
#include "MicroBitPin.h"
#include "mbed.h"
#include "LCD_Driver.h"
#include "SPI_RAM.h"
#define LCD_SPI_Write_Byte(value) lcd_spi.write(value)
LCD1IN8.LCD_Init()
buf = bytearray(160*128*2)
bitmap = [0, 16, 16, 16, 16, 16, 16, 16, 16]
fb = Buffer.from_array(bitmap) 
# Define a function to display the bitmap image on the LCD
def display_bitmap():
    x = 0
    y = 0
    LCD_CS = 0
    LCD_DC = 1
    LCD_SPI_Write_Byte(fb);
    LCD_CS = 1

# Display the bitmap image on the LCD
display_bitmap()