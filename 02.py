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
       soma =(clima1[0] + clima2[0])
       tm = (round(soma,4), clima1[1])
       print(tm)
    
    elif clima1[1]== 'C' and clima2[1] == 'C':
        soma =(clima1[0] + clima2[0])
        tm = (round(soma,4), clima2[1])
        print(tm)

    elif clima1[1]== 'F' and clima2[1] == 'C':
        t = (clima1[0]-32)*(5/9)
        soma = clima2[0]+t
        tm = (round(soma,4), clima2[1])
        print(tm)
            
    elif  clima1[1]=='C' and clima2[1] == 'F':
        t = (clima1[0]*(9/5))+32
        soma = clima2[0]+t
        tm = (round(soma,4), clima2[1])        
        print(tm)         
                  
def main():
    maior_temp()
    
if __name__=='__main__':
    main()
