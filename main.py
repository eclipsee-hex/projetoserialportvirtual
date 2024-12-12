import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QVBoxLayout
from PyQt5.QtCore import QCoreApplication
import serial_utils

class SerialGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Comunicação Serial")

        # Listagem de portas
        self.ports = serial_utils.list_serial_ports()

        # elementos interface
        self.label = QLabel("Digite a mensagem:", self)
        self.line_edit = QLineEdit(self)
        self.port_combo = QComboBox(self)
        self.port_combo.addItems(self.ports)
        self.send_button = QPushButton("Enviar", self)
        self.receive_label = QLabel("Mensagem recebida:", self)
        self.baud_rate_label = QLabel("Baud rate:", self)
        self.baud_rate_edit = QLineEdit("9600", self)

        # Conexão dos sinais e slots
        self.port_combo.currentIndexChanged.connect(self.configure_port)
        self.send_button.clicked.connect(self.send_data)

        # Posicionamento elementos da janela
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.port_combo)
        layout.addWidget(self.baud_rate_label)
        layout.addWidget(self.baud_rate_edit)
        layout.addWidget(self.send_button)
        layout.addWidget(self.receive_label)
        self.setLayout(layout)

        # Configura a porta inicial
        if self.ports:
            self.configure_port()

        # leitura dos dados da porta serial
        self.timer = QCoreApplication.instance().timer()
        self.timer.timeout.connect(self.receive_data)
        self.timer.start(100)

    def configure_port(self):
        selected_port = self.port_combo.currentText()
        baud_rate = int(self.baud_rate_edit.text())
        try:
            self.ser = serial_utils.connect_serial(selected_port, baud_rate)
            print(f"Conectado à porta {selected_port} com baud rate {baud_rate}")
        except serial.SerialException as e:
            print(f"Erro ao conectar à porta: {e}")

    def send_data(self):
        message = self.line_edit.text()
        serial_utils.send_data(self.ser, message)

    def receive_data(self):
        try:
            data = serial_utils.receive_data(self.ser)
            self.receive_label.setText(data)
        except serial.SerialException:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SerialGUI()
    window.show()
    sys.exit(app.exec_())