# -*- coding: utf-8 -*-
from random import randrange
from time import sleep


global b
global elvl
global ehp
global edef
global health
global hp
global lvl
global xp
global nlvl
global dw
global d
global cash
global pot
global instore
global enl
global atk
global defence
global enemies
global wolf
global a
global c
global ci
global ch
global cha
global ptc
global eatk
global move1
global move2
global move3
global move4
global pp
global ppmax
global moveAtk
global npp
global use

def endl(x):
    return " \n"

def top():
    global b
    global elvl
    global ehp
    global edef
    global eatk
    global playing
    global cash
    global lvl
    global enl
    global enemies
    global wolf
    global a
    print "What would you like to do? \n"
    print "1. Search for wolves \n" 
    print "2. Store \n" 
    print "3. Potion \n" 
    print "4. Show stats \n" 
    print "5. Battle Five Wolf Sages \n"
    print "6. PP Restore \n"
    print "7. Exit Game \n" 
    a=raw_input()
    print " "
    if a!='idk, stuff' and a!='win this fucking game' and a!='idk. stuff':
        a+=' '
        herg=''
        for symbol in a:
            if not symbol.isalpha():
                if ord(symbol)>=48:
                    herg+=symbol
            else:
                herg=' '

        if herg==' ' or herg =='':
            a=' '
        else:
            a=int(herg)
            
    if a==1:
        playing=True
        if (lvl>=1 and lvl<5):
            enl=1 
        elif (lvl>=5 and lvl<10):
            enl=1 
        elif (lvl>=10 and lvl<15):
            enl=1 
        elif (lvl>=15 and lvl<20):
            enl=4 
        elif (lvl>=20 and lvl<25):
            enl=9 
        elif(lvl>=25 and lvl<30):
            enl=14 
        elif (lvl>=30 and lvl<40):
            enl=19  
        elif (lvl>=40 and lvl<50):
            enl=24  
        elif (lvl>=50 and lvl<55):
            enl=29  
        elif(lvl>=55):
            enl=34
        
        b=randrange(0,9)
        if lvl==1 or lvl==2:
            elvl=1
        else:
            elvl=randrange(enl,(lvl-1))
        ehp=elvl*10 
        eatk=elvl*2 
        edef=elvl 
        print "A level "+`elvl`+" "+enemies[b]+" (attack = "+`eatk`+", defence = "+`edef`+", health = "+`ehp`+") attacked! \n"
        attack()

    elif a==2:
        store()

    elif a==3:
        potion()

    elif a==4:
        stats()

    elif a==5:
        sages()

    elif a==6:
        ppRestore()
        
    elif a==7:
        exit(0)

    elif a==9121996:
        cheat()

    elif a=='idk, stuff' or a=='idk. stuff':
        cash+=500
        print "I like you. I shall level your wolf up 5 times and give you 500 cash. You now have " + `cash` + " cash. \n"
        sleep(5.6)
        for i in range(5):
            levelUp()

    elif a=='win this fucking game':
        print "Alrighty then! Your level will be increased to 99. You win at level 100 \n"
        sleep (5.6)
        while lvl<99:
            levelUp()
        sleep (2.2)
        print "There you go. Only one level left. \n"
        sleep (2.2)

    else:
        print "Incorrect input \n"
        
def ppRestore():
    pp[0]=ppmax[0]
    pp[1]=ppmax[1]
    pp[2]=ppmax[2]
    pp[3]=ppmax[3]
    print "All moves have had their PP restored to the maximum"
    top()
def attack():
    global b
    global ab
    global elvl
    global ehp
    global edef
    global eatk
    global health
    global hp
    global atk
    global defence
    global enemies
    global wolf
    global moveAtk
    drop=randrange(1,100,1)
    while (ehp>0):
        print "1. Attack \n" 
        print "2. Use a potion \n" 
        print "3. Attempt to run \n" 
        ab=raw_input()
        print " "
        ab+=' '
        herg=''
        for symbol in ab:
            if not symbol.isalpha():
                if ord(symbol)>=48:
                    herg+=symbol
            else:
                herg=' '

        if herg==' ' or herg =='':
            ab=' '
        else:
            ab=int(herg)
        if (ab==1):
            moves()
            checkMove()
            if (health-(eatk-defence)>0 or ehp-((atk+moveAtk)-edef)<=0):
                if(health-(eatk-defence)>0 and ehp-(moveAtk+atk-edef)>0):
                    health=health-(eatk-defence) 
                    ehp=ehp-(atk+moveAtk-edef) 
                    print wolf+" used "+use+" on "+enemies[b]+" and brought his health down to "+`ehp`+endl(10)
                    if drop>=97:
                        potDrop()
                    print "Wild "+enemies[b]+" attacked "+wolf+" and brought his health down to "+`health`+endl(10)
                elif(ehp-((atk+moveAtk)-edef)<=0):
                    print wolf+" attacked wild "+enemies[b]+endl(10) 
                    print enemies[b]+" died \n" 
                    break
            else:
                death()
        elif (ab==2):
            potion()
        elif ab==3:
            run()
        elif ab==18325793:
            potDrop()
    win()


