from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QFormLayout, QHBoxLayout, QLineEdit, QPushButton, \
    QApplication
from PyQt5 import QtGui
import sys
class Ventana1(QMainWindow):

    # Hacer el método de construcción de la ventana:
    def __int__(self, parent=None):
        super(Ventana1, self).__init__(parent)

        # Poner el titúlo
        self.setWindowTitle("Formulario de registro")

        # Poner el icono
        self.setWindowIcon(QtGui.QIcon('imagenes/imagen 1'))

        # Estableciendo las propiedades de ancho y alto:
        self.ancho = 900
        self.alto = 600

        # Establecer el tamaño de la ventana
        self.resize(self.ancho, self.alto)

        #Hacer que la ventana se vea en el centro:
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # Fijar el ancho y el alto de la ventana:
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # Establecemos el fondo principal:
        self.fondo = QLabel(self)

        # Definimos la imagen de fondo
        self.imagenFondo = QPixmap('imagenes/imagen2')

        #Definimos la imagen de fondo:
        self.fondo.setPixmap(self.imagenFondo)

        # Establecemos el modo para escalar la imagen:
        self.fondo.setScaledContents(True)

        # Hacemos que se adapte el tamaño de la imagen
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        # Establecemos la ventana de fondo como la ventana central
        self.setCentralWidget(self.fondo)

        # Establecemos la distribución de los elementos en layout horizontal:
        self.horizontal = QHBoxLayout()
        # Le ponemos las margenes
        self.horizontal.setContentsMargins(30,30,30,30)

        # --------- LAYOUT IZQUIERDO ---------

        # Creamos el layout del lado izquierdo:
        self.ladoIzquierdo = QFormLayout()

        # Hacemos el letrero
        self.letrero1 = QLabel()

        # Le escribimos el texto:
        self.letrero1.setText('Información del Cliente')

        # Le asignamos el tipo de letra:
        self.letrero1.setFont(QFont("Andale Mono",20))

        # Le ponemos el color de texto y marqenes:
        self.letrero1.setStyleSheet("color: #00080;")

        # Agregamos el letrero en la primera fila:
        self.ladoIzquierdo.addRow(self.letrero1)

        # Hacemos el letrero:
        self.letrero2 = QLabel()

        # Establecemos el ancho del label:
        self.letrero2.setFixedWidth(340)

        # Le escribimos el texto:
        self.letrero2.setText("Por favor ingrese la información del cliente"
                             "\nen el formulario de abajo. Los campos marcados"
                             "\ncon asterisco son obligatorios.")

        # Le asignamos el tipo de letra:
        self.letrero2.setFont(QFont("Andale Mono", 10))

        # Le ponemos color de texto y margenes:
        self.letrero2.setStylesheet("clor: #00080; margin-bottom: 40px"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #000080;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        # Agregamos el letrero en la fila siguiente:
        self.ladoIzquierdo.addRow(self.letrero2)

        # Hacemos el campo para ingresar nombre:
        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)

        # Agregamos estos en los formularios:
        self.ladoIzquierdo.addRow("Nombre Completo*",self.nombreCompleto)

        # Hacemos el campo para ingresar el usuario:
        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)

        # Agregamos estos en los formularios:
        self.ladoIzquierdo.addRow("Usuario*", self.usuario)

        # Hacemos el campo para ingresar el password:
        self.pasword = QLineEdit()
        self.password.setFixedWidth(250)
        self.password.setEchoMode(QLineEdit.password)

        # AQgregamos estos en el formulario:
        self.ladoIzquierdo.addRow("password*", self.password2)

        # Hacemos el campo para ingresar el documento:
        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)

        # Agregamos el documento en el formulario:
        self.ladoIzquierdo.addRow("Documento*", self.documento)

        # Hcaemos el campo para ingresar el correo:
        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)

        # Agregamos el documento en el formulario:
        self.ladoIzquierdo.addRow("Correo*", self.correo)

        # Hacemos el boton para registrar los datos:
        self.botonRegistrar = QPushButton("Registrar")

        # Establecemos el ancho del botón:
        self.botonRegistrar.setFixedWidth(90)

        # Le ponemos  los estilos:
        self.botonRegistrar.setStyleSheet("background-color: #008B45;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)

        # Hacemos el botón para limpiar los datos:
        self.botonLimpiar = QPushButton("Limpiar")

        # Establecemos el ancho del botón:
        self.botonLimpiar.setFixeWidth(90)

        #Le ponemos los estilos:
        self.botonLimpiar.setStylesheet("background-color: #008B45;"
                                        "color: #FFFFFF;"
                                        "padding: 10px;"
                                        "margin-top: 48px;"
                                        )
        # Agregamos los botones al layout ladoDerecho:
        self.ladoDerecho.addRow(self.botonBuscar,self.botonRecuperar)
        # ---

        # Agregamos el Layout ladoDerecho al layout horizontal:
        self.horizontal.addLayout(self.ladoDerecho)

        # --------------- OJO IMPORTANTE PONER AL FINAL ----------------

        #Indicamos que el layout principal del fondo es horizontal:
        self.fondo.setLayout(self.horizontal)

    # Metodo del botónLimpiar:
    def accion_botonLimpiar(self):

        self.nombreCompleto.setText('')
        self.usuario.setText('')
        self.pasword.setText('')
        self.pasword2.setText('')
        self.documento.setText('')
        self.correo.setText('')
        self.pregunta1.setText('')
        self.respuesta1.setText('')
        self.pregunta2.setText('')
        self.respuesta2.setText('')
        self.pregunta3.setText('')
        self.respuesta3.setText('')


class QAPPlication:
    pass


if __name__ == '__main__':

    app = QApplication(sys.argv)

    ventana1 = Ventana1()

    ventana1.show()

    sys.exit(app.exec_())
