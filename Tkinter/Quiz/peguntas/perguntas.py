import random

perguntas = [{'pergunta':'Quem descobrio o brasil?', 'resposta': 2, 'Opções:':['colombo','cabral', 'vasco', 'dom joao']},
             {'pergunta':'Qual a capital do brasil?', 'resposta': 4, 'Opções:':['sao paulo', 'rio de janeiro', 'salvador', 'brasilia']}]


print('='*30)

perguntando = random.choice(perguntas)
print(perguntando.get('pergunta'))
    
print('='*30)
    
op = perguntando.get('Opções:')
for i in range(len(op)):
    print(i+1, end=' ')
    print(op[i])
    
print('='*30)

resposta = int(input('Resposta:    '))
if resposta == perguntando.get('resposta'):
    print()
    print('\033[7;34m','**\**||** Acertou **||**/**','\033[m')
else:
    print()
    print('\033[7;33m','**\**||** Errou **||**/**', '\033[m')
    
print('='*30)