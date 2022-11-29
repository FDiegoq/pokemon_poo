from pokemon import pokemon
class miticos(pokemon):
    def __init__(self,nome,tipo,saude,velocidade,nivel,golpe1,golpe2,golpe3,golpe4,HP_inimigo,conta_uso,escudo):
        pokemon.__init__(self,nome,tipo,saude,velocidade,nivel,golpe1,golpe2,golpe3,golpe4,HP_inimigo,conta_uso)
        self.escudo=escudo
    
    def rec_vida(self):
        print("Você recuperou vida!")
        self.saude+=10
    
    def defender(self):
        print("Você evitou um ataque!")
    
    def mostrar_atributos(self):
        print("Nome:{0}\nNível:{1}\nTipo:{2}\nSaúde:{3}\nVelocidade:{4}".format(self.nome,self.nivel,self.tipo,self.saude+self.escudo,self.velocidade))