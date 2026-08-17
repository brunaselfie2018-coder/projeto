#calcule o IMC de uma pessoa e mostre o status
peso = float(input('Qual é o seu peso?'))
altura = float(input('Qual é a sua altura?'))

imc = peso / (altura ** 2 )
print (f'O IMC dessa pessoa é de {imc}')
if imc < 18.5:
    print ('Você está ABAIXO DO PESO NORMAL')
elif 18.5 <= imc <25:
    print ('SEU PESO ESTÁ NORMAL')
elif 25 <= imc <30:
    print('SOBREPESO')
elif 30 <= imc < 40:
    print ('VOCE ESTÁ OBESO!')
elif imc >=40:
    print ('VOCE ESTA EM OBESIDADE MÓRBIDA')