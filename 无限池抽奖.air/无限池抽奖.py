# -*- encoding=utf8 -*-
__author__ = "xubowu"
import datetime
from airtest.core.api import *
ST.THRESHOLD = 0.8

auto_setup(__file__)
total = 100;
count = 4;
sell = True;
couponRedeem = True;
couponType = 3;

def redeemCoupon():
    global couponType
    if(exists(Template(r"tpl1640133084099.png", record_pos=(-0.254, -0.075), resolution=(2532, 1170)))):
        touch((950,400))
        if couponType == 3:
            touch ((1300,800)) 
        elif couponType ==1:
            touch((1300,350))
        elif couponType ==2:
            touch((1300,600))
        swipe((920,660), (1700,660))
        touch(Template(r"tpl1640133413239.png", record_pos=(0.112, 0.175), resolution=(2532, 1170)))
        return None;

    else: 
        print("NotFound")
        return None;
def clearMailBox():
    global couponRedeem 
    redeemCount = 0
    touch((1600,900))
    print(redeemCount)
    print(couponRedeem)
    while (exists(Template(r"tpl1632092167816.png", record_pos=(0.002, -0.004), resolution=(2532, 1170)))==False):
        if (redeemCount==0 and couponRedeem==True):
            redeemCoupon()   
            sleep(3)
        wait(Template(r"tpl1632092063050.png", record_pos=(0.274, -0.088), resolution=(2532, 1170)))
        touch((1950,350))
        wait(Template(r"tpl1632092095121.png", record_pos=(0.126, 0.128), resolution=(2532, 1170)))
        touch((1600,900))
        sleep(3)
        redeemCount =redeemCount+1
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
        touch(Template(r"tpl1640131982901.png", record_pos=(0.235, -0.106), resolution=(2532, 1170)))

        touch(Template(r"tpl1640128794963.png", record_pos=(0.201, -0.103), resolution=(2532, 1170)))
        touch(Template(r"tpl1640128986388.png", record_pos=(0.063, -0.143), resolution=(2532, 1170)))

    else : 
        touch((1250,900))
        wait(Template(r"tpl1632092615392.png", record_pos=(-0.386, -0.203), resolution=(2532, 1170)))
        touch((275,65))
def collect():
    try:
        wait(Template(r"tpl1640129003664.png", record_pos=(-0.224, 0.071), resolution=(2532, 1170)))

        touch((780,692),110)
        collect()
    except TargetNotFoundError:
        if(exists(Template(r"tpl1640129042986.png", record_pos=(-0.217, 0.031), resolution=(2532, 1170)))):
            return None
        if exists(Template(r"tpl1632089176760.png", record_pos=(0.001, -0.001), resolution=(2532, 1170))):
            touch((1600,900))
            collect()
        if exists(Template(r"tpl1632091786617.png", record_pos=(0.002, -0.076), resolution=(2532, 1170))):
            clearMailBox()
            collect()
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

