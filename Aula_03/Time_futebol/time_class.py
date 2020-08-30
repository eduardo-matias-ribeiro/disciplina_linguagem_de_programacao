import random
import asyncio
class Time():
    def __init__(self,nomeTime, jogadores, tecnico):
        self.nomeTime = nomeTime
        self.jogadores = jogadores
        self.tecnico = tecnico
    async def jogar(self,adversario):
        placar1 = random.randint(0,5)
        placar2 = random.randint(0,5)
        print(self.nomeTime+" x "+ adversario.nomeTime)
        await asyncio.sleep(3)
        print("Jogo rolando...")
        print(str(placar1)+" x "+str(placar2))
        await asyncio.sleep(3)
        print("Jogo finalizado")
        if placar1 == placar2:
            print("Empatou!")
        elif placar1 > placar2:
            print(self.nomeTime+" ganhou!")
            return self.nomeTime
        else:
            print(adversario.nomeTime+" ganhou!")
            return adversario.nomeTime
    def premiarJogador(self):
        print(random.choice(self.jogadores))
    