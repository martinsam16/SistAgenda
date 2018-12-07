import eel
import personaD
import personaC

eel.init('web')

@eel.expose
def RegPer(nombre, apellido, dni):
    persona = personaC.personaC()
    persona.variablesM(nombre, apellido,dni)
    if (persona.RegistrarPer()):
        pass
    else:
        eel.AlertaJs("Error RegPer")




@eel.expose
def ShowPer():
    persona = personaD.PersonaD()
    persona.ShowPer()
    
#eel.say_hello_js('connectedf!')   # Llama funcion js

eel.start('index.htm', size=(800, 800))