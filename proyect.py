def usuario(peso, altura, edad):
  self.peso=peso
  self.altura=altura 
  self.edad=edad
def rutina(tipo_problema, tipo_ejercicio, duración_ejercicio):
  self.tipo_problema=tipo_problema
  self.tipo_ejercicio=tipo_ejercicio
  self.duración_ejercicio=duración_ejercicio
def consejos(tipo_problema, porcentaje_grasa):
  self.porcentaje_grasa=porcentaje_grasa
def menufit(recetas_faciles, recetas_elaboradas, tipo_problema):
  self.recetas_elaboradas=recetas_elaboradas
  self.recetas_faciles=recetas_faciles
  
import re
def get_respuesta(user_input):
  split_mensaje = re.split(r'\s|[,:;.-_?!]\s+', user_input.lower())
  respuesta = check_all_messages(split_mensaje)
  return respuesta

def mensaje_probabilidad(user_message, palabras_reconocidas, respuesta_sencilla = False, palabras_requeridas = []):
  mensaje_certainty = 0 
  palabras_req = True

  for palabra in user_message:
    if palabra in palabras_reconocidas:
      mensaje_certainty += 1
  porcentaje = float(mensaje_certainty)/float(len(palabras_reconocidas))

  for palabra in palabras_requeridas:
    if palabra not in user_message:
      palabras_req = False
      break
  if palabras_req or respuesta_sencilla:
    return int(porcentaje*100)
  else: 
    return 0
  def check_all_messages(message):
    masalta_prob = {}
    def respuesta(bot_respuesta, lista_de_palabras, respuesta_sencilla):
      nonlocal masalta_prob
      masalta_prob[bot_respuesta]=mensaje_probabilidad(message, lista_de_palabras, respuesta_sencilla, palabras_req)