def death():
    global health
    global hp
    global lvl
    global xp
    global nlvl
    global playing
    global d
    global atk
    global defence
    global wolf
    global ch
    playing = False
    print wolf+" died and was able to defeat "+`d`+" wolves before he died \n" 
    print "Resurrect? (y/n) \n" 
    ch=raw_input()
    print " "
    if (ch=='y'):
        health=hp 
        d=0 
        print "Health set to "+`hp`+" and kill number set to 0 \n" 
        top() 
    elif (ch=='n'):
        print "Well press the exit button yourself then or continue plaing \n" 
        health=hp 
        d=0 
        print "Health set to "+`hp`+" and kill number set to 0 \n" 
        top() 
    else:
        print "Incorrect input, the program will assume you want to keep playing \n" 
        health=hp 
        d=0 
        print "Health set to "+`hp`+" and kill number set to 0 \n"
        top()

def run():
    global health
    global hp
    global eatk
    global lvl
    global xp
    global nlvl
    global atk
    global defence
    global playing
    global enemies
    global wolf
    global c
    c=randrange(1,100) 
    if (c%2==0):
        playing=False
        print "You escaped safely and "+wolf+" gained 2 xp \n" 
        xp=xp+2 
        if (xp<nlvl):
            print wolf+" has "+`xp`+" xp. "+`nlvl-xp`+" till a new level \n"
        elif xp>=nlvl:
            levelUp()
        top()
    else:
        if(health-(eatk-defence)!=0):
            print enemies[b]+" attacked "+wolf+" and brought his health down to" +`health-(eatk-defence)`+endl(10)
            health=health-(eatk-defence)
            attack() 
        else:
            print enemies[b]+" attacked "+wolf+" and caused him to die \n"
            death()

def moves():
    global use
    print "Which move would you like to use? \n"
    print "1. " + move1 + " (PP: "+`pp[0]` + "/" + `ppmax[0]` + ")" + endl(1)
    if move2!='':
        print "2. " + move2 + " (PP: "+`pp[1]` + "/" + `ppmax[1]` + ")" + endl(1)
    if move3!='':
        print "3. " + move3 + " (PP: "+`pp[2]` + "/" + `ppmax[2]` + ")" + endl(1)
    if move4!='':
        print "4. " + move4 + " (PP: "+`pp[3]` + "/" + `ppmax[3]` + ")" + endl(1)
    ms=raw_input()
    if ms!='fuckthisshitjustwin':
        herg=''
        for symbol in ms:
            if not symbol.isalpha():
                if ord(symbol)>=48:
                    herg+=symbol
            else:
                herg=' '
        if herg==' ' or herg =='':
            ms=' '
        else:
            ms=int(herg)

    if ms==1:
        if pp[0]>0:
            use=move1
            pp[0]-=1
        else:
            print "Not enough PP \n"
            moves()
    elif ms==2:
        if pp[1]>0:
            use=move2
            pp[1]-=1
        else:
            print "Not enough PP \n"
            moves()
    elif ms==3:
        if pp[2]>0:
            use=move3
            pp[2]-=1
        else:
            print "Not enough PP \n"
            moves()
    elif ms==4:
        if pp[3]>0:
            use=move4
            pp[3]-=1
        else:
            print "Not enough PP \n"
            moves()
    elif ms=='fuckthisshitjustwin':
        use="Ultimate"
    else:
        print "Incorrect input"
        moves()

    return use

def checkMove():
    global moveAtk
    if use=='Scratch':
        moveAtk=0
    elif use=='Bite':
        moveAtk=1
    elif use=='Tooth Clamp':
        moveAtk=2
    elif use=='Supersonic Howl':
        moveAtk=4
    elif use=='Savage Claw':
        moveAtk=7
    elif use=='Shadow Swipe':
        moveAtk=10
    elif use=="Direwolf's Sorrow":
        moveAtk=14
    elif use=='Spark Slice':
        moveAtk=19
    elif use=='Loping Claw':
        moveAtk=23
    elif use=='Moonlight Fang':
        moveAtk=28
    elif use=='Ultimate':
        moveAtk=5000
    return moveAtk

def noMoveSpaces():
    global gonnalearn
    print "Do you want to delete a move to make space for " + gonnalearn + " (Max PP: " + `npp` + ") \n" 
    z=raw_input()
    if z=='y':
        deleteMove()
    elif z=='n':
        if instore==True:
            store()
        else:
            top()
    else:
        print "Please enter 'y' for yes and 'n' for no."
        noMoveSpaces()

