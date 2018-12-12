import conexionD as dao
from personaM import PersonaM
import eel


class PersonaD(PersonaM):

    def __init__(self):
        super().__init__()
        self.__miConexion = dao.conexionD()

    def RegPer(self):
        try:
            self.__miConexion = dao.conexionD()
            _, self.__cursor, self.__cnn = self.__miConexion.conectar()
            if (self.__miConexion.estado()):
                sql = ("INSERT INTO PERSONA"
                "(NOMPER, APEPER, DNIPER, EMAILPER)"
                "VALUES (%s, %s , %s , %s)")
                val = (PersonaM.getNomPer(self), PersonaM.getApePer(self), PersonaM.getDniPer(self), PersonaM.getEmailPer(self))
                self.__cursor.execute(sql, val)
                self.__cnn.commit()

                self.__cnn.close()
                self.__cursor.close()
                self.__miConexion.desconectar()
                print("Registro exitoso")
                return True
            else:
                print("No pudiste con ella :,v")
                return False
        except Exception as e:
            print("ErrorRegPErpersonaD")
            eel.AlertaJs (str(e))
            return False

    def ShowPer(self):
        try:
            _, self.__cursor, self.__cnn = self.__miConexion.conectar()
            if (self.__miConexion.estado()):
                sql = ("SELECT codper, nomper, apeper, dniper, emailper FROM PERSONA")
                self.__cursor.execute(sql)

                for (codper, nomper, apeper, dniper, emailper) in self.__cursor:
                    eel.LlenarTbl(codper, nomper, apeper, dniper, emailper)

                self.__cnn.close()
                self.__cursor.close()
                self.__miConexion.desconectar()

        except Exception as e:
            eel.AlertaJs(str(e))

    def ShowPer1(self, codigo):
        try:
            _, self.__cursor, self.__cnn = self.__miConexion.conectar()
            if (self.__miConexion.estado()):
                sql = ("SELECT codper, nomper, apeper, dniper, emailper FROM PERSONA where codper = '"+ str(codigo)+"'")
                self.__cursor.execute(sql)

                for (codper, nomper, apeper, dniper, emailper) in self.__cursor:
                    eel.LlenarInpt(codper, nomper,apeper,dniper,emailper)

                self.__cnn.close()
                self.__cursor.close()
                self.__miConexion.desconectar()

        except Exception as e:
            eel.AlertaJs(str(e))

    def ElimPer(self, codigo):
        try:
            _, self.__cursor, self.__cnn = self.__miConexion.conectar()
            if (self.__miConexion.estado()):
                sql = ("delete from PERSONA where codper = "+ str(codigo))
                self.__cursor.execute(sql)
                self.__cnn.commit()

                self.__cnn.close()
                self.__cursor.close()
                self.__miConexion.desconectar()
                print("Eliminacion exitosa")
                return True
            else:
                print("No pudiste con ella..")
                return False
        except Exception as e:
            print("ErrorElimPer_PersonaD")
            eel.AlertaJs(str(e))
            return False

