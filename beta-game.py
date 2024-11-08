
class CampoMinado():
  def __init__(self, size):
    self.size = size
    self.matriz = []
    self.posicoes_minas = []
    self.porcentagem_minas = 45

    self.inicializar_matriz()

  def inicializar_matriz(self):
    self.matriz = []

    for x in range(self.size):
      lista = []

      for y in range(self.size):
        lista.append({
          "pos_x": x,
          "pos_y": y,
          "aberto": False,
          "marcado": False,
          "minado": False
        })

      self.matriz.append(lista)



jogo = CampoMinado(5)

print(jogo.matriz)