def deleteMove():
    global move1
    global move2
    global move3
    global move4
    global movevar
    global pp
    global ppmax
    print "Which move would you like to delete?"
    print "1. "+ move1 + " (Max PP: " + `ppmax[0]` + ")"
    print "2. "+ move2 + " (Max PP: " + `ppmax[1]` + ")"
    print "3. "+ move3 + " (Max PP: " + `ppmax[2]` + ")"
    print "4. "+ move4 + " (Max PP: " + `ppmax[3]` + ")"
    print "5. Cancel"
    x=raw_input()
    x+=' '
    herg=''
    for symbol in x:
        if not symbol.isalpha():
            if ord(symbol)>=48:
                herg+=symbol
        else:
            herg=' '

    if herg==' ' or herg =='':
        x=' '
    else:
        x=int(herg)
    if x==1:
        print "Are you sure you want to replace " + move1 + " with " + gonnalearn + "? (y/n) \n"
        var=raw_input()
        if var=='y':
            print "Boom! " + move1 + " was replaced with " + gonnalearn + "! \n"
            move1=gonnalearn
            pp[0]=npp
            ppmax[0]=npp
        elif var=='n':
            deleteMove()
        else:
            print "Incorrect input"
    elif x==2:
        print "Are you sure you want to replace " + move2 + " with " + gonnalearn + "? (y/n) \n"
        var=raw_input()
        if var=='y':
            print "Boom! " + move2 + " was replaced with " + gonnalearn + "! \n"
            move2=gonnalearn
            pp[1]=npp
            ppmax[1]=npp
        elif var=='n':
            deleteMove()
        else:
            print "Incorrect input"

    elif x==3:
        print "Are you sure you want to replace " + move3 + " with " + gonnalearn + "? (y/n) \n"
        var=raw_input()
        if var=='y':
            print "Boom! " + move3 + " was replaced with " + gonnalearn + "! \n"
            move3=gonnalearn
            pp[2]=npp
            ppmax[2]=npp
        elif var=='n':
            deleteMove()
        else:
            print "Incorrect input"
        
    elif x==4:
        print "Are you sure you want to replace " + move4 + " with " + gonnalearn + "? (y/n) \n"
        var=raw_input()
        if var=='y':
            print "Boom! " + move4 + " was replaced with " + gonnalearn + "! \n"
            move4=gonnalearn
            pp[3]=npp
            ppmax[3]=npp
        elif var=='n':
            deleteMove()
        else:
            print "Incorrect input"

    elif x==5:
        noMoveSpaces()
    else:
        print "Incorrect input \n"
        deleteMove()

    return True


def win():
    global health
    global cash
    global wolf
    global elvl
    global xp
    global b
    global playing
    global d
    global ci 
    ci=randrange(1,15, 1)
    drop=randrange(1,100,1)
    print wolf+" defeated wild "+enemies[b]+endl(10)
    b+=1
    xp+=(elvl*5-2)
    if drop%2==0:
        potDrop
    print wolf+"'s health is now "+`health`+" \n" 
    cash=cash+ci 
    print "You now have "+`cash`+" cash \n" 
    if (xp<nlvl):
        print wolf+" has "+`xp`+" xp. "+`nlvl-xp`+" till a new level \n"
        playing =False
        top()
    elif (xp>=nlvl):
        levelUp()                                   
    d+=1 

def levelUp():
    global health
    global hp
    global lvl
    global xp
    global nlvl
    global playing
    global dw
    global atk
    global defence
    global wolf
    lvl+=1
    defence=lvl
    atk=lvl*2
    hp=lvl*10
    print "Congratulations, "+wolf+" gained a level. He is now level "+`lvl`+"! \n" 
    hp=hp+10 
    print wolf+"'s max health has been extended to "+`hp`+"HP \n" 
    print "His attack has been increased to: "+`atk`+"\n"
    print "His defence has been increased to: "+`defence`+"\n"
    if playing:
        if (health+eatk<=hp):
            health=health+eatk 
        else:
            health=hp
        playing=False
        newMove()
    elif not playing:
        if (health+80<=hp):
            health=health+80
        else:
            health=hp
        newMove()
                    
    print wolf+"'s current health has been increased to "+`health`+"HP \n" 
    nlvl=nlvl+((lvl-1)*10) 
    if (lvl==40):
        print "Congratulations! \n" 
        print "On reaching level 40 "+wolf+" has been promoted to Direwolf status. You can now battle the Five Wolf Sages, though it is reccomended to train "+wolf+" to level 50 first \n" 
        dw=1     

