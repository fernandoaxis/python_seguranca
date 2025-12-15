import socket  # Importa o módulo para trabalhar com sockets

# Definindo o IP e a porta do servidor (no caso, estamos usando '127.0.0.1' para se conectar à própria máquina)
HOST = '127.0.0.1'  # IP do servidor (localhost)
PORT = 5000         # Porta em que o servidor estará ouvindo as conexões

# Criação do socket TCP (AF_INET indica que estamos utilizando IPv4, SOCK_STREAM define o tipo como TCP)
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Conectando-se ao servidor na máquina local e na porta especificada
    cliente.connect((HOST, PORT))
    print(f"Conectado ao servidor {HOST} na porta {PORT}")
    
    while True:
        # Solicitando ao usuário que digite uma mensagem
        mensagem = input("Digite uma mensagem (ou 'sair' para encerrar): ")
        
        # Se o usuário digitar 'sair', o programa encerrará a conexão
        if mensagem.lower() == 'sair':
            print("Fechando a conexão...")
            break
        
        # Enviando a mensagem codificada para o servidor
        cliente.sendall(mensagem.encode())
        
        # Esperando uma resposta do servidor e recebendo até 1024 bytes
        resposta = cliente.recv(1024)
        
        # Imprimindo a resposta do servidor, decodificada
        print(f"Resposta do servidor: {resposta.decode()}")
        
except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    # Fechando a conexão com o servidor
    cliente.close()
    print("Conexão finalizada.")
