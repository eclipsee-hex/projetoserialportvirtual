import serial
import serial.tools.list_ports

class SerialManager:
    def __init__(self):
        self.serial_connection = None
        
    def get_ports(self):
        ports = serial.tools.list_ports.comports()
        return [port.device for port in ports] or ["Nenhuma porta Localizada"]
    
    def connect(self, port):
        try:
            self.serial_connection = serial.Serial(
                port,
                boudrate=9600,
                timeout=1,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS
            )
            return True
        except serial.SerialException:
            return False
    
    def send_data(self, data):
        if self.serial_connection and self.serial_connection.is_open:
            try:
                self.serial_connection.write(data.encode())
                return True
            except Exception:
                return False
        return False
    
    def disconnect(self):
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            return True
        return False