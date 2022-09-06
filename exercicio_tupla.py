#Criar um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
#Seu programa deverá ler um numero pelo teclado entra 0 e 20 e mostra-lo por extenso.

tupla = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
        'treze', 'cartoze', 'quinze', 'deseseis', 'desessete', 'dezoito','dezenove', 'vinte')


numero = int(input('Digite um número de 0 a 20: '))

if numero in tupla:
    print(tupla[-1])
