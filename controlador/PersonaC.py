import modelo.PersonaM as persona
from dao import PersonaD as dao


class personaC(persona.PersonaM):

    def RegistrarPer(self):
        if dao.PersonaD.RegPer(self):
            return True
        else:
            return False

    def variablesM(self, nombre, apellido, dni, email):
        persona.PersonaM.setNomPer(self, nombre)
        persona.PersonaM.setApePer(self, apellido)
        persona.PersonaM.setDniPer(self, dni)
        persona.PersonaM.setEmailPer(self, email)

    def listarPersonas(self):
        dao.PersonaD.showPer(self)

    def listarPersonasPorCod(self,codigo):
        dao.PersonaD.ShowPer1(self,codigo)