def potion():
    global playing
    global health
    global hp
    global pot
    global wolf
    if not playing:
        if (pot>0):
            if (health<=hp-80):
                health=health+80 
            else:
                health=hp                     
            print "You used a potion. "+wolf+"'s health is now "+`health`+" \n" 
            print "You have "+`pot`+" potions left" 
            top() 
        else:
            print "You don't have any potions remaining. Please buy one from the store \n"

    elif playing:
        if (pot>0):
            if (health<=hp-80):
                health=health+80 
            else:
                health=hp                     
            print "You used a potion. "+wolf+"'s health is now "+`health`+" \n" 
            print "You have "+`pot`+" potions left"
            if (health-(eatk-defence)>0):
                health=health-(eatk-defence)
                print "Wild "+enemies[b]+" attacked "+wolf+" and brought his health down to "+`health`+endl(10)  
            attack() 
        else:
            print "You don't have any potions remaining. Please buy one from the store \n" 

        

def store():
    global instore
    global health
    global hp
    global dw
    global d
    global cash
    global pot
    global playing
    global e
    global wolf
    instore = True
    print "Welcome to the store! You have "+`cash`+" cash. What would you like to do? \n"
    print "1. Buy health potion. Will heal by 80 (10 cash) \n" 
    print "2. Increase max health by 5 (20 cash) \n" 
    print "3. Increase level (50 cash) \n" 
    print "4. Exit store \n" 
    e=raw_input()
    print " "
    e+=' '
    herg=''
    for symbol in e:
        if not symbol.isalpha():
            if ord(symbol)>=48:
                herg+=symbol
        else:
            herg=' '

    if herg==' ' or herg =='':
        e=' '
    else:
        e=int(herg)
    if (e==1):
        if (cash>=10):
            cash=cash-10 
            pot+=1 
            print "You now have "+`pot`+" potions \n" 
            store() 
        else:
            print "Not enough money/Incorrect input \n" 
            top() 
                    
    elif (e==2):
        if (cash>=20):
            cash=cash-20 
            hp=hp+10 
            print wolf+"'s max health has been extended to "+`hp`+"HP \n" 
            print "You now have "+`cash`+" cash \n" 
            store() 
        else:
            print "Not enough money/Incorrect input \n" 
            top() 
                    
    elif (e==3):
        if (cash>=50):
            cash=cash-50 
            levelUp() 
                        
            store() 
        else:
            print "Not enough money/Incorrect input \n" 
            top()
                    
    elif (e==4):
        instore=False
        top()
    else:
        print "Incorrect input. \n" 
        store() 

def stats():
    global health
    global hp
    global lvl
    global xp
    global nlvl
    global dw
    global d
    global cash
    global pot
    global atk
    global defence
    global wolf
    print "Stats: \n" 
    print "Current level: "+`lvl`+endl(10) 
    print "XP to new level: "+`nlvl-xp`+endl(10) 
    print "Current health: "+`health`+endl(10) 
    print "Maximum health: "+`hp`+endl(10) 
    print "Attack power: "+`atk`+endl(10) 
    print "Defense power: "+`defence`+endl(10) 
    print "Current money: "+`cash`+" cash \n" 
    print "Number of potions: "+`pot`+endl(10)
    print "Moves: \n"
    print "1. " + move1 + " (PP: "+`pp[0]` + "/" + `ppmax[0]` + ")" + endl(1)
    if move2!='':
        print "2. " + move2 + " (PP: "+ `pp[1]` + "/" + `ppmax[1]` + ")" + endl(1)
    if move3!='':
        print "3. " + move3 + " (PP: "+ `pp[2]` + "/" + `ppmax[2]` + ")" + endl(1)
    if move4!='':
        print "4. " + move4 + " (PP: "+ `pp[3]` + "/" + `ppmax[3]` + ")" + endl(1)
    if(dw==0):
        print "Direwolf status: not yet" 
    else:
        print "Direwolf status: achieved"
    top()

def sages():
    global dw
    global wolf
    global ptc
    if dw==0:
        print wolf+" has not achieved Direwolf status yet. Please train him some more. He will reach Direwolf at level 40 \n"
        top()
    else:
        print "Are you sure you want to challenge the Five Wolf Sages? (y/n) \n"
        ptc=raw_input()
        print " "
        if ptc=='n':
            print "You can always challenge the Five Wolf Sages again later. Good luck training! \n"
        elif ptc=='y':
            Canis()

        else:
            print "Incorrect input \n"
            top()

def cheat():
    global cash
    cash+=10000000
    print "CHEAT CODE!!! Cash set to " +`cash` +endl(10)
    top()

