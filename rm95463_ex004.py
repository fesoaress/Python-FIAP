n = int(input('Insira o número dos minutos atuais: '))
c = 0
f = 1
for c in range(1, n):
    f *= n
    n -= 1
print(f'Sua senha é: LIBERDADE{f}')