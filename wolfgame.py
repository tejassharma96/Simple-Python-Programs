from random import randint

def endl(x):
    return " \n"

a=0
if(a==0):
    dw=0 
    xp=0 
    nlvl=10 
    lvl=1 
    hp=50
    health=50 
    d=0 
    cash=0 
    pot=0 
    enl=0 
    atk=lvl*5 
    defence=lvl 
    enemies=["Steppe Wolf", "Red Wolf", "Grey Wolf", "Black Stalker Wolf", "Wind Wolf", "Flame Wolf", "Ice Wolf", "White Wolf", "Hansa Wolf", "Hokkaida Wolf" ]
    print "Welcome to THE GAME. You have one trained wolf. Your goal is to use this wolf to defeat other wolves, and level it up so that you can challenge the Five Wolf Sages. \n" 
    print "What would you like to name your wolf? \n" 
    wolf=raw_input()
    print "You named your wolf "+wolf
    do:
        label .top
            print "What would you like to do? \n" 
            print "1. Search for wolves \n" 
            print "2. Store \n" 
            print "3. Potion \n" 
            print "4. Show stats \n" 
            print "5. Battle Five Wolf Sages \n" 
            print "6. Exit Game \n" 
            a=input() 
            if (a==1):
                if (lvl>=1&&lvl<5):
                    enl=1 
                elif (lvl>=5&&lvl<10):
                    enl=1 
                elif (lvl>=10&&lvl<5):
                    enl=1 
                elif (lvl>=15&&lvl<5):
                    enl=4 
                elif (lvl>=20&&lvl<5):
                    enl=9 
                elif(lvl>=25&&lvl<5):
                    enl=14 
                elif (lvl>=30&&lvl<5):
                    enl=19  
                elif (lvl>=40&&lvl<50):
                    enl=24  
                elif (lvl>=50&&lvl<55):
                    enl=29  
                elif(lvl>=55):
                    enl=34
                
                elvl=randrange(enl,(lvl-1))
                ehp=elvl*10 
                eatk=elvl*2 
                edef=elvl 
                print "A level "+`elvl`+" "+enemies[b]+" (attack = "+`eatk`+", defence = "+`edef`+", health = "+`ehp`+") attacked! \n" 
                label .attack                
                while (ehp>0):
                    print "1. Attack \n" 
                    print "2. Use a potion \n" 
                    print "3. Attempt to run \n" 
                    ab=input() 
                    if (ab==1):
                        if (health-(eatk-defence)>0||ehp-(atk-edef)<=0):
                            if(health-(eatk-defence)>0&&ehp-(atk-edef)>0):
                                health=health-(eatk-defence) 
                                ehp=ehp-(atk-edef) 
                                print wolf+" attacked wild "+enemies[b]+" and brought his health down to "+`ehp`+endl()
                                print "Wild "+enemies[b]+" attacked "+wolf+" and brought his health down to "+`health`+endl(10) 
                                goto .attack  
                            elif(ehp-(atk-edef)<=0):
                                print wolf+" attacked wild "+enemies[b]+endl(10) 
                                print enemies[b]+" died \n" 
                                break 
                            
                        else:
                            label .death
                            print wolf+" died and was able to defeat "+`d`+" wolves before he died \n" 
                            print "Resurrect? (y/n) \n" 
                            ch=raw_input()
                            if (ch=='y'):
                                health=hp 
                                d=0 
                                print "Health set to "+`hp`+" and kill number set to 0 \n" 
                                goto .top 
                            elif (ch=='n'):
                                print "Well press the exit button yourself then or continue plaing \n" 
                                health=hp 
                                d=0 
                                print "Health set to "+`hp`+" and kill number set to 0 \n" 
                                goto .top 
                            else:
                                print "Incorrect input, the program will assume you want to keep playing \n" 
                                health=hp 
                                d=0 
                                print "Health set to "+`hp`+" and kill number set to 0 \n" 
                                goto .top 
                            
                    elif (ab==3):
                        c=randrange(0,100+1) 
                        if (c%2==0):
                            print "You escaped safely and"+wolf+" gained 2 xp \n" 
                            xp=xp+2 
                            if (xp<nlvl):
                                print wolf+" has "+`xp`+" xp. "+`nlvl-xp`+" till a new level \n" 
                            
                            elif (xp>=nlvl):
                                lvl+=1 
                                print "Congratulations, "+wolf+" gained a level. He is now level "+`lvl`+"! \n" 
                                hp=hp+10 
                                print wolf+"'s max health has been extended to "+`hp`+"HP \n" 
                                atk=lvl*5 
                                defence=lvl*2 
                                print "His attack has been increased to "+`atk`+" and his defence to "+`defence`+","+endl(10) 
                                if (health+eatk<=hp):
                                    health=health+eatk 
                                else:
                                    health=hp 
                                
                                print "And his current health has been increased to "+`health`+"HP \n" 
                                nlvl=nlvl+10 
                                if (lvl==40):
                                    print "Congratulations! \n" 
                                    print "On reaching level 40 "+wolf+" has been promoted to Direwolf status. You can now battle the Five Wolf Sages, though it is reccomended to train "+wolf+" to level 50 first \n" 
                                    dw=1 
                                
                            
                            goto .top 
                        
                        else:
                            if(health-(eatk-defence)!=0):
                                print enemies[b]+" attacked "+wolf+" and brought his health down to"+`health-(eatk-defence)`+endl(10) 
                                goto .attack 
                            else:
                                print enemies[b]+" attacked "+wolf+" and caused him to die \n" 
                                goto .death 
                            
                        
                    elif(ab==2):
                        if (pot>0):
                            if (health<=hp-80):
                                health=health+80 
                            else:
                                health=hp 
                            
                            print "You used a potion. "+wolf+"'s health is now "+`health`+" \n" 
                            print "You have "+`pot`+" potions left" 
                            goto .attack 
                        else:
                            print "You don't have any potions remaining. Please buy one from the store \n" 
                            goto .attack 
                        
                    else:
                        print "Incorrect input \n" 
                        goto .attack 
                     
                
                
                xp=xp+(b) 
                ci=randrange(1,15) 
                print wolf+" defeated the animal \n" 
                print wolf+"'s health is now "+`health`+" \n" 
                cash=cash+ci 
                print "You now have "+`cash`+" cash \n" 
                if (xp<nlvl):
                    print wolf+" has "+`xp`+" xp. "+`nlvl-xp`+" till a new level \n" 
                
                elif (xp>=nlvl):
                    lvl+=1 
                    print "Congratulations, "+wolf+" gained a level. He is now level "+`lvl`+"! \n" 
                    hp=hp+10 
                    print wolf+"'s max health has been extended to "+`hp`+"HP \n" 
                    print "His attack has been increased to: " 
                    if (health+eatk<=hp):
                        health=health+eatk 
                    else:
                        health=hp 
                    
                    print wolf+"'s current health has been increased to "+`health`+"HP \n" 
                    nlvl=nlvl+((lvl-1)*10) 
                    if (lvl==40):
                        print "Congratulations! \n" 
                        print "On reaching level 40 "+wolf+" has been promoted to Direwolf status. You can now battle the Five Wolf Sages, though it is reccomended to train "+wolf+" to level 50 first \n" 
                        dw=1 
                    
                
                d+=1 
                goto .top 
                
            
            elif (a==6):
                print "Well press the exit button yourself then or continue playing \n" 
                goto .top 
            elif (a==2):
                label .store
                print "1. Buy health potion. Will heal by 80 (10 cash) \n" 
                print "2. Increase max health by 5 (20 cash) \n" 
                print "3. Increase level (50 cash) \n" 
                print "4. Exit store \n" 
                e=input()
                if (e==1):
                    if (cash>=10):
                        cash=cash-10 
                        pot+=1 
                        print "You now have "+`pot`+" potions \n" 
                        goto .store 
                    else:
                        print "Not enough money/Incorrect input \n" 
                        goto .top 
                    
                elif (e==2):
                    if (cash>=20):
                        cash=cash-20 
                        hp=hp+10 
                        print wolf+"'s max health has been extended to "+`hp`+"HP \n" 
                        print "You now have "+`cash`+" cash \n" 
                        goto .store 
                    else:
                        print "Not enough money/Incorrect input \n" 
                        goto .top 
                    
                elif (e==3):
                    if (cash>=50):
                        cash=cash-50 
                        lvl+=1 
                        print "Congratulations, "+wolf+" gained a level. He is now level "+`lvl`+"! \n" 
                        print "You now have "+`cash`+" cash \n" 
                        hp=hp+10 
                        print wolf+"'s max health has been extended to "+`hp`+"HP \n" 
                        atk=lvl*5 
                        defence=lvl*2 
                        print "His attack has been increased to "+`atk`+" and his defence to "+`defence`+","+endl(10) 
                        if (health+20<=hp):
                            health=health+20 
                        else:
                            health=hp 
                        
                        print "And his current health has been increased to "+`health`+"HP \n" 
                        nlvl=nlvl+10 
                        if (lvl==40):
                            print "Congratulations! \n" 
                            print "On reaching level 40 "+wolf+" has been promoted to Direwolf status. You can now battle the Five Wolf Sages, though it is reccomended to train "+wolf+" to level 50 first \n" 
                            dw=1 
                        
                        goto .store 
                    else:
                        print "Not enough money/Incorrect input \n" 
                        goto .top 
                    
                elif (e==4):
                    goto .top 
                else:
                    print "Incorrect input. \n" 
                    goto .store 
                
            elif (a==3):
                if (pot>0):
                    if (health<=hp-80):
                        health=health+80 
                    else:
                        health=hp 
                    
                    print "You used a potion. "+wolf+"'s health is now "+`health`+" \n" 
                    print "You have "+`pot`+" potions left" 
                    goto .top 
                else:
                    print "You don't have any potions remaining. Please buy one from the store \n" 
                    goto .top 
                
                
            elif (a==1996):
                cash=cash+10000000 
                print "CHEAT CODE!!! Cash set to "+`cash`+endl(10) 
                goto .top 
            elif(a==4):
                print "Stats: \n" 
                print "Current level: "+`lvl`+endl(10) 
                print "XP to new level: "+`nlvl`-xp+endl(10) 
                print "Current health: "+`health`+endl(10) 
                print "Maximum health: "+`hp`+endl(10) 
                print "Attack power: "+`atk`+endl(10) 
                print "Defense power: "+`defence`+endl(10) 
                print "Current money: "+`cash`+" cash \n" 
                print "Number of potions: "+`pot`+endl(10) 
                if(dw==0)
                    print "Direwolf status: not yet" 
                else 
                    print "Direwolf status: achieved" 
                goto .top 
                
            elif(a==5):
                if (dw==0):
                    print wolf+" is not a Direwolf yet. Please train him some more." 
                    goto .top 
                else:
                    print "Are you sure you want to challenge the Five Wolf Sages? (y/n) \n" 
                    ptc=raw_input() 
                    if (ptc=='n'):
                        print "You can always battle the Five Wolf Sages again later. Good luck training!" 
                        goto .top 
                    elif (ptc=='y'):
                        
                        print "The first sage is Canis \n" 
                        print "Level: 55 \n" 
                        elvl=55 
                        print "HP: 550 \n" 
                        ehp=550 
                        print "Attack: 110 \n" 
                        eatk=110 
                        print "Defence: 55 \n" 
                        edef=55 
                        do:
                        label .cattack
                            print "1. Attack \n" 
                            print "2. Use a potion \n" 
                            print "3. Attempt to run \n" 
                            ab=input() 
                            if (ab==1):
                                if (health-(eatk-defence)>0||ehp-atk<=0):
                                    if(health-(eatk-defence)>0&&ehp-atk>0):
                                        health=health-eatk 
                                        ehp=ehp-atk 
                                        print wolf+" attacked Canis and brought his health down to "+`ehp`+endl(10) 
                                        print "Canis attacked "+wolf+" and brought his health down to "+`health`+endl(10) 
                                        goto .cattack  
                                    elif(ehp-(atk-edef)):
                                        print wolf+" attacked Canis \n" 
                                        print "Canis died \n" 
                                        break 
                                    
                                else:
                                label .cdeath:
                                    print wolf+"died and was able to defeat "+`d`+" animals \n" 
                                    print "Resurrect? (y/n) \n" 
                                    ch=raw_input() 
                                    if (ch=='y'):
                                        health=hp 
                                        d=0 
                                        print "Health set to "+`hp`+" and kill number set to 0 \n" 
                                        goto .top 
                                    elif (ch=='n'):
                                        print "Well press the exit button yourself then or continue plaing \n" 
                                        health=hp 
                                        d=0 
                                        print "Health set to "+`hp`+" and kill number set to 0 \n" 
                                        goto .top 
                                    else:
                                        print "Incorrect input, the program will assume you want to keep playing \n" 
                                        health=hp 
                                        d=0 
                                        print "Health set to "+`hp`+" and kill number set to 0 \n" 
                                        goto .top 
                                    
                            elif (ab==3):
                                print "Can't run!" 
                                if(health-(eatk-defence)!=0)
                                    print "Canis attacked "+wolf+" and brought his health down to"+`health-(eatk-defence)`+endl(10) 
                                else:
                                    print "Canis attacked "+wolf+" and caused him to die \n" 
                                    goto cdeath 
                                
                            elif(ab==2):
                                if (pot>0):
                                    if (health<=hp-80):
                                        health=health+80 
                                    else:
                                        health=hp 
                                    
                                    print "You used a potion. "+wolf+"'s health is now "+health+" \n" 
                                    print "You have "+pot+" potions left" 
                                    goto .cattack 
                                else:
                                    print "You don't have any potions remaining. Please buy one from the store \n" 
                                    goto .cattack 
                                
                            else:
                                print "Incorrect input \n" 
                                goto .cattack 
                            
                         while (ehp>0&&health>0) 
                        
                        print "The second sage is Sirius \n" 
                        print "Level: 60 \n" 
                        elvl=60 
                        print "HP: 600 \n" 
                        ehp=600 
                        print "Attack: 120 \n" 
                        eatk=120 
                        print "Defence: 60 \n" 
                        edef=60 
                        do:
                        .sattack:
                            print "1. Attack \n" 
                            print "2. Use a potion \n" 
                            print "3. Attempt to run \n" 
                            a=input()b 
                            if (ab==1):
                                if (health-(eatk-defence)>0||ehp-atk<=0):
                                    if(health-(eatk-defence)>0&&ehp-atk>0):
                                        health=health-eatk 
                                        ehp=ehp-atk 
                                        print wolf+" attacked Sirius and brought his health down to "+ehp+endl(10) 
                                        print "Sirius attacked "+wolf+" and brought his health down to "+health+endl(10) 
                                        goto .sattack  
                                    elif(ehp-(atk-edef)):
                                        print wolf+" attacked Sirius \n" 
                                        print "Sirius died \n" 
                                        break 
                                    
                                else:
                                sdeath:
                                    print wolf+"died and was able to defeat "+d+" animals \n" 
                                    print "Resurrect? (y/n) \n" 
                                    cin>>ch 
                                    if (ch=='y'):
                                        health=hp 
                                        d=0 
                                        print "Health set to "+hp+" and kill number set to 0 \n" 
                                        goto .top 
                                    elif (ch=='n'):
                                        print "Well press the exit button yourself then or continue plaing \n" 
                                        health=hp 
                                        d=0 
                                        print "Health set to "+hp+" and kill number set to 0 \n" 
                                        goto .top 
                                    else:
                                        print "Incorrect input, the program will assume you want to keep playing \n" 
                                        health=hp 
                                        d=0 
                                        print "Health set to "+hp+" and kill number set to 0 \n" 
                                        goto .top 
                                    
                            elif (ab==3):
                                print "Can't run!" 
                                if(health-(eatk-defence)!=0)
                                    print "Sirius attacked "+wolf+" and brought his health down to"+health-(eatk-defence)+endl(10) 
                                else:
                                    print "Sirius attacked "+wolf+" and caused him to die \n" 
                                    goto sdeath 
                                
                            elif(ab==2):
                                if (pot>0):
                                    if (health<=hp-80):
                                        health=health+80 
                                    else:
                                        health=hp 
                                    
                                    print "You used a potion. "+wolf+"'s health is now "+health+" \n" 
                                    print "You have "+pot+" potions left" 
                                    goto .sattack 
                                else:
                                    print "You don't have any potions remaining. Please buy one from the store \n" 
                                    goto .sattack 
                                
                            else:
                                print "Incorrect input \n" 
                                goto .sattack 
                            
                         while (ehp>0&&health>0) 
                        
                        print "The third sage is Ragnarok \n" 
                        print "Level: 65 \n" 
                        elvl=65 
                        print "HP: 650 \n" 
                        ehp=650 
                        print "Attack: 130 \n" 
                        eatk=130 
                        print "Defence: 65 \n" 
                        edef=65 
                        do:
                        rattack:
                            print "1. Attack \n" 
                            print "2. Use a potion \n" 
                            print "3. Attempt to run \n" 
                            a=input()b 
                            if (ab==1):
                                if (health-(eatk-defence)>0||ehp-atk<=0):
                                    if(health-(eatk-defence)>0&&ehp-atk>0):
                                        health=health-eatk 
                                        ehp=ehp-atk 
                                        print wolf+" attacked Ragnarok and brought his health down to "+ehp+endl(10) 
                                        print "Ragnarok attacked "+wolf+" and brought his health down to "+health+endl(10) 
                                        goto rattack  
                                    elif(ehp-(atk-edef)):
                                        print wolf+" attacked Ragnarok \n" 
                                        print "Ragnarok died \n" 
                                        break 
                                    
                                else:
                                rdeath:
                                    print wolf+"died and was able to defeat "+d+" animals \n" 
                                    print "Resurrect? (y/n) \n" 
                                    cin>>ch 
                                    if (ch=='y'):
                                        health=hp 
                                        d=0 
                                        print "Health set to "+hp+" and kill number set to 0 \n" 
                                        goto .top 
                                    elif (ch=='n'):
                                        print "Well press the exit button yourself then or continue plaing \n" 
                                        health=hp 
                                        d=0 
                                        print "Health set to "+hp+" and kill number set to 0 \n" 
                                        goto .top 
                                    else:
                                        print "Incorrect input, the program will assume you want to keep playing \n" 
                                        health=hp 
                                        d=0 
                                        print "Health set to "+hp+" and kill number set to 0 \n" 
                                        goto .top 
                                    
                            elif (ab==3):
                                print "Can't run!" 
                                if(health-(eatk-defence)!=0)
                                    print "Ragnarok attacked "+wolf+" and brought his health down to"+health-(eatk-defence)+endl(10) 
                                else:
                                    print "Ragnarok attacked "+wolf+" and caused him to die \n" 
                                    goto cdeath 
                                
                            elif(ab==2):
                                if (pot>0):
                                    if (health<=hp-80):
                                        health=health+80 
                                    else:
                                        health=hp 
                                    
                                    print "You used a potion. "+wolf+"'s health is now "+health+" \n" 
                                    print "You have "+pot+" potions left" 
                                    goto rattack 
                                else:
                                    print "You don't have any potions remaining. Please buy one from the store \n" 
                                    goto rattack 
                                
                            else:
                                print "Incorrect input \n" 
                                goto rattack 
                            
                         while (ehp>0&&health>0) 
                        
                        print "The fourth sage is Skoll \n" 
                        print "Level: 70 \n" 
                        elvl=70 
                        print "HP: 700 \n" 
                        ehp=700 
                        print "Attack: 140 \n" 
                        eatk=140 
                        print "Defence: 70 \n" 
                        edef=70 
                        do:
                        skattack:
                            print "1. Attack \n" 
                            print "2. Use a potion \n" 
                            print "3. Attempt to run \n" 
                            a=input()b 
                            if (ab==1):
                                if (health-(eatk-defence)>0||ehp-atk<=0):
                                    if(health-(eatk-defence)>0&&ehp-atk>0):
                                        health=health-eatk 
                                        ehp=ehp-atk 
                                        print wolf+" attacked Skoll and brought his health down to "+ehp+endl(10) 
                                        print "Skoll attacked "+wolf+" and brought his health down to "+health+endl(10) 
                                        goto skattack  
                                    elif(ehp-(atk-edef)):
                                        print wolf+" attacked Skoll \n" 
                                        print "Skoll died \n" 
                                        break 
                                    
                                else:
                                skdeath:
                                    print wolf+"died and was able to defeat "+d+" animals \n" 
                                    print "Resurrect? (y/n) \n" 
                                    cin>>ch 
                                    if (ch=='y'):
                                        health=hp 
                                        d=0 
                                        print "Health set to "+hp+" and kill number set to 0 \n" 
                                        goto .top 
                                    elif (ch=='n'):
                                        print "Well press the exit button yourself then or continue plaing \n" 
                                        health=hp 
                                        d=0 
                                        print "Health set to "+hp+" and kill number set to 0 \n" 
                                        goto .top 
                                    else:
                                        print "Incorrect input, the program will assume you want to keep playing \n" 
                                        health=hp 
                                        d=0 
                                        print "Health set to "+hp+" and kill number set to 0 \n" 
                                        goto .top 
                                    
                            elif (ab==3):
                                print "Can't run!" 
                                if(health-(eatk-defence)!=0)
                                    print "Skoll attacked "+wolf+" and brought his health down to"+health-(eatk-defence)+endl(10) 
                                else:
                                    print "Skoll attacked "+wolf+" and caused him to die \n" 
                                    goto skdeath 
                                
                            elif(ab==2):
                                if (pot>0):
                                    if (health<=hp-80):
                                        health=health+80 
                                    else:
                                        health=hp 
                                    
                                    print "You used a potion. "+wolf+"'s health is now "+health+" \n" 
                                    print "You have "+pot+" potions left" 
                                    goto .cattack 
                                else:
                                    print "You don't have any potions remaining. Please buy one from the store \n" 
                                    goto .cattack 
                                
                            else:
                                print "Incorrect input \n" 
                                goto .cattack 
                            
                         while (ehp>0&&health>0) 
                        
                        print "The final sage is Fenrir \n" 
                        print "Level: 90 \n" 
                        elvl=90 
                        print "HP: 900 \n" 
                        ehp=900 
                        print "Attack: 180 \n" 
                        eatk=180 
                        print "Defence: 90 \n" 
                        edef=90 
                        do:
                        fattack:
                            print "1. Attack \n" 
                            print "2. Use a potion \n" 
                            print "3. Attempt to run \n" 
                            a=input()b 
                            if (ab==1):
                                if (health-(eatk-defence)>0||ehp-atk<=0):
                                    if(health-(eatk-defence)>0&&ehp-atk>0):
                                        health=health-eatk 
                                        ehp=ehp-atk 
                                        print wolf+" attacked Fenrir and brought his health down to "+ehp+endl(10) 
                                        print "Fenrir attacked "+wolf+" and brought his health down to "+health+endl(10) 
                                        goto fattack  
                                    elif(ehp-(atk-edef)<=0):
                                        print wolf+" attacked Fenrir \n" 
                                        print "Fenrir died \n" 
                                        break 
                                    
                                else:
                                fdeath:
                                    print wolf+"died and was able to defeat "+d+" animals \n" 
                                    print "Resurrect? (y/n) \n" 
                                    cin>>ch 
                                    if (ch=='y'):
                                        health=hp 
                                        d=0 
                                        print "Health set to "+hp+" and kill number set to 0 \n" 
                                        goto .top 
                                    elif (ch=='n'):
                                        print "Well press the exit button yourself then or continue plaing \n" 
                                        health=hp 
                                        d=0 
                                        print "Health set to "+hp+" and kill number set to 0 \n" 
                                        goto .top 
                                    else:
                                        print "Incorrect input, the program will assume you want to keep playing \n" 
                                        health=hp 
                                        d=0 
                                        print "Health set to "+hp+" and kill number set to 0 \n" 
                                        goto .top 
                                    
                            elif (ab==3):
                                print "Can't run!" 
                                if(health-(eatk-defence)!=0)
                                    print "Fenrir attacked "+wolf+" and brought his health down to"+health-(eatk-defence)+endl(10) 
                                else:
                                    print "Fenrir attacked "+wolf+" and caused him to die \n" 
                                    goto fdeath 
                                
                            elif(ab==2):
                                if (pot>0):
                                    if (health<=hp-80):
                                        health=health+80 
                                    else:
                                        health=hp 
                                    
                                    print "You used a potion. "+wolf+"'s health is now "+health+" \n" 
                                    print "You have "+pot+" potions left" 
                                    goto fattack 
                                else:
                                    print "You don't have any potions remaining. Please buy one from the store \n" 
                                    goto fattack 
                                
                            else:
                                print "Incorrect input \n" 
                                goto fattack 
                            
                         while (ehp>0&&health>0) 
                        
                        print "CONGRATULATIONS!!!!! You defeated the Five Wolf Sages and have mastered the game. You can quit now or continue playing until you reach level 100 when you will be forced to either quit or restart \n" 
                        print wolf+" has gained 5 levels. He is now level "+lvl+5+". \n" 
                        lvl=lvl+5 
                        hp=hp+50 
                        print wolf+"'s max health has been extended to "+hp+"HP \n" 
                        atk=lvl*5 
                        defence=lvl*2 
                        print "His attack has been increased to "+atk+" and his defence to "+defence+","+endl(10) 
                        health = hp 
                        print "And his current health has been fully restored to "+health+"HP \n" 
                        nlvl=nlvl+50 
                        goto .top                         
                        
                    else:
                        print "Incorrect input. The program will assume you do not want to challenge the Five Wolf Sages. Good luck training!" 
                    
                
                goto .top 
            else:
                print "Incorrect input" 
                goto .top 
            
        
    while (lvl<100) 
    print wolf+" is now level 100 and you have defeated the game. Play again?(y/n) \n" 
    cin>>cha 
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
        goto .top 
    elif (cha=='n'):
        print "Well press the exit button yourself then or continue plaing \n" 
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
        goto .top 
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
        goto .top 
    

    return 0         

