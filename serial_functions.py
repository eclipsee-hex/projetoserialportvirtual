import serial as sr


def conectar_serial(porta, baudrate):
    ser=sr.Serial(porta, baudrate)
    return ser

def enviar_dados(serial_port, dados):
    serial_port.write(dados.encode())
    
def receber_dados(serial_port):
    dados = serial_port.readline().encode()
    return dados