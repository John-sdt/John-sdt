def tr(tr):
    dic={'31':'a','32':'b','11':'c','21':'d','41':'e','33':'f','34':'g',\
       '35':'h','36':'i','22':'j','37':'k','23':'l','42':'m','38':'n',\
       '12':'o','24':'p','25':'q','39':'r','13':'s','26':'t','14':'u',\
       '27':'v','43':'w','28':'x','51':'y','52':'z',' ':' ',',':',',\
        '.':'.','!':'!','?':'?','/':'/',';':';',':':':','(':'(',')':')',\
        "'":"'",'"':'"','-':'-','\n':'\n'}
    p=-1
    crypt=list(str(tr))
    def cg(a,b):
        del crypt[p:p+a]
        crypt.insert(p,b)

    for i in crypt:
        p+=1
        if i.isdigit() is True:
            crypt[p]+=crypt[p+1]
            del crypt[p+1]
        else:
            if p+4<=len(crypt):
                if crypt[p+3]=='h':    
                    cg(4,'\n')
                elif crypt[p+2].isdigit() is False:
                    if crypt[p+2]=='d':
                        cg(3,'.')
                    elif crypt[p+2]=='q':
                        cg(3,'?')
                    elif crypt[p+2]=='a':
                        cg(3,'!')
                    elif crypt[p+2]=='s':
                        cg(3,"'")
                    elif crypt[p+2]=='d':
                        cg(3,'"')
                    elif crypt[p+2]=='l':
                        cg(3,'(')
                    elif crypt[p+2]=='r':
                        cg(3,')')
                    elif crypt[p+2]=='c':
                        cg(3,':')
                    elif crypt[p+2]=='D':
                        cg(3,'/')
                    elif crypt[p+2]=='C':
                        cg(3,'-')
                    elif crypt[p+2]=='S':
                        cg(3,';')
                elif crypt[p+1].isdigit() is False:
                    cg(2,',')
                elif crypt[p].isdigit() is False:
                    cg(1,' ')
            elif p+3<=len(crypt):
                if crypt[p+2].isdigit() is False:
                    if crypt[p+2]=='d':
                        cg(3,'.')
                    elif crypt[p+2]=='q':
                        cg(3,'?')
                    elif crypt[p+2]=='a':
                        cg(3,'!')
                    elif crypt[p+2]=='s':
                        cg(3,"'")
                    elif crypt[p+2]=='d':
                        cg(3,'"')
                    elif crypt[p+2]=='l':
                        cg(3,'(')
                    elif crypt[p+2]=='r':
                        cg(3,')')
                    elif crypt[p+2]=='c':
                        cg(3,':')
                    elif crypt[p+2]=='D':
                        cg(3,'/')
                    elif crypt[p+2]=='C':
                        cg(3,'-')
                    elif crypt[p+2]=='S':
                        cg(3,';')
                elif crypt[p+1].isdigit() is False:
                    cg(2,',')
                elif crypt[p].isdigit() is False:
                    cg(1,' ')            
    print('Your chapter is:')
    for i in crypt:
        print(dic[i],end='')

