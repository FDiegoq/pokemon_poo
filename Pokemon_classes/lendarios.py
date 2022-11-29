from pokemon import pokemon
class lendarios(pokemon):
    def __init__(self,nome,tipo,saude,velocidade,nivel,golpe1,golpe2,golpe3,golpe4,HP_inimigo,conta_uso,tipo_2):
        self.tipo_2=tipo_2
        pokemon.__init__(self,nome,tipo,saude,velocidade,nivel,golpe1,golpe2,golpe3,golpe4,HP_inimigo,conta_uso)
    
    def rec_vida(self):
        print("Recuperou vida!")
        self.saude+=15
    
    def aumentar_velocidade(self):
        print("Você aumentou sua velocidade!")
        self.velocidade+=15
    
    def mostrar_atributos(self):
        print("Seu pokemon se encontra com:")
        print("Nome:{0}\nNível:{1}\nTipo:{2} e {3}\nSaúde:{4}\nVelocidade:{5}".format(self.nome,self.nivel,self.tipo,self.tipo_2,self.saude,self.velocidade))

    
