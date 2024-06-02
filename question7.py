nome_alu = input("Qual seu nome?")
diciplina = input("Qual o nome da diciplina?")
not1 = int(input("Qual foi sua primeira nota nesta diciplina?"))
not2 = int(input("Qual a sua segunda nota nesta diciplina"))
média = (not1+not2) / 2
if média >= 6:
    situação = "aprovado"
if média <6:
    situação = "reprovado"
print (f'{nome_alu} esta {situação} na diciplina de {diciplina}')