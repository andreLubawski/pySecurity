import socket
import sys


def main():

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("Falha na conexão")
        print("Erro: {}".format(e))
        sys.exit()

    print("Socket criado com sucesso")

    HostAlvo = input("Digite o host ou ip a ser conectado: ")
    PortaAlvo = input("Digite a porta: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print("cliente tcp conectado com sucesso!\n Host:" + HostAlvo + "\nPorta" + PortaAlvo)
        s.shutdown(2)
        "em 2 segundos a conexão é finalizada"
    except socket.error as e:
        print("A conexão falhou")
        print("Erro: {}".format(e))
        sys.exit()
if __name__ == "__main__":
    main()
