nome = input("Digite o nome do aluno: ")
diciplina = input("Qual o nome da diciplina?")
not1 = int(input("Qual foi sua primeira nota nesta diciplina?"))
not2 = int(input("Qual a sua segunda nota nesta diciplina"))
média = (not1+not2) / 2
if média >= 6:
    situação = "aprovado"
else:
    situação = "reprovado"
print (f'{nome} esta {situação} na diciplina de {diciplina}')