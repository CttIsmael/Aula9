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

habt = ()
popl = int(input())

habt = (popl,)

print(f'CIDADES COM MAIS DE {popl} HABITANTES: ')    
for tupla in cidades:
    if tupla[5] > habt[0]:
        print(f'IBGE: {tupla[1]} - {tupla[2]}({tupla[0]}) - POPULAÇÃO: {tupla[5]}')

def main():
    carrega_cidades()

if __name__=='__main__':
    main()
