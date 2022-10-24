assinatura_cliente = input("Insira o número correspondente a assinatura: 1- Basic, 2- Silver, 3- Gold, 4- Platinum " )
faturamento_anual = float(input("Insira o faturamento anual "))

if assinatura_cliente.upper() == "1":
    valor_pagamento = faturamento_anual * 0.3
elif assinatura_cliente.upper() == "2":
    valor_pagamento = faturamento_anual * 0.2
elif assinatura_cliente.upper() == "3":
    valor_pagamento = faturamento_anual * 0.1
elif assinatura_cliente.upper() == "4":
    valor_pagamento = faturamento_anual * 0.05

print(f"O valor do bônus é {valor_pagamento}")
