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
mes_pop = ()

m = int(input())
popl = int(input())
mes_pop = (m, popl)

if mes_pop[0] == 1:
    mes = 'Janeiro'
elif mes_pop[0] == 2:
    mes = 'Fevereiro'
elif mes_pop[0] == 3:
    mes = 'Março'
elif mes_pop[0] == 4:
    mes = 'Abril'
elif mes_pop[0] == 5:
    mes = 'Maio'
elif mes_pop[0] == 6:
    mes = 'Junho'

elif mes_pop[0] == 7:
    mes = 'Julho'

elif mes_pop[0] == 8:
    mes = 'Agosto'

elif mes_pop[0] == 9:
    mes = 'Setembro'

elif mes_pop[0] == 10:
    mes = 'Outubro'

elif mes_pop[0] == 11:
    mes = 'Novembro'

elif mes_pop[0] == 12:
    mes = 'Dezembro'

print(f'CIDADES COM MAIS DE {popl} HABITANTES E ANIVERSÁRIO EM {mes.upper()}:')  

for tupla in cidades:    
    if tupla[4] == mes_pop[0]:        
        if tupla[5] > mes_pop[1]:            
            print(f'{tupla[2]}({tupla[0]}) tem {tupla[5]} habitantes e faz aniversário em {tupla[3]} de {mes.lower()}.')

def main():
    carrega_cidades()

if __name__=='__main__':
    main()
