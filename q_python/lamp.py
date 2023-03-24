# Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu
# construtor, True se a lâmpada estiver ligada, False caso esteja desligada.
# A classe Lampada possuí os seguintes métodos:

# liga(): muda o estado da lâmpada para ligada

# desliga(): muda o estado da lâmpada para desligada

# esta_ligada(): retorna true se a lâmpada estiver ligada, falso caso contrário


class Lamp:
    def __init__(self, on) -> None:
        self.status = on

    def on(self):
        self.status = True

    def off(self):
        self.status = False

    def is_on(self):
        return self.status
