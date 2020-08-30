from Aviao_class import Aviao
import asyncio

aviao1 = Aviao('Boing777', 'PYTHON', 2020, 'TAM')
aviao2 = Aviao('TitanicAereo', 'NODE-JS', 2020, 'GOL')

asyncio.run(aviao1.decolar())
asyncio.run(aviao1.pousar())
asyncio.run(aviao2.decolar())
asyncio.run(aviao2.pousar())