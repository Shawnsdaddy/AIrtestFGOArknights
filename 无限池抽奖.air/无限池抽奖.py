# -*- encoding=utf8 -*-
__author__ = "xubowu"
import datetime
from airtest.core.api import *
ST.THRESHOLD = 0.8

auto_setup(__file__)
total = 349;
count = 283;
sell = True;


def clearMailBox():
    touch((1600,900))
    
    while (exists(Template(r"tpl1632092167816.png", record_pos=(0.002, -0.004), resolution=(2532, 1170)))==False):
    
        wait(Template(r"tpl1632092063050.png", record_pos=(0.274, -0.088), resolution=(2532, 1170)))
        touch((1950,350))
        wait(Template(r"tpl1632092095121.png", record_pos=(0.126, 0.128), resolution=(2532, 1170)))
        touch((1600,900))
        sleep(3)
    #卖掉
    if sell :
        touch((800,750))
        wait(Template(r"tpl1632092436300.png", record_pos=(-0.382, -0.149), resolution=(2532, 1170)))
        swipe((450,400), ((1750,870)),duration=3)
        sellCount = 1; 
        while sellCount <=5: 
            swipe((443,1035), ((1750,1035)),duration=3)
            sellCount += 1
        touch((2100,1100))
        wait(Template(r"tpl1632108700318.png", record_pos=(0.127, 0.169), resolution=(2532, 1170)))
        touch((1600,1000))

        wait(Template(r"tpl1632092589088.png", record_pos=(0.003, 0.171), resolution=(2532, 1170)))
        touch((1250,1000))
        touch(Template(r"tpl1632092615392.png", record_pos=(-0.386, -0.203), resolution=(2532, 1170)))
        touch(Template(r"tpl1632108773544.png", record_pos=(0.229, -0.107), resolution=(2532, 1170)))
        touch(Template(r"tpl1632108788077.png", record_pos=(0.193, -0.101), resolution=(2532, 1170)))
        touch(Template(r"tpl1632109109309.png", record_pos=(0.103, -0.142), resolution=(2532, 1170)))
    else : 
        touch((1250,900))
        wait(Template(r"tpl1632092615392.png", record_pos=(-0.386, -0.203), resolution=(2532, 1170)))
        touch((275,65))
def collect():
    try:
        wait(Template(r"tpl1631982213485.png", record_pos=(-0.226, 0.072), resolution=(2532, 1170)))
        touch((780,692),100)
        collect()
    except TargetNotFoundError:
        if(exists(Template(r"tpl1632076358588.png", record_pos=(-0.221, 0.055), resolution=(2532, 1170)))):
            return None
        if exists(Template(r"tpl1632089176760.png", record_pos=(0.001, -0.001), resolution=(2532, 1170))):
            touch((1600,900))
            collect()
        if exists(Template(r"tpl1632091786617.png", record_pos=(0.002, -0.076), resolution=(2532, 1170))):
            clearMailBox()
            collect()
#def: nextBucket():
def reset():
    touch((2100,400))
    wait(Template(r"tpl1631942364444.png", record_pos=(0.126, 0.13), resolution=(2532, 1170)))
    touch((1600,900))
    wait(Template(r"tpl1632076609376.png", record_pos=(0.001, 0.131), resolution=(2532, 1170)))
    touch((1260,900))

def start():
    global count
    global total
    while count <= total:
        collect()
        reset()
        print("Finish collecging N0. "+str(count))  
        print(datetime.datetime.now())
        count += 1

start()

