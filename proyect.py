class appfit:
  def __init__(self, peso, altura, edad):
    self.peso = peso
    self.altura = altura
    self.edad = edad
    self.fitapagado = False
usuario = appfit("50kg", "1.60", "15")
print(type(usuario))

print(usuario.peso, usuario.altura, usuario.edad)
