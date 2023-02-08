from data.models.tipo import Tipo

class TipoDao():
    def __init__(self,db) -> None:
        self.db = db

    def get_all(self):
        cursor=self.db.cursor()
        cursor.execute('SELECT * FROM tipo')
        data=cursor.fetchall()
        tipos_lista = []

        for tipos in data:
            tipos_lista.append(Tipo(tipos[0],tipos[1],tipos[2]))
        
        return tipos_lista
            
    def addTipo(self,tipo):
            cursor=self.db.cursor()
            cursor.execute('INSERT INTO tipo (idtipo,elemento,afinidad) VALUES (%s,%s,%s)',(tipo.idtipo,tipo.elemento,tipo.afinidad))
            self.db.commit()

    def deleteTipo(self,idtipo):
            cursor=self.db.cursor()
            cursor.execute('DELETE FROM tipo WHERE idtipo=%s',(idtipo,))
            self.db.commit()
