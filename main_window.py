from PySide2.QtWidgets import QMainWindow, QFileDialog
from PySide2.QtCore import Slot
from note import Note
from ui_mainwindow import Ui_MainWindow
import pickle, threading
from time import sleep
from datetime import datetime


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Notepad')
        
        # ? al inicio
        self.cargarNota()

        # ? abrir una en especifico
        self.ui.actionAbrir.triggered.connect(self.abrir_ventana)
        # ? guardar nota con la ventana
        self.ui.actionGuardar.triggered.connect(self.guardar_ventana)


        threading.Thread(target=self.respaldoInfo, daemon=True).start()
        
        
        
    @Slot()
    def guardarNota(self, ubicacion='nueva_nota'):
        titulo = self.ui.lineTitulo.text()
        texto = self.ui.textoNota.toPlainText()

        self.dbfile = open(ubicacion, 'wb')
        self.nota = Note(titulo, texto)

        pickle.dump(self.nota, self.dbfile)    

        self.dbfile.close()

        # * guardar ultima nota
        self.guardarUltima(titulo, texto)

        
    def guardarUltima(self, titulo, texto):
        self.dbfile = open('nueva_nota', 'wb')
        self.nota = Note(titulo, texto)

        pickle.dump(self.nota, self.dbfile)                     
            
        self.dbfile.close()


    def cargarNota(self, note='nueva_nota'):
        try:
            with open(note, 'rb') as dbfile:
                self.nota = pickle.load(dbfile)
                self.ui.lineTitulo.setText(self.nota.getTitulo())
                self.ui.lineFecha.setText(self.nota.getFecha())
                self.ui.textoNota.setText(self.nota.getTexto())       
                if note == 'nueva_nota':
                    note = 'F:/Documentos/Computación tolerante a fallas/status/' + note  
                self.ui.labelRuta.setText(note)
               
            dbfile.close()
        except:
            self.ui.lineTitulo.setText('')
            self.ui.textoNota.setText('')
            self.ui.lineFecha.setText(str(datetime.today().strftime('%Y-%m-%d')))
    
    @Slot()
    def abrir_ventana(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir archivo',
            '.',
            ''
        )[0]
        if ubicacion != '':
            self.cargarNota(ubicacion)

    @Slot()
    def guardar_ventana(self):
        ubicacion = QFileDialog.getSaveFileName(
            self, #origen
            'Guardar archivo', #titulo de la ventana
            '.', # directorio (raiz del proyecto)
            '' # extension del archivo
        )[0]
        if ubicacion != '':
            self.guardarNota(ubicacion)

    def respaldoInfo(self):
        while True:
            self.guardarNota()
            sleep(3)


       