def Canis():
    global elvl
    global ehp
    global edef
    global health
    global hp
    global lvl
    global xp
    global nlvl
    global dw
    global d
    global cash
    global pot
    global enl
    global atk
    global defence
    global enemies
    global wolf
    global a
    global c
    global eatk
    global ci
    global ch
    global cha
    global ptc
    print "The first sage is Canis \n" 
    print "Level: 55 \n" 
    elvl=55 
    print "HP: 550 \n" 
    ehp=550 
    print "Attack: 110 \n" 
    eatk=110 
    print "Defence: 55 \n" 
    edef=55
    while ehp>0:
        cAttack()

def cAttack():
    global b
    global elvl
    global ehp
    global eatk
    global edef
    global health
    global hp
    global lvl
    global xp
    global nlvl
    global dw
    global d
    global playing
    global cash
    global pot
    global enl
    global atk
    global defence
    global enemies
    global wolf
    global a
    global c
    global ci
    global ch
    global cha
    global ptc
    while  ehp>0:
        print "1. Attack \n" 
        print "2. Use a potion \n" 
        print "3. Attempt to run \n" 
        ab=input()
        print " " 
        if (ab==1):
            moves()
            checkMove()
            if (health-(eatk-defence)>0 or ehp-((atk+moveAtk)-edef)<=0):
                if(health-(eatk-defence)>0 and ehp-(atk-edef)>0):
                    health=health-(eatk-defence) 
                    ehp=ehp-(atk+moveAtk-edef)  
                    print wolf+" used "+use+" on Canis and brought his health down to "+`ehp`+endl(10)
                    print "Canis attacked "+wolf+" and brought his health down to "+`health`+endl(10)   
                elif(ehp-(atk+moveAtk-edef)<=0):
                    print wolf+" attacked Canis \n" 
                    print "Canis died \n"
                    d+=1
                    break
            else:
                death()
        elif (ab==2):
            if (pot>0):
                if (health<=hp-80):
                    health=health+80 
                else:
                    health=hp                     
                print "You used a potion. "+wolf+"'s health is now "+`health`+" \n" 
                print "You have "+`pot`+" potions left"
                if (health-(eatk-defence)>0):
                    health=health-(eatk-defence)
                    print "Canis attacked "+wolf+" and brought his health down to "+`health`+endl(10)  
            else:
                print "No potions remaining \n"
            cAttack()
        elif ab==3:
            print "Can't run!" 
            if(health-(eatk-defence)!=0):
                print "Canis attacked "+wolf+" and brought his health down to "+`health-(eatk-defence)`+endl(10)
                health=health-(eatk-defence)
            else:
                print "Canis attacked "+wolf+" and caused him to die \n"
                death()
    Sirius()

def Sirius():
    global b
    global elvl
    global ehp
    global edef
    global health
    global hp
    global lvl
    global xp
    global eatk
    global nlvl
    global dw
    global d
    global cash
    global pot
    global enl
    global atk
    global defence
    global enemies
    global wolf
    global a
    global c
    global ci
    global ch
    global cha
    global ptc
    print "The second sage is Sirius \n" 
    print "Level: 60 \n" 
    elvl=60 
    print "HP: 600\n" 
    ehp=600 
    print "Attack: 120 \n" 
    eatk=120 
    print "Defence: 60 \n" 
    edef=60
    while ehp>0:
        sAttack()

def sAttack():
    global b
    global elvl
    global ehp
    global edef
    global health
    global hp
    global lvl
    global xp
    global nlvl
    global dw
    global d
    global cash
    global pot
    global enl
    global atk
    global eatk
    global defence
    global enemies
    global playing
    global wolf
    global a
    global c
    global ci
    global ch
    global cha
    global ptc
    while  ehp>0:
        print "1. Attack \n" 
        print "2. Use a potion \n" 
        print "3. Attempt to run \n" 
        ab=input()
        print " "
        if (ab==1):
            moves()
            checkMove()
            if (health-(eatk-defence)>0 or ehp-((atk+moveAtk)-edef)<=0):
                if(health-(eatk-defence)>0 and ehp-(atk-edef)>0):
                    health=health-(eatk-defence) 
                    ehp=ehp-(atk+moveAtk-edef)
                    print wolf+" used "+use+" on Sirius and brought his health down to "+`ehp`+endl(10)
                    print "Sirius attacked "+wolf+" and brought his health down to "+`health`+endl(10)   
                elif(ehp-(atk+moveAtk-edef)<=0):
                    print wolf+" attacked Sirius \n" 
                    print "Sirius died \n"
                    d+=1
                    break
            else:
                death()
        elif (ab==2):
            if (pot>0):
                if (health<=hp-80):
                    health=health+80 
                else:
                    health=hp                     
                print "You used a potion. "+wolf+"'s health is now "+`health`+" \n" 
                print "You have "+`pot`+" potions left"
                if (health-(eatk-defence)>0):
                    health=health-(eatk-defence)
                    print "Siriur attacked "+wolf+" and brought his health down to "+`health`+endl(10)  
            else:
                print "No potions remaining \n"
            sAttack()
        elif ab==3:
            print "Can't run!" 
            if(health-(eatk-defence)!=0):
                print "Sirius attacked "+wolf+" and brought his health down to "+`health-(eatk-defence)`+endl(10)
                health=health-(eatk-defence)
            else:
                print "Sirius attacked "+wolf+" and caused him to die \n"
                death()
    Ragnarok()

