# -*- encoding=utf8 -*-
__author__ = "frank"

import cv2

from PIL import Image as im

from airtest.core.api import *
from airtest.aircv import *
ST.THRESHOLD = 0.8
ST.FIND_TIMEOUT = 3
ST.FIND_TIMEOUT_TMP = 0
ST.CVSTRATEGY = ['tpl']
from airtest.cli.parser import cli_setup
from PIL import Image
import pytesseract
from datetime import datetime

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Android://127.0.0.1:5037/127.0.0.1:7555?cap_method=JAVACAP^&^&ori_method=ADBORI",
    ])    
iphone6s = {"confirmload": (1900, 1000), "cancelload": (1300,1000)}
ipad = {"confirmload": (1800, 1150), "cancelload": (1300,1150)}
iphone12 = {"confirmload": (2000,950), "cancelload":(1500,950)}
mumu = {"confirmload": (2000,950), "cancelload":(1500,950)}
total =23
count = 1;
autoLoadPoint = False;
showFacilityDetail = False;

swtichMenuLag = 10;
deviceconfig = mumu;

def readScreen(cord):
    screen = G.DEVICE.snapshot()
    local = aircv.crop_image(screen,cord)
    img = cv2.cvtColor(local, cv2.COLOR_BGR2GRAY)
    pil_image = cv2_2_pil(img)
    pil_image.save("F:\Git\AIrtestFGOArknights/score0.png", quality=99, optimize=True)

    image = cv2.imread('F:\Git\AIrtestFGOArknights/score0.png')        
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    thresh = 255 - thresh
    pic = im.fromarray(thresh)
    pic.save("F:\Git\AIrtestFGOArknights/test0.png", quality=99, optimize=True)    
    data = pytesseract.image_to_string(thresh, lang='eng',config='--psm 6')
    return (data.strip())

class Operator:
    def __init__(self,name,onSelectRest,currentEnergy,onSelectDuty,deSelect,group,changeTime):
        self.name = name
        self.onSelectRest=onSelectRest
        self.currentEnergy=currentEnergy
        self.onSelectDuty=onSelectDuty
        self.deSelectRest=deSelect
        self.group=group
        self.changeTime=changeTime
        self.operator = None        
        
    def refreshTime(self,isSelect,retryCount=0):        
        if isSelect==True : 
            touchPic(self.onSelectRest)
            touchPic(self.onSelectRest,1)
        try:
            print(readScreen((452,609,1900,938)))
          #self.changeTime=datetime.strptime(readScreen((487,342,635,386)).strip(), '%H:%M:%S').time()            
        except Exception as e:
            if retryCount<5:
                self.refreshTime(isSelect,retryCount+1)
            else:
                raise Exception('Max retryCount reach')
#         print(readScreen((487,342,635,386)))        
        print(self.changeTime)
#         print(readScreen((540,166,655,219)))
        
    

def touchPic(pic,delay=0):
    touch(pic)
    sleep(delay)
def battleStart():
    #wait(Template(r"tpl1626937650893.png", record_pos=(0.372, 0.187), resolution=(2532, 1170)))
    touch(Template(r"tpl1626937650893.png", record_pos=(0.372, 0.187), resolution=(2532, 1170)))
    sleep(3)
    notEnough=exists(Template(r"tpl1626938991391.png", record_pos=(-0.321, -0.059), resolution=(2532, 1170)))
    if notEnough!= False:
        if autoLoadPoint==True:
            touch(Template(r"tpl1642455994290.png", record_pos=(0.348, 0.172), resolution=(2560, 1440)))


            raise Exception('继续')
        else :
            touch(Template(r"tpl1642456007146.png", record_pos=(0.106, 0.17), resolution=(2560, 1440)))


            raise Exception('结束')
    #wait(Template(r"tpl1626937699168.png", record_pos=(0.297, 0.094), resolution=(2532, 1170)))
    touch(Template(r"tpl1626937699168.png", record_pos=(0.297, 0.094), resolution=(2532, 1170)))
