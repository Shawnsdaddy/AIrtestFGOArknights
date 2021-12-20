# -*- encoding=utf8 -*-
__author__ = "xubowu"

from airtest.core.api import *
import datetime

from airtest.core.settings import Settings as ST;
#设置图片识别pass为90%
ST.THRESHOLD = 0.8
auto_setup(__file__)
from poco.drivers.ios import iosPoco
        
poco = iosPoco()
roundConfig1 = {"skills": [(1, 0), (2, 3), (3, 3),(5, 3),(6, 3),(9, 0) ], "hoguNo": [3], "wave":1,"makeup":False}
roundConfig2 = {"skills": [(4, 0),(10, 3,3,""),], "hoguNo": [3], "wave":2,"makeup":False}
roundConfig3 = {"skills": [(10, 1,3,"") ], "hoguNo": [3], "wave":3,"makeup":False}
team1 = {"configuration":[roundConfig1,roundConfig2,roundConfig3],"description":"无限池票,伊阿宋单核"}

roundConfig4 = {"skills": [(1, 0), (2, 0),(3,0),(4,0),(5,0),(6,0),(9,0) ,(10, 3,2,"")], "hoguNo": [2], "wave":1,"makeup":False}
roundConfig5 = {"skills": [], "hoguNo": [1], "wave":2,"makeup":False}
roundConfig6 = {"skills": [(7, 0),(10, 1,3,"")], "hoguNo": [3], "wave":3,"makeup":False}
team2 = {"configuration":[roundConfig4,roundConfig5,roundConfig6],"description":"黄星碎片"}

roundConfig7 = {"skills": [(1, 0), (2, 3), (3, 3),(4, 0),(5,3),(6,3),(8,0)], "hoguNo": [3], "wave":1,"makeup":False}
roundConfig8 = {"skills": [], "hoguNo": [3], "wave":2,"makeup":False}
roundConfig9 = {"skills": [(10, 1,3,""),(9,0) ], "hoguNo": [3], "wave":3,"makeup":False}
team3 = {"configuration":[roundConfig7,roundConfig8,roundConfig9],"description":"刷废都巴比伦"}

roundConfig10 = {"skills": [(1, 0),(3, 0),(6,0)], "hoguNo": [1], "wave":1,"makeup":False}
roundConfig11 = {"skills": [], "hoguNo": [2], "wave":2,"makeup":False}
roundConfig12 = {"skills": [(5, 1,"enemy"),(4,0),(6,0),(9,5),(10, 2,3,"")], "hoguNo": [3], "wave":3,"makeup":False}
team4 = {"configuration":[roundConfig10,roundConfig11,roundConfig12],"description":"勾玉"}

roundConfig13 = {"skills": [(1, 0),(4, 0),(5,0),(7,0),(8,0)], "hoguNo": [2], "wave":1,"makeup":False}
roundConfig14 = {"skills": [(3,0)], "hoguNo": [1], "wave":2,"makeup":False}
roundConfig15 = {"skills": [(9,0),(10, 2,3,"")], "hoguNo": [3], "wave":3,"makeup":False}
team5 = {"configuration":[roundConfig13,roundConfig14,roundConfig15],"description":"箭头"}
        


#设置
config = team1["configuration"];
total = 1000;
count = 1;
#无限池Flag
unlimited = True;
#目前有几个单个的礼装 到 5 程序就停止
#假如礼装数量为4，刚从商店兑换完这个数应该设置成4，因为掉一个就可以平铺
#掉完一个后程序会停止，得手动更新这个数字，如果现在5礼装无满破，应该设置成0。即再刷5个就停止
rewardNum= 4;
autoLoadPoint = True;

