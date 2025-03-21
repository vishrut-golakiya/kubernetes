print("welcome to the rollercoster")
score= float(input("what is your hight in foot? "))
bill= 0
if score>=5.2:
    print("u can ride a rollercoster")
    age= int(input("what is your age? "))    
    if(age<12):
        print("+$5")
        bill= bill+5
    elif(age>=12 and age<=18):
        bill= bill+7
    elif(age>=45 and age<=55):
        bill= bill+0    
    else:
        bill= bill+12
    photo= (input("u want photo yes or no? "))
    if(photo=="yes"):
        bill= bill+3
        print("the total bill is", bill )
    else:
        print("the total bill is", bill )


else:
    print("u can not ride rollercoster")   
     



