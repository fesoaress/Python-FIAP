total_alunos = 50
media_par = 0
media_impar = 0
for impar in range(1, total_alunos, 2):
    print("Você está digitando as notas dos alunos ímpares")
    soma_impar: float = float(input(f"Insira a nota do aluno de número {impar}: "))

for par in range(2, total_alunos + 2, 2):
    print("Você está digitndo as notas dos alunos pares")
    soma_par: float = float(input(f"Insira a nota do aluno de número  {par}: "))

media_par = media_par + soma_par / 25
media_impar = media_impar + soma_impar / 25

print(f"A média da parte par foi: {media_par} ")
print(f"A média da parte impar foi: {media_impar} ")

if media_par > media_impar:
    print("A parte par teve média maior.")
else:
    print('A parte impar teve média maior.')