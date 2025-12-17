# cliente_udp.py
import socket

# IP e porta do servidor
SERVER_IP = "127.0.0.1"  # localhost
SERVER_PORT = 5000

# Cria o socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Usuário digita a mensagem
    mensagem = input("Digite uma mensagem (ou 'sair'): ")

    if mensagem.lower() == "sair":
        break

    # Envia mensagem para o servidor
    sock.sendto(mensagem.encode(), (SERVER_IP, SERVER_PORT))

    # Aguarda resposta do servidor
    data, _ = sock.recvfrom(1024)

    print("Resposta do servidor:", data.decode())

# Fecha o socket
sock.close()
