import serial
import serial.tools.list_ports
import time

# Listando as portas seriais disponíveis
ports = list(serial.tools.list_ports.comports())
if not ports:
    print("Nenhuma porta serial encontrada.")
else:
    for port in ports:
        print(f'Porta encontrada: {port.device}')

try:
    ser = serial.Serial('COM1', baudrate=9600, timeout=1, parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
    print(f'Conectado à porta {ser.portstr}')


    dados = "Olá, envio realizado com sucesso!"
    ser.write(dados.encode())  
    print(f'Dados enviados: {dados}')
    

    time.sleep(2)

except serial.SerialException as e:
    print(f"Erro ao conectar à porta serial: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print('Conexão serial fechada.')
