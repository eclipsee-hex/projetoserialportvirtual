import serial

def list_serial_ports():
    """Lista todas as portas seriais disponíveis."""
    ports = serial.tools.list_ports.comports()
    return [comport.device for comport in ports]

def connect_serial(port, baudrate=9600):
    """Conecta à porta serial especificada."""
    ser = serial.Serial(port, baudrate)
    return ser

def send_data(ser, data):
    """Envia dados para a porta serial."""
    ser.write(data.encode())

def receive_data(ser):
    """Recebe dados da porta serial."""
    data = ser.readline().decode()
    return data