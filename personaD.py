import conexionD as dao
from personaM import PersonaM

class PersonaD(PersonaM):        
    
    def RegPer(self):
        self.__miConexion = dao.conexionD()
        try:
            _,self.__cursor,self.__cnn = self.__miConexion.conectar()
            if (self.__miConexion.estado()):
                sql= ("INSERT INTO PERSONA"
                "(NOMPER, APEPER, DNIPER)"
                "VALUES (%s, %s,%s)")
                val=(PersonaM.getNomPer(self),PersonaM.getApePer(self),PersonaM.getDniPer(self))
                self.__cursor.execute(sql,val)
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
            print (e)
            return False
        
    def ShowPer(self):
        self.__miConexion = dao.conexionD()
        try:
            _,self.__cursor,self.__cnn = self.__miConexion.conectar()
            if (self.__miConexion.estado()):
                sql= ("SELECT * FROM PERSONA")
                self.__cursor.execute(sql)
                print(self.__cursor.fetchall())

                self.__cnn.close()
                self.__cursor.close()
                self.__miConexion.desconectar()
        except Exception as e:
            print(e)
        