import conexionD as dao

class PersonaD():

    def __init__(self,nom,ape,dni):
        self.__nomper=nom
        self.__apeper=ape
        self.__dniper=dni
        self.__miConexion = dao.conexionD()
    
    def RegPer(self):
        try:
            _,self.__cursor,self.__cnn = self.__miConexion.conectar()
            if (self.__miConexion.estado()):
                sql= ("INSERT INTO PERSONA"
                "(NOMPER, APEPER, DNIPER)"
                "VALUES (%s, %s,%s)")
                val=(self.__nomper,self.__apeper,self.__dniper)

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
        