def soma_pr_linha(matrix):
    soma =0
    sm=()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i ==0:
                soma += matrix[i][j]
                sm=(soma)

    return(sm)

def soma_ultima_col(matrix, colunas):
    s_col = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == (colunas-1):
                s_col += matrix[i][j]
    return(s_col)

def media_elementos(matrix, linhas, colunas):
    soma =0
    media =0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            soma+= matrix[i][j]
    media = soma/(linhas*colunas)
    return round(media, 4)

def maior_n(matrix):
    mx = matrix[0][0]
        
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):      
            if matrix[i][j] >mx:
                mx = matrix[i][j]
            else:
                mx == matrix[0][0]            
    return(mx) 

def menor_n(matrix):
    mnr = matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):      
            if matrix[i][j] < mnr:
                mnr = matrix[i][j]
            else:
                mnr == matrix[0][0]                    
    return(mnr) 

def main():
    linhas = int(input())
    colunas = int(input())
    matrix = []
    for linn in range(linhas):
        linha = []
        for col in range(colunas):
            x = int(input())
            linha.append(x)
        matrix.append(linha)
    

    sm = soma_pr_linha(matrix)
    col = soma_ultima_col(matrix, colunas)
    md_el = media_elementos(matrix, linhas, colunas)
    menor = menor_n(matrix)
    maior = maior_n(matrix)
    resp = ()
    resp =(sm, col, md_el, menor, maior) 
    print(resp)



if __name__=='__main__':
    main()
