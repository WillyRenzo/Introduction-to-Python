n1 = input("Digite um numero: ")
n2 = input("Digite um segundo numero: ")

print "\nFunções: "
print "\n1-) Soma"
print "\n2-) Subtração"
print "\n3-) Multiplicação"
print "\n4-) Divisão"
print "\n5-) Potencia quadrada"

menu = raw_input("\nQual função deseja usar? ")

if(menu == "1"):
    res = n1 + n2
    print "\nO resultado da soma é: ",res
else:
    if(menu == "2"):
        res = n1 - n2
        print "\nO resultado da subtracao é: ",res
    else:
        if(menu == "3"):
            res = n1 * n2
            print "\nO resultado da multiplicacao é: ",res
        else:
            if(menu == "4"):
                res = n1 / n2
                print "\nO resultado da divisão é: ",res
            else:
                if(menu == "5"):
                    res = pow(n1,n2)
                    print "\nO resultado da potencia de ",n1," elevado a ",n2," é: ",res
                else:
                    print "\nO codigo nao existe."


    
    
