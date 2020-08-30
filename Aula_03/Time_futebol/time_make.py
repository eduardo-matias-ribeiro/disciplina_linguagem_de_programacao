from time_class import Time
import asyncio

time1 = Time('Barcelona', ['Messi','Frenkie','Marc-Andre','Dani Morer', 'Jorge Cuenca'],'Ronald Koeman')
time2 = Time('Real Madrid', ['Cristiano Ronaldo','Diego Altube','Marcelo','Nacho', 'Mariano'],'Zinédine Zidane')

ganhador = asyncio.run(time1.jogar(time2))
if ganhador == time1.nomeTime:
    print("Melhor jogador da partida:")
    time1.premiarJogador()
elif ganhador == time2.nomeTime:
    print("Melhor jogador da partida:")
    time2.premiarJogador()
else:
    print("Melhores jogadores da partida:")
    time1.premiarJogador()
    time2.premiarJogador()