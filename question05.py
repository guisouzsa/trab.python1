hora = int(input("Que horas são?"))
if 0 <= hora <12:
    print("agora é manhã!")
elif 12 <= hora <18: 
    print("Agora é tarde!")
else:
    print("Agora é noite!")