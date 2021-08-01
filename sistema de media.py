 # Pedindo as notas
port = float( input("Digite a nota de Português, por favor: ") )
ingles = float( input("digita  a nota de Inglês: ") )
fisica= float( input("digite a nota de Fisica:"))
matematica= float( input("digite sua nota de Matematica:"))
historia= float( input("digite a nota de historia:"))
filosofia= float( input("digite a nota de filosofia:"))
# Cálculo da média
media=port+ingles+fisica+matematica+historia+filosofia/6

print("Sua media %.2f ",media)

if media>=6:
    print("ALUNO APROVADO")
else:
    print("ALUNO REPROVADO")

print("programa executado com sucesso")    


    



