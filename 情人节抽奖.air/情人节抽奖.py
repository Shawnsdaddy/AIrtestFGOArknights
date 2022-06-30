# -*- encoding=utf8 -*-
__author__ = "frank"

from airtest.core.api import *

ST.THRESHOLD = 0.8
auto_setup(__file__)
while exists(Template(r"tpl1645738106652.png", record_pos=(0.209, -0.027), resolution=(1280, 720)))!=False:
        try:
            touch(Template(r"tpl1645738106652.png", record_pos=(0.209, -0.027), resolution=(1280, 720)))
            sleep(0.5)
            touch(Template(r"tpl1645738155363.png", record_pos=(0.132, 0.1), resolution=(1280, 720)))
            sleep(0.5)
            touch(Template(r"tpl1645738164413.png", record_pos=(0.003, 0.157), resolution=(1280, 720)))
            
            touch(Template(r"tpl1645738195143.png", record_pos=(0.434, -0.252), resolution=(1280, 720)))
            sleep(0.5)
            touch(Template(r"tpl1645738222816.png", record_pos=(0.145, 0.155), resolution=(1280, 720)))
            sleep(0.5) 
            touch(Template(r"tpl1645738232372.png", record_pos=(0.002, 0.159), resolution=(1280, 720)))      
            sleep(0.5)
        except Exception as e:
            touch((1200,40))
            touch(Template(r"tpl1645738222816.png", record_pos=(0.145, 0.155), resolution=(1280, 720)))
            touch(Template(r"tpl1645738232372.png", record_pos=(0.002, 0.159), resolution=(1280, 720)))  