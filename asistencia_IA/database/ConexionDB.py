import pymysql

class ConexionDB():
   #conexion
    def __init__(self,con):
        self.con = con

    def connection():
        con = pymysql.connect(
            host ="localhost",
            port = 3306,
            user = "root",
            password = "2468",
            db = "colegio"
        )

        print("Conexion establecida!")
        return con

    def getUser(self,user,password):
        with self.con.cursor()as cursor:
            sql = """select usuario from login where usuario =%s and clave =%s""" 
            cursor.execute(sql,(user,password))
            result = cursor.fetchone()
            return result
