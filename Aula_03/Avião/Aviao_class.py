import asyncio
class Aviao():
    def __init__(self,nomeAviao, modeloAviao,ano_modeloAviao, empresa):
        self.nomeAviao = nomeAviao
        self.modelo = modeloAviao
        self.ano_modelo = ano_modeloAviao
        self.empresa = empresa  
    async def decolar(self):
        print(self.nomeAviao+" pegou vôo!")
        await asyncio.sleep(3)
        print(self.nomeAviao+" está voando")
    async def pousar(self):
        print(self.nomeAviao+" está pousando...")
        await asyncio.sleep(3)
        print(self.nomeAviao+" pousou")