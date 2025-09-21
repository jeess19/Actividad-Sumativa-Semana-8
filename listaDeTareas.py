import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, 
                             QPushButton, QListWidget, QVBoxLayout, QMessageBox, QHBoxLayout)

class TareasApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de Tareas Estudiantiles")
        self.setGeometry(200, 200, 420, 350)

        # --- Widgets ---
        self.lbl_tarea = QLabel("Nombre de la tarea:")
        self.txt_tarea = QLineEdit()

        self.lbl_fecha = QLabel("Fecha límite (dd/mm/aaaa):")
        self.txt_fecha = QLineEdit()

        self.btn_agregar = QPushButton("Agregar Tarea")
        self.btn_limpiar = QPushButton("Limpiar Lista")

        self.lista_tareas = QListWidget()

        # --- Label para contador ---
        self.lbl_contador = QLabel("Cantidad de tareas: 0")

        # --- Layout ---
        layout = QVBoxLayout()
        layout.addWidget(self.lbl_tarea)
        layout.addWidget(self.txt_tarea)
        layout.addWidget(self.lbl_fecha)
        layout.addWidget(self.txt_fecha)

        # fila de botones
        botones_layout = QHBoxLayout()
        botones_layout.addWidget(self.btn_agregar)
        botones_layout.addWidget(self.btn_limpiar)
        layout.addLayout(botones_layout)

        layout.addWidget(self.lista_tareas)
        layout.addWidget(self.lbl_contador)

        self.setLayout(layout)

        # --- Conexión de botones ---
        self.btn_agregar.clicked.connect(self.agregar_tarea)
        self.btn_limpiar.clicked.connect(self.limpiar_lista)

    def actualizar_contador(self):
        """Actualiza el texto del contador con la cantidad actual de tareas."""
        cantidad = self.lista_tareas.count()
        self.lbl_contador.setText(f"Cantidad de tareas: {cantidad}")

    def agregar_tarea(self):
        """Agrega la tarea con fecha a la lista si los campos son válidos."""
        tarea = self.txt_tarea.text().strip()
        fecha = self.txt_fecha.text().strip()

        if not tarea or not fecha:
            QMessageBox.warning(self, "Error", "Debes llenar todos los campos")
            return

        # Validación sencilla del formato de fecha dd/mm/aaaa
        if len(fecha.split('/')) != 3:
            QMessageBox.warning(self, "Error", "Formato de fecha no válido. Use dd/mm/aaaa")
            return

        self.lista_tareas.addItem(f"Tarea: {tarea} - Fecha límite: {fecha}")
        self.txt_tarea.clear()
        self.txt_fecha.clear()
        self.actualizar_contador()
        QMessageBox.information(self, "Éxito", "Tarea agregada correctamente")

    def limpiar_lista(self):
        """Limpia todas las tareas registradas"""
        self.lista_tareas.clear()
        self.actualizar_contador()
        QMessageBox.information(self, "Limpieza", "Lista de tareas vaciada")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = TareasApp()
    ventana.show()
    sys.exit(app.exec_())
