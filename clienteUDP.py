import socket  #  Importa biblioteca Socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Variável de conexão UDP.

print('Cliente Socket Criado Com Sucesso!!!')  #  Imprime mensagem após conexão.

host = 'localhost'  #  Rede local interna do computador.
porta = 5433  #  Variável porta do cliente
mensagem = 'Olá servidor, firmeza mano?'  #  Variável mensagem a ser enviada

try:
    # print('Empacotando mensagem do Cliente: ' + mensagem)  #  Imprime a mensagem
    s.sendto(mensagem.encode(), (host, 5432))  #  Conecta e envia mensagem empacotada

    dados, servidor = s.recvfrom(4096)  #  Variável  que recebe uma resposta de 4096 bytes
    dados = dados.decode()  #  Desenpacota os dados
    print('Cliente: ' + dados)  #  Imprime a mensagem desempacotada
finally:
    print('Cliente: Fechando a conexão!')  #  Imprime mensagem de fechamento de conexão.
    s.close()  #  Fecha conexão
