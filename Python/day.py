y,m,d=map(int,input('yyyy/mm/dd:'+'\n').split('/'))
n=0

#year
for i in range(y-1):
    #闰年
    if i%4==0 and (i%100!=0 or i%400==0):
        n+=366
    #非闰年
    else:
        n+=365

#month
if m==1:
    p=0
elif m==2:
    p=31
elif m==3:
    p=31+28
elif m==4:
    p=31+28+31
elif m==5:
    p=31+28+31+30
elif m==6:
    p=31+28+31+30+31
elif m==7:
    p=31+28+31+30+31+30
elif m==8:
    p=31+28+31+30+31+30+31
elif m==9:
    p=31+28+31+30+31+30+31+31
elif m==10:
    p=31+28+31+30+31+30+31+31+30
elif m==11:
    p=31+28+31+30+31+30+31+31+30+31
elif m==12:
    p=31+28+31+30+31+30+31+31+30+31+30
    
if y%4==0 and (y%100!=0 or y%400==0) and m>=3:
    p+=1

#day
q=d

#sum
s=n+p+q
e=s%7-1
dic={1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',-1:'Saturday',0:'Sunday'}
print(dic[e])