def waitBattleFinish():
    try:
        if(exists(Template(r"tpl1649223411555.png", record_pos=(-0.179, 0.228), resolution=(2240, 1260)))):
            waitBattleFinish()
        else :
            wait(Template(r"tpl1626937446602.png", record_pos=(-0.322, 0.176), resolution=(2532, 1170)))
            sleep(2)
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

# arknStart(deviceconfig)
# swipe((1300,800), (1300,500))
def swipeDevice(direction):
    # swipe((1300,800), (1300,500))
    if(direction=='left'):
        swipe((500,800), (1300,800))
    elif direction=='right':
        swipe((1300,800), (500,800))
# swipeDevice('left')

def collectResource(): 
    if(exists(Template(r"tpl1649356920794.png", record_pos=(0.442, -0.21), resolution=(2240, 1260)))):
        touchPic(Template(r"tpl1649356920794.png", record_pos=(0.442, -0.21), resolution=(2240, 1260)),1)        
        if(exists(Template(r"tpl1649277817432.png", record_pos=(-0.315, 0.261), resolution=(2240, 1260)))):
            touchPic(Template(r"tpl1649277817432.png", record_pos=(-0.315, 0.261), resolution=(2240, 1260)),swtichMenuLag)
        if exists(Template(r"tpl1649358115656.png", record_pos=(-0.313, 0.264), resolution=(2240, 1260))):
            touchPic(Template(r"tpl1649358115656.png", record_pos=(-0.313, 0.264), resolution=(2240, 1260)),swtichMenuLag)   
#         if exists(Template(r"tpl1649362130702.png", record_pos=(-0.046, 0.259), resolution=(2240, 1260))):
#             touchPic(Template(r"tpl1649362130702.png", record_pos=(-0.046, 0.259), resolution=(2240, 1260)),swtichMenuLag)
        if exists(Template(r"tpl1649362178281.png", record_pos=(-0.18, 0.262), resolution=(2240, 1260))):
            touchPic(Template(r"tpl1649362178281.png", record_pos=(-0.18, 0.262), resolution=(2240, 1260)),swtichMenuLag)
    else:
        return None;
def switchMenu(name):   
    print("start switch menu to "+name)
    if exists(Template(r"tpl1649357635930.png", record_pos=(-0.287, -0.251), resolution=(2240, 1260))):
        a = True;
        print('Calendar Exists')
    elif exists(Template(r"tpl1649357408325.png", record_pos=(-0.291, -0.252), resolution=(2240, 1260))):        
        print("Home exists")
        touchPic(Template(r"tpl1649357408325.png", record_pos=(-0.291, -0.252), resolution=(2240, 1260)))       
        touchPic(Template(r"tpl1649357748576.png", record_pos=(-0.428, -0.096), resolution=(2240, 1260)),swtichMenuLag)        
    if(name=='基建'):
        touchPic(Template(r"tpl1649357762378.png", record_pos=(0.27, 0.197), resolution=(2240, 1260)),swtichMenuLag+2)   
def switchFacility(floor,index):
    switchMenu('基建')
    pinch(in_or_out='in')
    y=400 - floor*150
    x=1400
    if index>4:
        x= 2000
    elif index <4:
        x = 290*index
    touchPic((x,y),swtichMenuLag)
def openFacilityDetail(floor,index):
    global showFacilityDetail
    switchFacility(floor,index)
    
    if showFacilityDetail==False:
        touchPic(Template(r"tpl1649401710589.png", record_pos=(-0.448, -0.064), resolution=(2240, 1260)),1)
        showFacilityDetail=True
    touch((1600,300))
    
#openFacilityDetail(-1,1)



