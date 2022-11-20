# octopus_rur22 - tetro ultra replica
# --- punched card/tape reader ---
# KPX80 (10 x photo T)
# DoIt adapter BOARD
# simple 3D case
# ESP32 / Mictopython


from machine import Pin, I2C
from time import sleep, sleep_ms
from micropython import const
from components.led import Led
from components.rgb import Rgb
from components.analog import Analog

print("--- init ---")
DEBUG = False


d0 = 26
d1 = 35
d2 = 34
d3 = 39
d4 = 36
treshold = 2000

rgb = Rgb(27,8)

def rgb_clear():
    for i in range(7):
        rgb.color((0,0,0),i)
        
def rgb_show(d):
    for i in range(len(d)):        
        if d[i]:
            rgb.color((20,0,0),i) # 1 = GREEN
        else:
            rgb.color((2,8,0),i)  # 0 = RED
    
        
        
def debug_print(s):
    if DEBUG:
        print("DEBUG: ")
        print(s)
        

def data_read():
    dig0, dig1, dig2, dig3, dig4 = 0,0,0,0,0
    data0 = ad0.get_adc_aver(3)
    data1 = ad1.get_adc_aver(3)
    data2 = ad2.get_adc_aver(3)
    data3 = ad3.get_adc_aver(3)
    data4 = ad4.get_adc_aver(3)
    raw_data = data0,data1,data2,data3,data4
    debug_print(raw_data)
    
    if data0 < treshold: dig0 = 1        
    if data1 < treshold: dig1 = 1
    if data2 < treshold: dig2 = 1
    if data3 < treshold: dig3 = 1
    if data4 < treshold: dig4 = 1
        
    data = dig0, dig1, dig2, dig3, dig4 
    return(data)
    
        
print("rgb_clear")
rgb_clear()

# analog
ad0 = Analog(d0)
ad1 = Analog(d1)
ad2 = Analog(d2)
ad3 = Analog(d3)
ad4 = Analog(d4)

print("start")
old_d = 0,0,0,0,0
data_arr = {}
cnt = 0

while True:
    d = data_read()
    if old_d == d:
        print("=",end="") 
    else:
        old_d = d
        print()
        print(cnt, d)
        cnt += 1
        rgb_show(d)
        #data_arr.ad
    sleep_ms(100)
    

        



