class pokemon:
    def __init__(self,nome,tipo,saude,velocidade,nivel,golpe1,golpe2,golpe3,golpe4,HP_inimigo,conta_uso):
        self.nome=nome
        self.tipo=tipo
        self.saude=saude
        self.velocidade=velocidade
        self.nivel=nivel
        self.__golpe1=golpe1
        self.__golpe2=golpe2
        self.__golpe3=golpe3
        self.__golpe4=golpe4
        self.HP_inimigo=HP_inimigo
        self.conta_uso=conta_uso
    
    def atacar(self):
        golpe=int(input("Escolha seu ataque:\n1-{0}\n2-{1}\n3-{2}\n4-{3}\n".format(self.__golpe1,self.__golpe2,self.__golpe3,self.__golpe4)))
        if golpe==1:
            print("Você atacou usando:",self.__golpe1)
            self.HP_inimigo-=5
        elif golpe==2:
            print("Você atacou usando:",self.__golpe2)
            self.HP_inimigo-=5
        elif golpe==3:
            print("Você atacou usando:",self.__golpe3)
            self.HP_inimigo-=10
        elif golpe==4:
            print("Você atacou usando:",self.__golpe3)
            self.HP_inimigo-=15
    
    def rec_vida(self):
        if self.conta_uso<3:
           print("Recuperou 5 de vida!")
           self.saude+=5
           self.conta_uso+=1
        elif self.conta_uso>3:
            print("Você já usou a recuperação de vida 3 vezes! Limite atingido.")

    def mostrar_atributos(self):
        print("Seu pokemon se encontra com:")
        print("Nome:{0}\nNível:{1}\nTipo:{2}\nSaúde:{3}\nVelocidade:{4}".format(self.nome,self.nivel,self.tipo,self.saude,self.velocidade))
    
    def mostrar_vida_do_inimigo(self):
        print("Saude do pokemon inimigo:",self.HP_inimigo)
    
    def mostrar_vida_pokemon(self):
        print("Vida de {0} é igual a {1}".format(self.nome,self.saude))
    
    def muda_golpe(self):
        golpe=int(input("Digite o golpe que você deseja modificar(1,2,3,4): "))
        if golpe==1:
            golpe=input("Digite o novo golpe:")
            self.__golpe1=golpe
        elif golpe==2:
            golpe=input("Digite o novo golpe:")
            self.__golpe2=golpe
        elif golpe==3:
            golpe=input("Digite o novo golpe:")
            self.__golpe3=golpe
        elif golpe==4:
            golpe=input("Digite o novo golpe:")    
            self.__golpe4=golpe  