#Fiammetta = Operator('菲亚梅塔',Template(r"tpl1649403082887.png", record_pos=(0.103, -0.111), resolution=(2240, 1260)),24,'',Template(r"tpl1649403040465.png", record_pos=(0.089, -0.128), resolution=(2240, 1260)),1,'')
#Fiammetta = Operator('菲亚梅塔',Template(r"tpl1649403082887.png", record_pos=(0.103, -0.111), resolution=(2240, 1260)),24,'',Template(r"tpl1649403040465.png", record_pos=(0.089, -0.128), resolution=(2240, 1260)),1,'')

#Fiammetta.refreshTime(True);

# str1 = '05:56:50'
# str2 = '05:57:50'
# print(datetime.strptime(str2.strip(), '%H:%M:%S'))
# print(datetime.strptime(str2.strip(), '%H:%M:%S')-datetime.strptime(str1.strip(), '%H:%M:%S'))



# switchMenu('基建')
# collectResource()
        
# collectResource()

# os.system("shutdown /s /t 60")


#touch(Template(r"tpl1649277817432.png", record_pos=(-0.315, 0.261), resolution=(2240, 1260)))
# touch(Template(r"tpl1649314570799.png", record_pos=(-0.4, -0.187), resolution=(2240, 1260)))+
def get_sec(time_str):
    """Get seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def switchTrade():

    touchPic(Template(r"tpl1656145700054.png", record_pos=(-0.086, 0.212), resolution=(2560, 1440)))
    touchPic(Template(r"tpl1656145766714.png", record_pos=(-0.011, -0.15), resolution=(2560, 1440)))
    touchPic(Template(r"tpl1656145786583.png", record_pos=(0.215, -0.136), resolution=(2560, 1440)))
    touchPic(Template(r"tpl1656145808681.png", record_pos=(0.421, 0.248), resolution=(2560, 1440)),swtichMenuLag)
    touch(Template(r"tpl1656145829970.png", record_pos=(-0.211, 0.104), resolution=(2560, 1440)))
    touch(Template(r"tpl1656145838306.png", record_pos=(0.251, -0.019), resolution=(2560, 1440)))
    touchPic(Template(r"tpl1656145847945.png", record_pos=(0.241, 0.174), resolution=(2560, 1440)),swtichMenuLag)
    touchPic(Template(r"tpl1656147745803.png", record_pos=(-0.207, 0.077), resolution=(2560, 1440)),swtichMenuLag)

    #touchPic(Template(r"tpl1656145855589.png", record_pos=(-0.28, 0.173), resolution=(2560, 1440)),swtichMenuLag)
    
    orderTime = readScreen((653,672,843,730));
    print('剩余时间' + orderTime)
    sleepTime=get_sec(orderTime)-180
    print(sleepTime)
    #print(get_sec(sleepTime)-1200)
    
    touch(Template(r"tpl1656145874854.png", record_pos=(-0.086, 0.21), resolution=(2560, 1440)))
    touch(Template(r"tpl1656145895568.png", record_pos=(-0.013, -0.152), resolution=(2560, 1440)))
    touch(Template(r"tpl1656145908506.png", record_pos=(0.327, 0.097), resolution=(2560, 1440)))
    touchPic(Template(r"tpl1656145920163.png", record_pos=(0.421, 0.247), resolution=(2560, 1440)),swtichMenuLag)
    sleep(sleepTime)
sleep(7200)
while True:
    switchTrade()


# orderTime = readScreen((643,673,839,721));
# print('剩余时间' + orderTime)

# orderTime = readScreen((653,672,830,721));
# print('剩余时间' + orderTime)
# sleepTime=get_sec(orderTime)-1200
# print(sleepTime)

# image = cv2.imread('F:\Git\AIrtestFGOArknights/score.png')        
# gry = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# gry = cv2.dilate(gry, None, iterations=1)

# # OCR
# print(pytesseract.image_to_string(gry))
# data = pytesseract.image_to_string(gry, lang='eng',config='--psm 6')
# print(data)


# generate html reporte
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
