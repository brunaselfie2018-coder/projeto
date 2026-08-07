lista= []
quant = 0

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])

    sn = str(input('Quer continuar? S/N:  ')).lower().strip()
    if sn not in 's':
        break
print('\33[36m-='*15)
print(f'\33[33mN° \33[36m/\33[34  NOME \33[36m/\33[32m {"MÉDIA":>10}')
print('\33[36m-='*15)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' *35)
    opc = int(input('Mostrar notas de qual aluno? (999 Encerra):'))
    if opc == 999:
        print ('FINALIZANDO...')
        break
    if opc <= len(lista)-1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')
print('\33[34;42m SISTEMA FINALIZADO\33[m')