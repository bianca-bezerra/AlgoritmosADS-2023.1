
def main():
    #Entrada
    valor = float(input())

    notas = [100, 50, 20, 10, 5, 2]
    moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

    #Saída
    print('NOTAS:')
    for nota in notas:
     qtd_notas = int(valor/nota)
     print(f'{qtd_notas} nota(s) de R$ {nota:.2f}')
     valor -= qtd_notas * nota

    print('MOEDAS:')
    for moeda in moedas:
     valor = round(valor, 2)
     qtd_moedas = int(valor/moeda)
     print(f'{qtd_moedas} moeda(s) de R$ {moeda:.2f}')
     valor -= qtd_moedas * moeda

main()
