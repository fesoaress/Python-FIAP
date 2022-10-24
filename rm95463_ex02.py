alunos = int(input ("Quantidade de alunos na turma "))
segunda = 0
terca = 0
quarta = 0
quinta = 0
sexta = 0
votacao = 0

while votacao < alunos:
    voto = input("Qual dia da semana você prefere? ")
    if voto == "segunda":
        segunda = segunda + 1
    elif voto == "terca":
        terca = terca + 1
    elif voto == "quarta":
        quarta = quarta + 1
    elif voto == "quinta":
        quinta = quinta + 1
    elif voto == "sexta":
        sexta = sexta + 1
    votacao = votacao + 1

print("Segunda teve ", segunda, "votos")
print("Terça teve ", terca, "votos")
print("Quarta teve ", quarta, "votos")
print("Quinta teve ", quinta, "votos")
print("Sexta teve ", sexta, "votos")


