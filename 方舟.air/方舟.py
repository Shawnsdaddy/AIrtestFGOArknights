# -*- encoding=utf8 -*-
__author__ = "xubowu"

from airtest.core.api import *
ST.THRESHOLD = 0.8
auto_setup(__file__)
from poco.drivers.ios import iosPoco
import datetime

poco = iosPoco()
iphone6s = {"confirmload": (1900, 1000), "cancelload": (1300,1000)}
ipad = {"confirmload": (1800, 1150), "cancelload": (1300,1150)}
iphone12 = {"confirmload": (2000,950), "cancelload":(1500,950)}
total = 21;
count = 1;
autoLoadPoint = True;

deviceconfig = iphone12;
def battleStart():
    wait(Template(r"tpl1626937650893.png", record_pos=(0.372, 0.187), resolution=(2532, 1170)))
    touch(Template(r"tpl1626937650893.png", record_pos=(0.372, 0.187), resolution=(2532, 1170)))
    sleep(1)
    notEnough=exists(Template(r"tpl1626938991391.png", record_pos=(-0.321, -0.059), resolution=(2532, 1170)))
    if notEnough!= False:
        if autoLoadPoint==True:
            touch(deviceconfig["confirmload"])
            raise Exception('继续')
        else :
            touch(deviceconfig["cancelload"])
            raise Exception('结束')
    wait(Template(r"tpl1626937699168.png", record_pos=(0.297, 0.094), resolution=(2532, 1170)))
    touch(Template(r"tpl1626937699168.png", record_pos=(0.297, 0.094), resolution=(2532, 1170)))
def waitBattleFinish():
    try:
        wait(Template(r"tpl1626937446602.png", record_pos=(-0.322, 0.176), resolution=(2532, 1170)))
        sleep(1.5)
        touch(Template(r"tpl1626937446602.png", record_pos=(-0.322, 0.176), resolution=(2532, 1170)))
        return None;
    except TargetNotFoundError:
        waitBattleFinish()
def arknStart(deviceconfig): 
    global count
    while count <= total:
        try:
            battleStart();
            waitBattleFinish()
            print("finish "+ str(count))
            count += 1;
            snapshot(filename = "test.png")
        except Exception as e:
            if str(e)=='继续':
                continue
            elif str(e)=='结束':
                break
            else: 
                print(e)
                break
arknStart(deviceconfig)
    #snapshot(filename = "test.png")