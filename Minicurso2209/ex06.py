n1 = input("Digite um numero: ")
n2 = input("Digite um segundo numero: ")

print "\nFun��es: "
print "\n1-) Soma"
print "\n2-) Subtra��o"
print "\n3-) Multiplica��o"
print "\n4-) Divis�o"
print "\n5-) Potencia quadrada"

menu = raw_input("\nQual fun��o deseja usar? ")

if(menu == "1"):
    res = n1 + n2
    print "\nO resultado da soma �: ",res
else:
    if(menu == "2"):
        res = n1 - n2
        print "\nO resultado da subtracao �: ",res
    else:
        if(menu == "3"):
            res = n1 * n2
            print "\nO resultado da multiplicacao �: ",res
        else:
            if(menu == "4"):
                res = n1 / n2
                print "\nO resultado da divis�o �: ",res
            else:
                if(menu == "5"):
                    res = pow(n1,n2)
                    print "\nO resultado da potencia de ",n1," elevado a ",n2," �: ",res
                else:
                    print "\nO codigo nao existe."


    
    