def pickLastCard(position): 
    card1 = ((326,690),(560,950))
    card2 = ((740,690),(980,950))
    card3 = ((1154,690),(1380,950))
    card4 = ((1582,690),(1800,950))
    card5 = ((2010,690),(2250,950))
    lst = (card1,card2,card3,card4,card5)
    index = 0
    pick = False;
    while index<5 and pick == False :
        left = lst[index][0]
        right = lst[index][1]
        if True == (position[0] > left[0] and right[0]>position[0] and position[1]>left[1] and right[1]>position[1]):
            pick = True
            last = index+1
            if index ==4 :
                last = 0
            touch((((lst[last][0][0]+lst[last][1][0])/2,(lst[last][0][1]+lst[last][1][1])/2)))
        else:
            index +=1
def pickCard(count):
    if count == 0:
        touch ((1650,850))
        touch ((1250,850))
        return None;
    elif count ==-1:
        touch ((1650,850))
        touch ((1250,850))
        touch ((850,850))
        return None;

    
    bCard = exists(Template(r"tpl1625850478985.png", record_pos=(-0.22, 0.03), resolution=(2532, 1170)))




    if bCard !=False :
        touch(bCard)
        pickLastCard(bCard)
    else :

        ACard =exists(Template(r"tpl1625850534634.png", record_pos=(0.101, 0.034), resolution=(2532, 1170)))




        if ACard !=False :
            touch(ACard)
            pickLastCard(ACard)  
        else:
            QCard = exists(Template(r"tpl1625850503965.png", record_pos=(-0.008, 0.03), resolution=(2532, 1170)))





            if QCard !=False :
                touch(QCard)
                pickLastCard(QCard)  
            else:
                touch ((1650,850))
                touch ((1250,850))
def waitAttackButton():
    try:
        wait(Template(r"tpl1626568646598.png", record_pos=(0.321, 0.169), resolution=(2532, 1170)))
        return None;
    except TargetNotFoundError:
        if exists(Template(r"tpl1632089176760.png", record_pos=(0.001, -0.001), resolution=(2532, 1170))):
            touch((1600,900))
        waitAttackButton()
def castNoblePhantasm(order,wave,makeup=False):
    waitAttackButton()
    touch ((2063,993))
    sleep(secs=1.0)
    for servant in order:
        if servant==1 :
            touch((900,350))
        elif servant==2 :
            touch((1250,350))
        elif servant==3: 
            touch ((1650,350))
        else: 
            print('no order found')
    if makeup==True:
        pickCard(1)
    else :
        pickCard(0)
    sleep(8*len(order))
def castMasterSkill(order,target=0,name=""): 
    waitAttackButton()
    touch((2280,500))
    if order == 3: 
        touch((2100,500))
        if name == "changeOrder":
            touch((1750,600))
            touch((750,600))
            touch((1300,1000))
    elif order == 1:
        touch((1815,500))
    elif order == 2:
        touch((1960,500))
    if target == 3:
        touch ((1710,700)) 
    elif target ==1:
        touch((700,700))
    elif target ==2:
        touch((1250,700))
    sleep(1.5)
def castAbility(order,target,type="ally"):
    waitAttackButton()
    if type=="enemy":
        if target == 3:
            touch ((1000,75)) 
        elif target ==1:
            touch((200,75))
        elif target ==2:
            touch((600,75))
    if order == 1:
        touch((200,900))
    elif order == 2:
        touch((350,900))
    elif order == 3:
        touch((500,900))
    elif order == 4:
        touch((725,900))
    elif order == 5:
        touch((875,900))
    elif order == 6:
        touch((1025,900))
    elif order == 7:
        touch((1225,900))
    elif order == 8:
        touch((1375,900))
    elif order == 9:
        touch((1525,900))
    if type == "ally":
        if target == 3:
            touch ((1710,700)) 
        elif target ==1:
            touch((700,700))
        elif target ==2:
            touch((1250,700))
        # 卫宫 蓝卡
        elif target == 4:
            touch((1000,700))
        # 卫宫 红卡
        elif target == 5:
            touch((1500,700))
    sleep(1.5)
