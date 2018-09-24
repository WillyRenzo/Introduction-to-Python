op = '0'

print "Lista de Opções"
print "\n1-)Inserir"
print "\n2-)Listar"
menu = input("\nDigite uma opção: ")
if(menu == 1):
    op = "1"
    file = open("agenda.txt","a")
    nome = raw_input("Informe o nome: ")
    celular = raw_input("Informe o telefone: ")
    email = raw_input("Informe o email: ")
    ano = raw_input("Informe o ano de nascimento: ")
    idade = 2018 - int(ano);

    file.write("Nome: "+nome+"\n")
    file.write("Celular: "+celular+"\n")
    file.write("Email: "+email+"\n")
    file.write("Idade: "+str(idade)+"\n")
    file.write("---------------------------------------------")
    file.close()
    op = "0"
else:
    if(menu == 2):
        op = "1"
        file = open("agenda.txt","a")
        with open("agenda.txt") as agenda:
           for contato in agenda:
                print contato
        file.close()
    else:
        print "O codigo nao existe"
