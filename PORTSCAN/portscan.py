import socket

def port_scan(host, start_port, end_port):
    print(f"\nIniciando port scan em {host}")
    print(f"Portas de {start_port} até {end_port}\n")

    for port in range(start_port, end_port + 1):
        try:
            # Cria o socket TCP
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)  # timeout curto para não travar

            # Tenta conectar
            result = sock.connect_ex((host, port))

            if result == 0:
                print(f"[+] Porta {port} aberta")
            else:
                print(f"[-] Porta {port} fechada")

            sock.close()

        except KeyboardInterrupt:
            print("\nScan interrompido pelo usuário.")
            break
        except socket.error:
            print("Erro ao conectar.")
            break

# ===== EXECUÇÃO =====
if __name__ == "__main__":
    target = input("Digite o host (ex: 127.0.0.1): ")
    start = int(input("Porta inicial: "))
    end = int(input("Porta final: "))

    port_scan(target, start, end)
