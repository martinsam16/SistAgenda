from personaM import PersonaM
from personaD import PersonaD as dao

class personaC(PersonaM):

    def RegistrarPer(self):
        if (dao.RegPer(self)):
            return True
        else:
            return False

    def variablesM(self,nombre,apellido,dni,email):
        PersonaM.setNomPer(self, nombre )
        PersonaM.setApePer(self,apellido )
        PersonaM.setDniPer(self,dni )
        PersonaM.setEmailPer(self,email)

    
