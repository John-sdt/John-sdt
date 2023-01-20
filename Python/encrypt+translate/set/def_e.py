def en(en):
    import random
    dic_1={'a':31,'b':32,'c':11,'d':21,'e':41,'f':33,'g':34,\
        'j':22,'k':37,'l':23,'m':42,'n':38,'o':12,'p':24,\
        'q':25,'r':39,'s':13,'t':26,'u':14,'v':27,'w':43,\
        'x':28,'y':51,'z':52,'A':31,'B':32,'C':11,'D':21,\
        'E':41,'F':33,'G':34,'H':35,'I':36,'h':35,'i':36,\
        'J':22,'K':37,'L':23,'M':42,'N':38,'O':12,'P':24,\
        'Q':25,'R':39,'S':13,'T':26,'U':14,'V':27,'W':43,\
        'X':28,'Y':51,'Z':52,'0':50,'1':51,'2':52,'3':53,\
        '4':54,'5':55,'6':56,'7':57,'8':58,'9':59}
    dic_2={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'z',9:'i',\
        10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',\
        19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y'}
    encrypt=[]

    chapter=list(str(en))
    for i in range (0,len(chapter)):
        if chapter[i]==' ':
            encrypt+=list(dic_2[random.randint(1,23)])
        elif chapter[i]==',':
            encrypt+=list(dic_2[random.randint(1,23)]+dic_2[random.randint(1,23)])
        elif chapter[i]=='.':
            encrypt+=list(dic_2[random.randint(1,23)]+dic_2[random.randint(1,23)]+'d')
        elif chapter[i]=='?':
            encrypt+=list(dic_2[random.randint(1,23)]+dic_2[random.randint(1,23)]+'q')
        elif chapter[i]=='!':
            encrypt+=list(dic_2[random.randint(1,23)]+dic_2[random.randint(1,23)]+'a')
        elif chapter[i]=="'":
            encrypt+=list(dic_2[random.randint(1,23)]+dic_2[random.randint(1,23)]+'s')
        elif chapter[i]=='"':
            encrypt+=list(dic_2[random.randint(1,23)]+dic_2[random.randint(1,23)]+'d')
        elif chapter[i]=='(':
            encrypt+=list(dic_2[random.randint(1,23)]+dic_2[random.randint(1,23)]+'l')
        elif chapter[i]==')':
            encrypt+=list(dic_2[random.randint(1,23)]+dic_2[random.randint(1,23)]+'r')
        elif chapter[i]==':':
            encrypt+=list(dic_2[random.randint(1,23)]+dic_2[random.randint(1,23)]+'c')
        elif chapter[i]=='-':
            encrypt+=list(dic_2[random.randint(1,23)]+dic_2[random.randint(1,23)]+'C')
        elif chapter[i]==';':
            encrypt+=list(dic_2[random.randint(1,23)]+dic_2[random.randint(1,23)]+'S')
        elif chapter[i]=='/':
            encrypt+=list(dic_2[random.randint(1,23)]+dic_2[random.randint(1,23)]+'D')
        elif chapter[i]=='\\':
            encrypt+=list(dic_2[random.randint(1,23)]+dic_2[random.randint(1,23)]+\
                dic_2[random.randint(1,23)]+'h')
        else:
            encrypt+=list(str(dic_1[chapter[i]]))
    print('Your cryptogram is:')
    for i in range(0,len(encrypt)):
        print(encrypt[i],end='')
