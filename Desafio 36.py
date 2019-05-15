imovel = float(input('Informe o valor do imóvel: R$'))
salario = float(input('Informe seu salário: R$'))
ano = int(input('Informe em quantos anos deseja financiar o imóvel:'))
vmes = imovel / (ano * 12)
limite = salario * 30 / 100
if vmes <= limite:
    print('Emprestimo \033[1;7;32mAPROVADO!\033[m \nMesalidade: R$\033[1;32m{:.2f}\033[m \n30% do salário: R$\033[1;32m{:.2f}\033[m'.format(vmes, limite))
elif vmes >= limite:
    print('Emprestimo \033[1;7;31mNEGADO!\033[m \nMensalidade: R$\033[1;31m{:.2f}\033[m \n30% do salário: R$\033[1;31m{:.2f}\033[m'.format(vmes, limite))
    
