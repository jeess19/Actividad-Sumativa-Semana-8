import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QListWidget, QVBoxLayout, QMessageBox

class TareasApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de Tareas Estudiantiles")
        self.setGeometry(200, 200, 400, 300)

        # --- Widgets ---
        self.lbl_tarea = QLabel("Nombre de la tarea:")
        self.txt_tarea = QLineEdit()

        self.lbl_fecha = QLabel("Fecha límite (dd/mm/aaaa):")
        self.txt_fecha = QLineEdit()

        self.btn_agregar = QPushButton("Agregar Tarea")
        self.btn_limpiar = QPushButton("Limpiar Lista")

        self.lista_tareas = QListWidget()

        # --- Layout ---
        layout = QVBoxLayout()
        layout.addWidget(self.lbl_tarea)
        layout.addWidget(self.txt_tarea)
        layout.addWidget(self.lbl_fecha)
        layout.addWidget(self.txt_fecha)
        layout.addWidget(self.btn_agregar)
        layout.addWidget(self.btn_limpiar)
        layout.addWidget(self.lista_tareas)

        self.setLayout(layout)

        # --- Conexión de botones ---
        self.btn_agregar.clicked.connect(self.agregar_tarea)
        self.btn_limpiar.clicked.connect(self.limpiar_lista)

    def agregar_tarea(self):
        """Agrega la tarea con fecha a la lista"""
        tarea = self.txt_tarea.text()
        fecha = self.txt_fecha.text()

        if tarea and fecha:
            self.lista_tareas.addItem(f"Tarea: {tarea} - Fecha límite: {fecha}")
            self.txt_tarea.clear()
            self.txt_fecha.clear()
        else:
            QMessageBox.warning(self, "Error", "Debes llenar todos los campos")

    def limpiar_lista(self):
        """Limpia todas las tareas registradas"""
        self.lista_tareas.clear()
        QMessageBox.information(self, "Limpieza", "Lista de tareas vaciada")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = TareasApp()
    ventana.show()
    sys.exit(app.exec_())
