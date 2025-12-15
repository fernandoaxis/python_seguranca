import socket  # Módulo responsável pela comunicação em rede

# =========================
# CONFIGURAÇÕES DO SERVIDOR
# =========================

HOST = '127.0.0.1'  # Endereço IP do servidor (localhost)
PORT = 5000         # Porta onde o servidor ficará escutando

# =========================
# CRIAÇÃO DO SOCKET
# =========================

# AF_INET  -> Usa IPv4
# SOCK_STREAM -> Usa TCP (conexão orientada)
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# =========================
# ASSOCIA IP E PORTA
# =========================

# "bind" liga o socket ao IP e porta definidos
servidor.bind((HOST, PORT))

# =========================
# MODO DE ESCUTA
# =========================

# Coloca o servidor em modo de escuta
# O número 1 indica quantas conexões podem ficar na fila de espera
servidor.listen(1)

print(f"Servidor TCP aguardando conexão em {HOST}:{PORT}...")

# =========================
# ACEITA CONEXÃO DO CLIENTE
# =========================

# accept() pausa o programa até um cliente se conectar
# conn -> socket específico do cliente
# addr -> endereço (IP, porta) do cliente
conn, addr = servidor.accept()
print(f"Conectado por {addr}")

# =========================
# COMUNICAÇÃO COM O CLIENTE
# =========================

while True:
    # Recebe até 1024 bytes enviados pelo cliente
    dados = conn.recv(1024)

    # Se não houver dados, significa que o cliente encerrou a conexão
    if not dados:
        print("Cliente desconectou.")
        break

    # Converte os bytes recebidos para string
    mensagem = dados.decode()
    print(f"Mensagem recebida do cliente: {mensagem}")

    # Cria uma resposta para o cliente
    resposta = f"Servidor recebeu: {mensagem}"

    # Envia a resposta codificada
    conn.sendall(resposta.encode())

# =========================
# ENCERRAMENTO DA CONEXÃO
# =========================

conn.close()       # Fecha a conexão com o cliente
servidor.close()   # Fecha o socket do servidor
print("Servidor encerrado.")
