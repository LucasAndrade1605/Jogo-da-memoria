import random, os, time

class Campo:
    
    def __init__(self, campo, print):
        
        self.ValoresCampo = campo
        self.CampoPrint = print
        self.GerarValoresCampo()
    
    #Funcao para criar a matriz com seus pares
    def GerarValoresCampo(self):
    
        #Colocando valores na matriz. Os pares serao de 1 a 50, sendo o primeiro par 1 e 1, segundo 2 e 2 etc...


        listaValores = list(range(1,51)) * 2

        for l in range (0,10):
            for c in range(0,10):
                aux = random.choice(listaValores)
                self.ValoresCampo[l][c] = aux
                listaValores.remove(aux)

    #Funcao para mostrar o campo
    def MostrarCampo(self):
        coluna = 20
        linha = 22
        c = 0
        l = 0

        valoresCamp = self.CampoPrint

        for cont in range(linha):
            campo = ''
            c= 0
            for cont2 in range(coluna):
            

                if cont>0 and cont % 2 == 0:
                    if cont2 % 2 == 0:
                        campo += '    |    '
                    if cont2 % 2 ==1:
                        campo += str(valoresCamp[l][c])
                        c+=1
                        if(c==10):
                            l+=1
                    if cont2 == 19:
                        campo += '    |'
            
                  
            print(campo)
    
        
    #Metodos gets e sets
    def getCampo(self):
        return self.ValoresCampo
    
    def getCampoPrint(self):
        return self.CampoPrint
    
    def setCampo(self, valoresCampo):
        self.ValoresCampo = valoresCampo
    
    def setCampoPrint(self, campoPrint):
        self.CampoPrint = campoPrint

class Jogador:
    def __init__(self, vidas, acertosConsecutivos):
        self.Vidas = vidas
        self.AcertosConsecutivos = acertosConsecutivos

    def getVidas(self):
        return self.Vidas
    
    def getAcertosConsecutivos(self):
        return self.AcertosConsecutivos
    
    def setVidas(self, vidas):
        self.Vidas = vidas

    def setAcertosConsecutivos(self, acertosConsecutivos):
        self.AcertosConsecutivos = acertosConsecutivos

#Funcao para verificar se o jogador acertou ou nao um par
def MostrarValores(carta1,carta2,campoimport,jogador):
    campo = campoimport.getCampoPrint()
    valoresCampo = campoimport.getCampo()
    #if veridica se o jogador ja nao acertou essas posicoes
    if (campo[carta1[0]-1][carta1[1]-1] == "*") and (campo[carta2[0]-1][carta2[1]-1] == "*"):
        #if verifica se o jogador acertou o par
        if valoresCampo[carta1[0]-1][carta1[1]-1] == valoresCampo[carta2[0]-1][carta2[1]-1]:
            campo[carta1[0]-1][carta1[1]-1] = valoresCampo[carta1[0]-1][carta1[1]-1]
            campo[carta2[0]-1][carta2[1]-1] = valoresCampo[carta2[0]-1][carta2[1]-1]
            campoimport.setCampoPrint(campo)

            print("\n           Voce acertou um par!!!")

            #Verifica os acertos consecutivos do jogador
            if jogador.getAcertosConsecutivos() == 2:
                print("\nPARABENS VOCE ACERTOU 3 VEZES CONSECUTIVAS. GANHOU UMA VIDA")
                jogador.setAcertosConsecutivos(0)
                jogador.setVidas(jogador.getVidas()+1)
            else:
                jogador.setAcertosConsecutivos(jogador.getAcertosConsecutivos()+1)

        #Caso o jogador nao tenha acertado um par
        else:
            jogador.setVidas(jogador.getVidas()-1)
            jogador.setAcertosConsecutivos(0)

            campo[carta1[0]-1][carta1[1]-1] = valoresCampo[carta1[0]-1][carta1[1]-1]
            campo[carta2[0]-1][carta2[1]-1] = valoresCampo[carta2[0]-1][carta2[1]-1]
            campoimport.setCampoPrint(campo)
            print(campoimport.MostrarCampo())

            time.sleep(5)
            os.system("cls") or None
            campo[carta1[0]-1][carta1[1]-1] = "*"
            campo[carta2[0]-1][carta2[1]-1] = "*"
            campoimport.setCampoPrint(campo)

            print("\n           voce nao acertou!!! Perdeu uma vida")
    else:
        print("Voce ja informou essa coordenada")



#Funcao para reber as coodenadas do jogador
def ReceberCoodenadas(campo,jogador):

    carta1 = [0,0]
    carta2 = [0,0]

    while True:

        carta1[0] = int(input("\n Escolha a coordenada da primeira carta - Primeiro valor para linha e segundo para coluna(valores entre 1 e 10): "))
        carta1[1] = int(input())

        carta2[0] = int(input("\n Escolha a coordenada da segunda carta - Primeiro valor para linha e segundo para coluna(valores entre 1 e 10): "))
        carta2[1] = int(input())

        if (carta1[0] != carta2[0]) or (carta1[1] != carta2[1]):
            break
        print("Informe 2 coordenas diferentes!!!")
        
            

    MostrarValores(carta1,carta2,campo,jogador)

#Inicio do jogo
print("\n\n\nBem vindo ao jogo da tortura :)")

#Instanciando a class Jogador
jogador = Jogador(5,0)


#Instanciando a class Campo
aux = [[0] * 10 for cont in range(10)]
aux2 = [["*"]*10 for a in range(10)]
campo = Campo(aux,aux2)


while jogador.Vidas > 0:

    print(f"\nVIDAS: {jogador.getVidas()}")

    #Esses comandos mostra os valores do campo, remover comentario para aparecer. Vai facilitar na correcao S2
    """
    print("\nEsses sao os valores dos campos")
    for l in range(10):
        print((campo.getCampo())[l])
    campo.setCampoPrint(campo.getCampo())
    """
            
    campo.MostrarCampo()
    win =0

    #Verifica se o campo nao tem nenhuma carta para baixo
    for l in range(10):
        for c in range(10):

            if((campo.getCampoPrint())[l][c] == '*'):
                win += 1
                break
        break
    #Verifica se o jogador ganhou
    if win == 0:
        campo.MostrarCampo()
        print("\nPARABENS VOCE GANHOU!!!\n")
        break

    coordenadasCartas = ReceberCoodenadas(campo,jogador)

   

if(jogador.Vidas == 0):
    campo.MostrarCampo()
    print("FIM DE JOGO:\nVOCE PERDEU!!!\n")

