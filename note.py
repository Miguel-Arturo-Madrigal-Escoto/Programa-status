from datetime import datetime

class Note:
    def __init__(self, titulo, texto) -> None:
        self.__titulo = titulo
        self.__texto = texto
        self.__fecha = str(datetime.today().strftime('%Y-%m-%d'))

    
    def getTitulo(self) -> str:
        return self.__titulo
    
    def getTexto(self) -> str:
        return self.__texto
    
    def getFecha(self) -> str:
        return self.__fecha


        