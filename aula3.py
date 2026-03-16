nota = int(input("digite a nota: "))

if nota >= 7: 
    print("aprovado")
elif nota >= 5:
    print('recuperação')
else: 
    print("reprovado")

idade = int(input("digite sua idade: "))

if idade >= 18:
    print("voce é maior de idade")
else:
    print('voce é menor de idade')

numero = 10

if numero == 10:
    print('o numero é 10')

numero2 = int(input("digite um numero"))

if numero2 >= 0:
    print("numnero positivo")
else:
    print('numero negativo')

nota2 = float(input("digite a nota do aluno"))

if nota2 >= 6:
    print("aluno aprovado")
else:
    print('aluno reprovado')

numero3 = int(input("digite um numero"))

if numero3 % 2 == 0:
    print('o número é par')
else:
    print('o numero é impar')

idade2 =int(input("digite sua idade"))

if idade2 < 12:
    print("criuança")
elif idade2 < 18:
    print('adolecente')
elif idade < 60: 
    print('adulto')
else:
    print("idoso")

dia = int(input("digite um numero de 1 a 3"))

if dia == 1:
    print('segunda-feira')
elif dia == 2:
    print('terça-feira')
elif dia == 3:
    print('quarta-feira')
else: 
    print("dia invalido")

nota3 = float(input("digite a nota do aluno"))

if nota3 >= 9:
    print("perfeito")
elif nota >= 7:
    print('bom')
elif nota >= 6:
    print("regular")
else:
    print("péssimo")

estacao = int(input('digite um numero de 1 a 4 referente a esdtaçlão do ano: '))

if estecao == 1:
    print('primavera')
elif estacao == 2:
    print("verão")
elif estacao == 3:
    print("outono")
elif estacao == 4:
    print('inverno')
else:
    print("numero invalido")