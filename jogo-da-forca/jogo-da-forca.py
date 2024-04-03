import random 
import datetime

def escolhePala(arquivo):
    cont = 0
    PalavrasList = []
    with open(arquivo, "r") as palavras:
        for linha in palavras:
            PalavrasList.append(linha)
            cont +=1
        n = random.randint(0,cont-1)
    return PalavrasList[n] 

def boneco(erros):
    if erros == 1:
        print(" |------")
        print(" |     O")
        print(" |       ")
        print(" |       ")
        print(" |___-----__")
    elif erros ==2:
        print(" |------")
        print(" |     O")
        print(" |     | ")
        print(" |        ")
        print(" |___-----__")
    elif erro ==3:
        print(" |------")
        print(" |     O")
        print(" |   / |  ")
        print(" |    ")
        print(" |___-----__")
    elif erro ==4:
        print(" |------")
        print(" |     O")
        print(" |   / | \\ ")
        print(" |    ")
        print(" |___-----__")
    elif erro ==5:
        print(" |------")
        print(" |     O")
        print(" |   / | \\ ")
        print(" |    | ")
        print(" |___-----__")
    elif erro ==6:
        print(" |------")
        print(" |     O")
        print(" |   / | \\ ")
        print(" |    | |")
        print(" |___-----__")
        print("vc foi enforcado ")
        return "voce foi enforcado"
    
def salvaJogador(nome,erro, acerto):
    dataAtual = datetime.date.today()
    with open ("topjogadores.txt", "a") as top:
        top.write("jogador,erros, acerto ")
        top.write(f'Nome do Jogador:{nome} Erro:{erro} Acertos:{acerto} Data{dataAtual}')    

 

palavra = escolhePala("palavras.txt")
xx = []
for t in palavra.strip():
    xx.append("x")
print (xx)  
erro = 0
while True: 
    letra = input("Fale uma letra")

    if letra not in palavra:
            print("vc errou ")
            erro +=1
            en = boneco(erro)
            if en == "voce foi enforcado":
                break
    else: 
        cont = 0       
        for t in palavra:
            
            if letra == t:
                xx[cont] = letra
                print("vc acertou")
            cont +=1         
        
    print(xx) 


        