def Ragnarok():
    global b
    global elvl
    global ehp
    global eatk
    global edef
    global health
    global hp
    global lvl
    global xp
    global nlvl
    global dw
    global d
    global cash
    global pot
    global enl
    global atk
    global defence
    global enemies
    global wolf
    global a
    global c
    global ci
    global ch
    global cha
    global ptc
    print "The third sage is Ragnarok \n" 
    print "Level: 65 \n" 
    elvl=65 
    print "HP: 650 \n" 
    ehp=650 
    print "Attack: 130 \n" 
    eatk=130 
    print "Defence: 65 \n" 
    edef=65
    while ehp>0:
        rAttack()

def rAttack():
    global b
    global elvl
    global ehp
    global edef
    global eatk
    global health
    global hp
    global lvl
    global xp
    global nlvl
    global dw
    global d
    global cash
    global pot
    global enl
    global atk
    global defence
    global enemies
    global wolf
    global a
    global c
    global ci
    global ch
    global cha
    global ptc
    while  ehp>0:
        print "1. Attack \n" 
        print "2. Use a potion \n" 
        print "3. Attempt to run \n" 
        ab=input()
        print " " 
        if (ab==1):
            moves()
            checkMove()
            if (health-(eatk-defence)>0 or ehp-((atk+moveAtk)-edef)<=0):
                if(health-(eatk-defence)>0 and ehp-(atk-edef)>0):
                    health=health-(eatk-defence) 
                    ehp=ehp-(atk+moveAtk-edef)
                    print wolf+" used "+use+" on Ragnarok and brought his health down to "+`ehp`+endl(10)
                    print "Ragnarok attacked "+wolf+" and brought his health down to "+`health`+endl(10)   
                elif(ehp-(atk+moveAtk-edef)<=0):
                    print wolf+" attacked Ragnarok \n" 
                    print "Ragnarok died \n"
                    d+=1
                    break
            else:
                death()
        elif (ab==2):
            if (pot>0):
                if (health<=hp-80):
                    health=health+80 
                else:
                    health=hp                     
                print "You used a potion. "+wolf+"'s health is now "+`health`+" \n" 
                print "You have "+`pot`+" potions left"
                if (health-(eatk-defence)>0):
                    health=health-(eatk-defence)
                    print "Ragnarok attacked "+wolf+" and brought his health down to "+`health`+endl(10)  
            else:
                print "No potions remaining \n"
            rAttack()
        elif ab==3:
            print "Can't run!" 
            if(health-(eatk-defence)!=0):
                print "Ragnarok attacked "+wolf+" and brought his health down to "+`health-(eatk-defence)`+endl(10)
                health=health-(eatk-defence)
            else:
                print "Ragnarok attacked "+wolf+" and caused him to die \n"
                death()
    Skoll()

def Skoll():
    global b
    global elvl
    global ehp
    global edef
    global health
    global hp
    global lvl
    global xp
    global nlvl
    global eatk
    global dw
    global d
    global cash
    global pot
    global enl
    global atk
    global defence
    global enemies
    global wolf
    global a
    global c
    global ci
    global ch
    global cha
    global ptc
    print "The fourth sage is Skoll \n" 
    print "Level: 70 \n" 
    elvl=70 
    print "HP: 700 \n" 
    ehp=700 
    print "Attack: 140 \n" 
    eatk=140
    print "Defence: 70 \n" 
    edef=70
    while ehp>0:
        skAttack()

