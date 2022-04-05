'''
Está sendo representado um campeonato de ludo, em que cada jogador possui 
nome, pontuação, ppc(peões próprios capturados) que representa o número 
de peões do próprio jogador que foram capturados, pac(peôes adversários 
capturados) que representa o número de vezes que o jogador capturou um 
peão adversário e número de vitórias e derrotas, tal que é considerado 
vitória quando o jogador termina em 1º lugar e derrota quando termina em
último, com partidas de 4 jogadores
'''
class jogador:
    def __init__(self,nome,pontuação,ppc,pac,vitórias,derrotas):
        self.nome=nome
        self.pts=pontuação
        self.ppc=ppc
        self.pac=pac
        self.vtr=vitórias
        self.derr=derrotas
    def terminar_partida(self,posição):
        if(posição==1):
            self.pts+=5
            self.vtr+=1
        elif(posição==2):
            self.pts+=3
        elif(posição==3):
            self.pts+=1
        else:
            self.derr+=1
        #nota-se que a quarta posição em uma partida não dá pontos
    def foi_capturado(self):
        self.ppc+=1
    def capturou(self):
        self.pac+=1
    def __gt__(self,jogador2):
        return(self.pts>jogador2.pts)
    def __lt__(self,jogador2):
        return(self.pts<jogador2.pts)
    def __eq__(self,jogador2):
        return(self.pts==jogador2.pts)
    def __ne__(self,jogador2):
        return(self.pts!=jogador2.pts)
    def __repr__(self):
        r='{} tem {} pontos, {} peões capturados, {} capturas adversárias, {} vitórias e {} derrotas.\n'.format(self.nome,self.pts,self.ppc,self.pac,self.vtr,self.derr)
        return r
    def __add__(self,jogador2):
        r=self.pts+jogador2.pts
        return r
    def __sub__(self,jogador2):
        r=self.pts-jogador2.pts
        return r
j1=jogador('Pedro',13,15,14,3,2)
j2=jogador('Maria',24,16,11,4,1)
j3=jogador('João',23,14,18,5,2)
j4=jogador('Paula',10,16,10,1,3)
print(j1)
lista=[j1,j2,j3,j4]
lista.sort()
print(lista)
print('A soma dos pontos de',j1.nome,'e',j2.nome,'é',j1+j2)
print('A diferença entre os pontos de',j3.nome,'e',j4.nome,'é',j3-j4)