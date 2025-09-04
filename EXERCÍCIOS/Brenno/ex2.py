class Relogio:
    def __init__(self, horas, minutos):
        self.horas = horas
        self.minutos = minutos
    def __str__(self):
        return f"{self.horas:02}:{self.minutos:02}" 

relogio = Relogio(5, 35)
print(relogio) 
