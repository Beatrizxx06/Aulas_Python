# Faça um programa que exige quanto você ganha por horas e quanto vc trabalha no mês
print('-=' *30)
# Faça um programa que exige quanto você ganha por horas e quanto vc trabalha no mês
print('-=' *30)
print('Cáculos de horas trabalhadas')
print('-=' *30)
valor_hora =  float(input(' Informe o valor das horas trabaladas R$:'))
horas_trabalhadas = float(input('Informe, quantas horas foram trabalhadas'))
sálario =  valor_hora*horas_trabalhadas
if __name__ == '__main__':
if __name__ == '__main__'                                                                    #Esta condição verifica se a variável __name__
  print(f'O sálario, conforme as informações informadas, é de R${sálario:.2f}')              #tem o valor __main__. Se sim, o código dentro
                                                                                             #do bloco if é executado. Se não (por exemplo,
                                                                                             #se o script for importado como um módulo), o código
                                                                                             #dentro do bloco if não é executado
