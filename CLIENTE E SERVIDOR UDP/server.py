# servidor_udp.py
import socket

# Endereço e porta do servidor
HOST = "0.0.0.0"   # aceita mensagens de qualquer IP
PORT = 5000        # porta usada

# Cria o socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Liga o socket ao endereço e porta
sock.bind((HOST, PORT))

print("Servidor UDP ligado e esperando mensagens...")

# Loop infinito para receber mensagens
while True:
    # Recebe até 1024 bytes e o endereço do cliente
    data, endereco_cliente = sock.recvfrom(1024)

    # Converte bytes em texto
    mensagem = data.decode()

    print(f"Mensagem recebida: {mensagem}")

    # Resposta para o cliente
    resposta = "Mensagem recebida com sucesso!"

    # Envia a resposta para o cliente
    sock.sendto(resposta.encode(), endereco_cliente)
