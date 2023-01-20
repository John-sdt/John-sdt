import time;import turtle as t;import sys
sys.path.append('PATH TO def_e.py')
sys.path.append('PATH TO def_t.py')
from def_e import en
from def_t import tr
A=['2923692762','1']
AP={'2923692762':'yhj123abc','1':'1'}
At=input('Account:')
if At in A:
    for i in range(4):
        Pw = input("Password：");
        
        if Pw ==AP[At]:#Right Pw
            print('密码正确'+'\n'+'请3s后输入验证码')
            #王
            t.setup(500,500)
            t.colormode(255)
            t.pensize(20)

            t.penup()
            t.goto(-100,75)
            t.pd()
            t.goto(100,95)

            t.pu()
            t.goto(-50,-5)
            t.pd()
            t.goto(50,5)

            t.pu()
            t.goto(0,85)
            t.pd()
            t.goto(0,-85)

            t.pu()
            t.goto(-150,-100)
            t.pd()
            t.goto(150,-70)
            time.sleep(3)

            for i in range(3):
                Ck=input('您看到的汉字是：')
                if Ck in ['王','1','wang']: #Right check
                    print('Welcome!')
                    '''以下可为登录后可执行内容
                        ......
                    '''
                    while True :
                        choose=input('\n'+'加密请输入K,翻译请输入T,其它任意键注销：'+'\n')
                        if choose in ['K','k']:
                            en(input('Your chapter:'+'\n'))
                        elif choose in ['t','T']:
                            tr(input('Your cryptogram:'+'\n'))
                        else :
                            break
                    break
                else: #Wrong check
                    if i!=2:
                        print('验证码错误')
                    else:
                        print('次数用尽!')
            break
        else : #Wrong Pw
            if i==3:
                print('次数已用尽!')
            else :
                print('请再试一次')


                
else: #Wrong At
    print('账号不存在!')
