def maior(m):
    mx = m[0][0]
    pmx = ()
    
    for i in range(len(m)):
        for j in range(len(m[i])):      
            if m[i][j] >mx:
                pmx = i,j
                mx = m[i][j]
            elif mx == m[0][0]:
                pmx = 0,0
    print(pmx)  
    
def menor(m):
    mnr = m[0][0]
    pm = ()
    for i in range(len(m)):
        for j in range(len(m[i])):      
            if m[i][j] < mnr:
                pm = i,j
                mnr = m[i][j]
            elif mnr == m[0][0]:
                pm = 0,0    
            
    print(pm)

def main():
    linhas = colunas = int(input())
    m = []
    for linn in range(linhas):
        linha = []
        for col in range(colunas):
            x = int(input())
            linha.append(x)
        m.append(linha)
    maior(m)
    menor(m)

if __name__=='__main__':
    main()
