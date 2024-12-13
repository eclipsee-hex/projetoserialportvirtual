import tkinter as tk
from tkinter import messagebox
from serial_logic import SerialManager

class SerialApp:
    def __init_(self, root):
        self.root= root
        self.root.title("Serial Communication")
        
        self.serial_manager = SerialManager()
        
        #lista portas
        tk.Label(root, text="Serial:").grid(row=0, column=0, padx=10, pady=5)
        self.port_var = tk.StringVar()
        self.update_ports()
        
        #campo para dados
        tk.Label(root, text="Dados para enviar:").grid(row=1, column=0, padx=10, pady=5)
        self.data_entry = tk.Entry(root, width=30)
        self.data_entry.grid(row=1, column=1, padx=10, pady=5)
        
        #botões da interface
        self.connect_button = tk.Button(root, text="Conectar", command=self.connect)
        self.connect_button.grid(row=2, column=0, padx=10, pady=5)
        
        self.send_button = tk.Button(root, text="enviar", command=self.send_data, state=tk.DISABLED)
        self.send_button.grid(row=2, column=1, padx=10, pady=5)
        
        self.disconnect_button = tk.Button(root, text="desconectar", command=self.disconnect, state=tk.DISABLED)
        self.disconnect_button.grid(row=3, column=0, columnspan=2, pady=5)
    def update_ports(self):
        ports = self.serial_manager.get_ports()
        self.port_var.set(ports[0] if ports else "nenhuma porta encontrada")
        self.port_menu = tk.OptionMenu(self.root, self.port_var, *ports) 
        self.port_menu.grid(row=0, column=1, padx=10, pady=5)
    def connect(self)    :
        port = self.port_var.get()
        if not port or port == "nenhuma porta encontrada":
            messagebox.showerror("erro", "Seleciona uma porta valida!!!")
            return
        
        if self.serial_manager.connect(port):
            self.send_button.config(state=tk.NORMAL)
            self.disconnect_button.config(state=tk.NORMAL)
            self.connect_button.config(state=tk.DISABLED)
            messagebox.showerror("Erro", "Erro ao conectar à porta serial.")
            
            