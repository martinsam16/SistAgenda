import eel

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
    persona = personaC.personaC()
    persona.listarPersonas()


@eel.expose
def llenar(x):
    persona = personaC.personaC()
    persona.listarPersonasPorCod(x)

@eel.expose
def ElimPer(codigo):
    persona = personaC.personaC()
    persona.eliminarPersona(codigo)


eel.start('index.html', block=True)
