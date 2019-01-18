import eel

import dao.PersonaD
import controlador.PersonaC as personaC

eel.init('web')


@eel.expose
def RegPerr(nombre, apellido, dni, email):
    persona = personaC.personaC()
    persona.variablesM(nombre, apellido, dni, email)
    if persona.RegistrarPer():
        eel.AlertaJs("Registro Exitoso")
    else:
        eel.AlertaJs("Error RegPer")

@eel.expose
def ShowPer():
    persona = dao.PersonaD.PersonaD()
    persona.ShowPer()


@eel.expose
def llenar(x):
    persona = dao.PersonaD.PersonaD
    persona.ShowPer1(x)

@eel.expose
def ElimPer(codigo):
    persona = dao.PersonaD.PersonaD
    if (persona.ElimPer(codigo)):
        pass


eel.start('index.html', block=True)
