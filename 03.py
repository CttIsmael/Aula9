def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()
    return resultado


cidades = carrega_cidades()
dia = 0
aniversario = ()

day = int(input())
m = int(input())
aniversario = (day, m)
if aniversario[1] == 1:
    mes = 'JANEIRO'
elif aniversario[1] == 2:
    mes = 'FEVEREIRO'
elif aniversario[1] == 3:
    mes = 'MARÇO'

elif aniversario[1] == 4:
    mes = 'ABRIL'

elif aniversario[1] == 5:
    mes = 'MAIO'

elif aniversario[1] == 6:
    mes = 'JUNHO'

elif aniversario[1] == 7:
    mes = 'JULHO'

elif aniversario[1] == 8:
    mes = 'AGOSTO'

elif aniversario[1] == 9:
    mes = 'SETEMBRO'

elif aniversario[1] == 10:
    mes = 'OUTUBRO'

elif aniversario[1] == 11:
    mes = 'NOVEMBRO'

elif aniversario[1] == 12:
    mes = 'DEZEMBRO'

print(f'CIDADES QUE FAZEM ANIVERSÁRIO EM {day} DE {mes}:')    
for tupla in cidades:
    if tupla[4] == aniversario[1]:
        if tupla[3]== aniversario[0]:
            print(f'{tupla[2]}({tupla[0]})')
        
def main():
    carrega_cidades()

if __name__=='__main__':
    main()
