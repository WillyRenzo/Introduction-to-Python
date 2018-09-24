fp = open('C:\Users\Cliente\Desktop\Willy\Python\dados.txt')
lines = fp.read().split("\n")
print(lines)
fp.close()

print "\nOutro metodo"

with open('C:\Users\Cliente\Desktop\Willy\Python\dados.txt') as fp:
    for line in fp:
        print "\n",line
