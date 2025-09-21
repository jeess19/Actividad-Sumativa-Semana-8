import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class GestorGastos(QWidget):
    def _init_(self):
        super()._init_()
        self.setWindowTitle("Gestor de Gastos Mensuales")
        self.gastos = []
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Ingreso mensual
        self.ingreso_label = QLabel("Ingreso mensual:")
        self.ingreso_input = QLineEdit()
        layout.addWidget(self.ingreso_label)
        layout.addWidget(self.ingreso_input)

        # Nombre del gasto
        self.nombre_gasto_label = QLabel("Nombre del gasto:")
        self.nombre_gasto_input = QLineEdit()
        layout.addWidget(self.nombre_gasto_label)
        layout.addWidget(self.nombre_gasto_input)

        # Monto del gasto
        self.monto_gasto_label = QLabel("Monto del gasto:")
        self.monto_gasto_input = QLineEdit()
        layout.addWidget(self.monto_gasto_label)
        layout.addWidget(self.monto_gasto_input)

        # Botón para agregar gasto
        self.agregar_btn = QPushButton("Agregar gasto")
        self.agregar_btn.clicked.connect(self.agregar_gasto)
        layout.addWidget(self.agregar_btn)

        # Botón para calcular balance
        self.balance_btn = QPushButton("Calcular balance")
        self.balance_btn.clicked.connect(self.calcular_balance)
        layout.addWidget(self.balance_btn)

        # Botón para limpiar
        self.limpiar_btn = QPushButton("Limpiar")
        self.limpiar_btn.clicked.connect(self.limpiar_campos)
        layout.addWidget(self.limpiar_btn)

        # Lista de gastos
        self.lista_gastos_label = QLabel("Gastos registrados:")
        layout.addWidget(self.lista_gastos_label)

        # Balance restante
        self.balance_label = QLabel("Balance restante:")
        layout.addWidget(self.balance_label)

        self.setLayout(layout)

    def agregar_gasto(self):
        nombre = self.nombre_gasto_input.text()
        try:
            monto = float(self.monto_gasto_input.text())
            self.gastos.append((nombre, monto))
            self.actualizar_lista_gastos()
        except ValueError:
            self.lista_gastos_label.setText("⚠️ Monto inválido.")

    def actualizar_lista_gastos(self):
        texto = "\n".join([f"{nombre}: ${monto:.2f}" for nombre, monto in self.gastos])
        self.lista_gastos_label.setText(f"Gastos registrados:\n{texto}")

    def calcular_balance(self):
        try:
            ingreso = float(self.ingreso_input.text())
            total_gastos = sum(monto for _, monto in self.gastos)
            balance = ingreso - total_gastos
            self.balance_label.setText(f"Balance restante: ${balance:.2f}")
        except ValueError:
            self.balance_label.setText("⚠️ Ingreso inválido.")

    def limpiar_campos(self):
        self.ingreso_input.clear()
        self.nombre_gasto_input.clear()
        self.monto_gasto_input.clear()
        self.gastos = []
        self.lista_gastos_label.setText("Gastos registrados:")
        self.balance_label.setText("Balance restante:")

if _name_ == "_main_":
    app = QApplication(sys.argv)
    ventana = GestorGastos()
    ventana.show()
    sys.exit(app.exec_())