def catchMiss():
    try:
        wait(Template(r"tpl1631007534648.png", record_pos=(0.0, 0.183), resolution=(2532, 1170)))
        return None;
    except TargetNotFoundError:
        if exists(Template(r"tpl1632089176760.png", record_pos=(0.001, -0.001), resolution=(2532, 1170))):
            touch((1600,900))
            catchMiss()
        addackExists = exists(Template(r"tpl1626568646598.png", record_pos=(0.321, 0.169), resolution=(2532, 1170)))
        if(addackExists !=False):
            touch ((2063,993))
            sleep(secs=0.5)
            pickCard(-1)
            waitAttackButton()
            catchMiss()
        else :
            catchMiss()
def doOneBattle(config):
    skills = config["skills"]
    for skill in skills:
        if skill[0]==10:
            castMasterSkill(skill[1],skill[2],skill[3])
        elif len(skill)==3:
            castAbility(skill[0],skill[1],skill[2])
        else: 
            castAbility(skill[0],skill[1])
    castNoblePhantasm(config["hoguNo"],config["wave"],config["makeup"])
    if(config["wave"]==3):
        catchMiss()
def battleStart():
    wait(Template(r"tpl1625708685398.png", record_pos=(0.321, -0.204), resolution=(2532, 1170)))
    # CBA
    #support = exists(Template(r"tpl1625594007027.png", record_pos=(-0.1, -0.077), resolution=(2532, 1170)))
    # 术傻
    support = exists(Template(r"tpl1628233851456.png", record_pos=(0.004, -0.019), resolution=(2532, 1170)))
    failCount = 0
    
    while support == False: 
        if failCount >3 :
            touch((1550,226))
            wait(Template(r"tpl1632155301033.png", record_pos=(0.127, 0.131), resolution=(2532, 1170)))
            touch((1600,900))
            failCount = 0;
            continue
        if exists(Template(r"tpl1632089176760.png", record_pos=(0.001, -0.001), resolution=(2532, 1170))):
            touch((1600,900))
            continue;
        swipe((1170,1000), (1150,400))
        failCount+=1
        support = exists(Template(r"tpl1628233851456.png", record_pos=(0.004, -0.019), resolution=(2532, 1170)))
    touch(support)
    if count ==1:
        sleep(3)
        go = exists(Template(r"tpl1625642480951.png", record_pos=(0.353, 0.203), resolution=(2532, 1170)))
        if go !=False :
            touch(go)
    waitAttackButton()
def battleFinish():
    global count
    global rewardNum
    global unlimited
    touch((1300,500))
    wait(Template(r"tpl1631007534648.png", record_pos=(0.0, 0.183), resolution=(2532, 1170)))    
    touch((1300,500))
    wait(Template(r"tpl1625707970096.png", record_pos=(0.301, 0.204), resolution=(2532, 1170)))
    if unlimited :
        
        if (exists(Template(r"tpl1639988921163.png", record_pos=(-0.016, -0.018), resolution=(2532, 1170)))!=False):
            rewardNum+=1
            if rewardNum >=5:  
                count +=100000
            print(rewardNum)
            print(datetime.datetime.now())
    touch((2100,1100))
    wait(Template(r"tpl1625707993376.png", record_pos=(0.128, 0.133), resolution=(2532, 1170)))
    touch((1600,930))
    notEnough=exists(Template(r"tpl1625643337618.png", record_pos=(0.006, -0.188), resolution=(2532, 1170)))
    if notEnough!= False:
        if autoLoadPoint==True:
            #银
            touch((1300,800))
            #金
            #touch((1300,500))
            #石头
            #touch((1300,350))
            #铜
            #swipe((1300,800), (1300,500))
            #touch((1300,850))
            
            wait(Template(r"tpl1632165648098.png", record_pos=(0.128, 0.13), resolution=(2532, 1170)))
            touch((1600,900))
        else :
            touch((1250,1000))
            count+=10000
def FGOStart(config):
    global count
    while count <= total:
        battleStart();
        doOneBattle(config[0])
        doOneBattle(config[1])
        doOneBattle(config[2])
        battleFinish();
        count += 1
#点任意两下
FGOStart(config)


