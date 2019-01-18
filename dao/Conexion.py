import mysql.connector


class ConexionD():
    def __init__(self):
        self.__host = "localhost"
        self.__user = "root"
        self.__passwd = ""
        self.__db = "SistAgenda"

    def conectar(self):
        try:
            self.__cnn = mysql.connector.connect(host=self.__host, user=self.__user, passwd=self.__passwd, db=self.__db)
            self.__cursor = self.__cnn.cursor()
            return True, self.__cursor, self.__cnn
        except:
            return False

    def estado(self):
        try:
            if (self.__cnn.is_connected()):
                return True
            else:
                return False
        except:
            return False

    def desconectar(self):
        if (self.estado()):
            self.__cursor.close()
            self.__cnn.close()
            return True
        else:
            return False
