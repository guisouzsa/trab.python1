nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
if idade >= 16:
    print(f'{nome}, você pode emitir o seu título de eleitor!')
else:
    print(f'{nome}, você ainda não pode emitir o título de eleitor.')