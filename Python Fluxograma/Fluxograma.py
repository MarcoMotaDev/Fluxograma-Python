# Calculadora de média para aprovação

# Entrada das notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Cálculo da média
media = (nota1 + nota2) / 2

# Verificação da situação do aluno
if media >= 7:
    print(f"Média: {media:.2f} - Aprovado")
else:
    print(f"Média: {media:.2f} - Reprovado")
