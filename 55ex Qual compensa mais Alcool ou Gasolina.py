
'''55. Faça uma função que receba por parâmetro o valor de etanol e gasolina. Retorne 1 para 
abastecer com gasolina e 0 para bastecer com etanol. Trate este retorno de modo que na 
função principal apareça: Abasteça com Etanol ou Abasteça com Gasolina.'''


preco_alcool = float(input("Preço do álcool:R$ ")) 
preco_gasolina = float(input("Preço da gasolina:R$ ")) 

resultado = preco_alcool/preco_gasolina
if resultado <= 0.74: 
    print("\nCOMPENSA MAIS COLOCAR ALCOOL A:R$%.2f\n" % preco_alcool) 
else:  
    print("\nCOMPENSA MAIS COLOCAR GASOLINA A:R$%.2f\n" % preco_gasolina) 