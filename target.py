indice = 13
soma = 0
k = 0

while k < indice:
     k = k + 1
     soma = soma + k

print(soma)
   
   #exercicio 1 soma 91


ex : 2
def pertence_sequencia_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    if b == numero:
        return True
    else:
        return False

numero_procurado = int(input("Informe um número: "))

if pertence_sequencia_fibonacci(numero_procurado):
    print(f"O número {numero_procurado} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_procurado} não pertence à sequência de Fibonacci.")



# ex3

#  a) 1, 3, 5, 7, 9:  logica soma 2
#  b) 2, 4, 8, 16, 32, 64, 128: potenciação de 2
#  c) 0, 1, 4, 9, 16, 25, 36, 49: Elevando os numeros ao quadrado
#  d) 4, 16, 36, 64, 128: potenciação de 4
#  e) 1, 1, 2, 3, 5, 8, 13: fibonacci 
#  f) 2, 10, 12, 16, 17, 18, 19, 21: soma alternada de 8,2 
    
# ex 4 
# liga o interruptor 1 e espere 10 min
# liga o segundo interruptor e vá a sala
# liga e desliga o interruptor 

# interruptor quente o primeiro
# a lampada acesa o segundo
# a lampada fria o 3



#ex 5

def inverter_string(string):
    string_invertida = ""
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida

minha_string = input("Digite uma string: ")
string_invertida = inverter_string(minha_string)
print("String original:", minha_string)
print("String invertida:", string_invertida)

