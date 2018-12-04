import conexionD as dao
import mysql.connector
class PersonaD():

    def __init__(self):
        self.__nomper='demo'
        self.__apeper='demoo'
        self.__dniper='1234578'
        self.__miConexion = dao.conexionD()
    
    def RegPer(self):
        try:
            _,self.__cursor,self.__cnn = self.__miConexion.conectar()
            if (self.__miConexion.estado()):
                sql= ("INSERT INTO PERSONA"
                "(NOMPER, APEPER, DNIPER)"
                "VALUES (%s, %s,%s)")
                val=("hola","gg","12345678")

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
        

Persona = PersonaD()
Persona.RegPer()