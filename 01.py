def maior_temp():
    clima1 = ()
    clima2 = ()

    t = float(input())
    esc = input().upper()[0]
    clima1 = (t, esc)
    
    t = float(input())
    esc = input().upper()[0]
    clima2 = (t, esc)    
         
    if clima1[1]== 'F' and clima2[1] == 'F':
        if clima1[0] > clima2[0]:
            print(clima1)
        else:
            print(clima2)
    
    elif clima1[1]== 'C' and clima2[1] == 'C':
        if clima1[0] > clima2[0]:
            print(clima1)
        else:
            print(clima2)
            
    elif clima1[1]== 'C' and clima2[1] == 'F':
        t = (clima2[0]-32)*(5/9)
        if clima1[0]>t:
            print(clima1)
        else:
            print(clima2)
            
    elif  clima1[1]=='F' and clima2[1] == 'C':
        t = (clima2[0]*(9/5))+32
        if clima1[0]>t:
            print(clima1)
        else:
            print(clima2)
         

def main():
    maior_temp()
    
if __name__=='__main__':
    main()
