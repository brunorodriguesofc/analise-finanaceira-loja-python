# ANÁLISE FINCEIRA SIMPLES DE UMA LOJA 

# Dados iniciais

faturamento = 2500
custo = 1200
novas_vendas = 1500

#Parte 1 — Atualização do faturamento
#Atualize o faturamento somando as novas vendas.
faturamento = faturamento + novas_vendas
#Depois calcule:
#imposto = 12% do faturamento
imposto = 0.12 * faturamento


#Parte 2 — Cálculo do lucro

lucro = faturamento - custo - imposto

#Mostre:

#faturamento
#custo
#imposto
#lucro
#Parte 3 — Margem de lucro

print(f"Faturamento: R${faturamento:,.2f}")
print(f"Custo: R${custo:,.2f}")
print(f"Imposto: R${imposto:,.2f}")
print(f"Lucro: R${lucro:,.2f}")

#calcule:

#Margem do Lucro
margem_lucro = lucro / faturamento

#Mostre a margem.
print(f"Margem de lucro: {margem_lucro * 100:,.2f}%")


#Parte 4 — Tipos de dados

#Crie duas variáveis: mensagem & teve lucro
#mensagem → texto com o faturamento final
#teve_lucro → boolean

mensagem = f"A loja faturou R${faturamento:,.2f}"
teve_lucro = lucro>0
print(f"Teve lucro ? {teve_lucro}")

#Parte 5 — Conversão de meses

#A loja está aberta há: 145 meses

meses_total = 145

#Calcule:

#anos completos
#meses restantes

#Usando:
#//
#%

anos_completos = meses_total // 12
meses_restantes = meses_total % 12


print(f"A empresa tem {anos_completos} anos e {meses_restantes} meses.")