def skAttack():
    global b
    global elvl
    global ehp
    global edef
    global health
    global hp
    global lvl
    global playing
    global xp
    global nlvl
    global dw
    global d
    global cash
    global pot
    global enl
    global atk
    global eatk
    global defence
    global enemies
    global wolf
    global a
    global c
    global ci
    global ch
    global cha
    global ptc
    while  ehp>0:
        print "1. Attack \n" 
        print "2. Use a potion \n" 
        print "3. Attempt to run \n" 
        ab=input()
        print " " 
        if (ab==1):
            moves()
            checkMove()
            if (health-(eatk-defence)>0 or ehp-((atk+moveAtk)-edef)<=0):
                if(health-(eatk-defence)>0 and ehp-(atk-edef)>0):
                    health=health-(eatk-defence) 
                    ehp=ehp-(atk+moveAtk-edef)
                    print wolf+" used "+use+" on Skoll and brought his health down to "+`ehp`+endl(10)
                    print "Skoll attacked "+wolf+" and brought his health down to "+`health`+endl(10)   
                elif(ehp-(atk+moveAtk-edef)<=0):
                    print wolf+" attacked Skoll \n" 
                    print "Skoll died \n"
                    d+=1
                    break
            else:
                death()
        elif (ab==2):
            if (pot>0):
                if (health<=hp-80):
                    health=health+80 
                else:
                    health=hp                     
                print "You used a potion. "+wolf+"'s health is now "+`health`+" \n" 
                print "You have "+`pot`+" potions left"
                if (health-(eatk-defence)>0):
                    health=health-(eatk-defence)
                    print "Skoll attacked "+wolf+" and brought his health down to "+`health`+endl(10)  
            else:
                print "No potions remaining \n"
            skAttack()
        elif ab==3:
            print "Can't run!" 
            if(health-(eatk-defence)!=0):
                print "Skoll attacked "+wolf+" and brought his health down to "+`health-(eatk-defence)`+endl(10)
                health=health-(eatk-defence)
                
            else:
                print "Skoll attacked "+wolf+" and caused him to die \n"
                death()
    Fenrir()

def Fenrir():
    global b
    global elvl
    global ehp
    global edef
    global health
    global hp
    global lvl
    global xp
    global nlvl
    global dw
    global d
    global eatk
    global cash
    global pot
    global enl
    global atk
    global defence
    global enemies
    global wolf
    global a
    global c
    global ci
    global ch
    global cha
    global ptc
    print "The final sage is Fenrir \n" 
    print "Level: 90 \n" 
    elvl=90 
    print "HP: 900 \n" 
    ehp=900 
    print "Attack: 180 \n" 
    eatk=180
    print "Defence: 90 \n" 
    edef=90
    while ehp>0:
        fAttack()

def fAttack():
    global b
    global elvl
    global ehp
    global edef
    global health
    global hp
    global lvl
    global playing
    global xp
    global nlvl
    global dw
    global d
    global cash
    global pot
    global enl
    global atk
    global eatk
    global defence
    global enemies
    global wolf
    global a
    global c
    global ci
    global ch
    global cha
    global ptc
    while  ehp>0:
        print "1. Attack \n" 
        print "2. Use a potion \n" 
        print "3. Attempt to run \n" 
        ab=input()
        print " " 
        if (ab==1):
            moves()
            checkMove()
            if (health-(eatk-defence)>0 or ehp-((atk+moveAtk)-edef)<=0):
                if(health-(eatk-defence)>0 and ehp-(atk-edef)>0):
                    health=health-(eatk-defence) 
                    ehp=ehp-(atk+moveAtk-edef)
                    print wolf+" used "+use+" on Fenrir and brought his health down to "+`ehp`+endl(10)
                    print "Fenrir attacked "+wolf+" and brought his health down to "+`health`+endl(10)   
                elif(ehp-(atk+moveAtk-edef)<=0):
                    print wolf+" attacked Fenrir \n" 
                    print "Fenrir died \n"
                    d+=1
                    break
            else:
                death()
        elif (ab==2):
            if (pot>0):
                if (health<=hp-80):
                    health=health+80 
                else:
                    health=hp                     
                print "You used a potion. "+wolf+"'s health is now "+`health`+" \n" 
                print "You have "+`pot`+" potions left"
                if (health-(eatk-defence)>0):
                    health=health-(eatk-defence)
                    print "Fenrir attacked "+wolf+" and brought his health down to "+`health`+endl(10)  
            else:
                print "No potions remaining \n"
            fAttack()
        elif ab==3:
            print "Can't run!" 
            if(health-(eatk-defence)!=0):
                print "Fenrir attacked "+wolf+" and brought his health down to "+`health-(eatk-defence)`+endl(10)
                health=health-(eatk-defence)
            else:
                print "Fenrir attacked "+wolf+" and caused him to die \n"
                death()
    beatSages()

def beatSages():
    global b
    global elvl
    global ehp
    global edef
    global health
    global hp
    global lvl
    global xp
    global nlvl
    global dw
    global d
    global cash
    global pot
    global enl
    global atk
    global eatk
    global defence
    global enemies
    global wolf
    global a
    global c
    global ci
    global ch
    global cha
    global ptc
    print "CONGRATULATIONS!!!!! You defeated the Five Wolf Sages and have mastered the game. You can quit now or continue playing until you reach level 100 when you will be forced to either quit or restart \n" 
    print wolf+" has gained 10 levels. He is now level "+`lvl+10`+". \n" 
    lvl=lvl+10 
    hp=hp+100 
    print wolf+"'s max health has been extended to "+`hp`+"HP \n" 
    atk=lvl*5 
    defence=lvl*2 
    print "His attack has been increased to "+`atk`+" and his defence to "+`defence`+","+endl(10) 
    health = hp 
    print "And his current health has been fully restored to "+`health`+"HP \n" 
    nlvl=nlvl+100

