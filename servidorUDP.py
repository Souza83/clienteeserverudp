import socket  # Importa a biblioteca

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #  Variável de conexão

print('Socket criado com sucesso!!!')  #  Imprime o sucesso da conexão

host = 'localhost'  #  Variável do host local
port = 5432  #  Variável da porta do servidor

s.bind((host, port))  #  Ligação a partir do host e porta
mensagem = '\nServidor: Olá Cliente, BLZ!!!'  #  Variável mensagem.

while 1:  #  Enquanto a ligação (bind) verdadeiro
    dados, end = s.recvfrom(4096)  #  Recebe 4096 bytes e guarda dentro de endereços e dados
    if dados:  #  Se dados tiver aguma coisa ele envia a mensagem empacotada
        print('Servidor enviando mensagem...')
        s.sendto(dados + (mensagem.encode()), end)

