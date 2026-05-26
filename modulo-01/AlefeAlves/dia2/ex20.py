C = float(input("Informe o seu capital:\n"))
i = float(input("Informe a taxa de juros ao mês (%):\n"))
t = int(input("Informe o período do investimento em meses:\n"))

M = C * (1 + (i/100) * t)

print(f"""
===== CALCULADORA DE INVESTIMENTOS SIMPLES =====
Capital       : R$ [{C}]
Taxa          : [{i} %]
Período       : R$ [{t}]
Juros totais  : R$ [{C * (i/100) * t}]
Montante Final: R$ [{M}]
=======================
""")