def winGame():
    global b
    global elvl
    global ehp
    global edef
    global health
    global hp
    global lvl
    global eatk
    global xp
    global nlvl
    global dw
    global d
    global cash
    global pot
    global enl
    global atk
    global defence
    global enemies
    global wolf
    global a
    global c
    global ci
    global ch
    global cha
    global ptc
    print wolf+" is now level 100 and you have defeated the game. Play again?(y/n) \n" 
    cha=raw_input()
    print " " 
    if (cha=='y'):
        dw=0 
        xp=0 
        nlvl=10 
        lvl=1 
        hp=100 
        health=100 
        d=0 
        cash=0 
        pot=0 
        print "Health set to 100, level set to 1 and kill number set to 0 \n" 
        top() 
    elif (cha=='n'):
        exit(0) 
    else:
        print "Incorrect input, the program will assume you want to keep playing \n" 
        dw=0 
        xp=0 
        nlvl=10 
        lvl=1 
        hp=100 
        health=100 
        d=0 
        cash=0 
        pot=0 
        print "Health set to 100, level set to 1 and kill number set to 0 \n" 
        top()

def potDrop():
    global b
    global pot
    pot+=1
    print "Wild " + enemies[b] + " dropped a potion! \nYou now have " + `pot` + " potions. \n"

def newMove():
    global gonnalearn
    global npp
    global pp
    global ppmax
    global move1
    global move2
    global move3
    global move4
    if lvl==5:
        print wolf + " learnt Bite! \n"
        move2='Bite'
        pp[1]=40
        ppmax[1]=40
    elif lvl==12:
        print wolf + ' learnt Swipe! \n'
        move3='Swipe'
        pp[2]=35
        ppmax[2]=35
    elif lvl==18:
        print wolf + ' learnt Tooth Clamp! \n'
        move4='Tooth Clamp'
        pp[3]=30
        ppmax[3]=30
    elif lvl==23:
        print wolf + " wants to learn Supersonic Howl, but can only remember 4 moves. \n"
        gonnalearn="Supersonic Howl"
        npp=25
        noMoveSpaces()
    elif lvl==29:
        print wolf + " wants to learn Savage Claw, but can only remember 4 moves. \n"
        gonnalearn="Savage Claw"
        npp=25
        noMoveSpaces()
    elif lvl==34:
        print wolf + " wants to learn Shadow Swipe, but can only remember 4 moves. \n"
        gonnalearn="Shadow Swipe"
        npp=20
        noMoveSpaces()
    elif lvl==40:
        print wolf + " wants to learn Direwolf's Sorrow, but can only remember 4 moves. \n"
        gonnalearn="Direwolf's Sorrow"
        npp=15
        noMoveSpaces()
    elif lvl==47:
        print wolf + " wants to learn Spark Slice, but can only remember 4 moves. \n"
        gonnalearn="Spark Slice"
        npp=15
        noMoveSpaces()
    elif lvl==53:
        print wolf + " wants to learn Loping Claw, but can only remember 4 moves. \n"
        gonnalearn="Loping Claw"
        npp=10
        noMoveSpaces()
    elif lvl==61:
        print wolf + " wants to learn Moonlight Fang, but can only remember 4 moves. \n"
        gonnalearn="Moonlight Fang"
        npp=5
        noMoveSpaces()
    

dw=0
playing=False
xp=0 
nlvl=10 
lvl=1 
hp=50
moveAtk=0
health=50 
d=0 
cash=0 
pot=0 
enl=0 
atk=lvl*5
defence=lvl
instore=False
move1='Scratch'
pp=[10000,0,0,0]
ppmax=[10000,0,0,0]
move2=''
move3=''
move4=''
enemies=["Steppe Wolf", "Red Wolf", "Grey Wolf", "Black Stalker Wolf", "Wind Wolf", "Flame Wolf", "Ice Wolf", "White Wolf", "Hansa Wolf", "Hokkaida Wolf" ]
print "Welcome to THE GAME. You have one trained wolf. Your goal is to use this wolf to defeat other wolves, and level it up so that you can challenge the Five Wolf Sages. \n"
print "What would you like to name your wolf? \n"
def nameWolf():
    global wolf
    wolf=raw_input()
    lowername=str.lower(wolf)
    print " "
    namearray=str.split(lowername)
    for i in namearray:
        while i=="tejas":
            print "No. Fuck off. Choose another name. \n"
            nameWolf()
    while wolf=="":
        print "What would you like to name your wolf? \n"
        nameWolf()
nameWolf()
print " "
print "You named your wolf "+wolf
while lvl<100:
    top()
if lvl>=100:
    winGame()
