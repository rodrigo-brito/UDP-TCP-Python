import sys, time
from socket import *

tamanhoPacote = 1000
bufferSize = tamanhoPacote
dados = bytearray(tamanhoPacote-49) #tamanho base da estrutura é 49Bytes
sizeData = sys.getsizeof(dados)

port = 13000 #Porta padrão definiada para o servidor

def main():
    print 'Digite o tipo de terminal'
    print '1 - Cliente'
    print '2 - Servidor'
    
    op = input()

    tamanhoPacote = input('Tamanho do pacote = ')
    bufferSize = tamanhoPacote
    dados = bytearray(tamanhoPacote-49) #tamanho base da estrutura é 49Bytes
    sizeData = sys.getsizeof(dados)

    if op == 1:
        client()
    elif op == 2:        
        server()
    else:
        print 'Opcao invalida'
        sys.exit(2)

def server():
    serverSocket =  socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', port))
    print ('Server esta pronto')
    while(1):
        data, (host, remoteport) = serverSocket.recvfrom(bufferSize)   
        rcvSize = sys.getsizeof(data)
        serverSocket.sendto('OK', (host, remoteport))
        print 'Host = ', host, ':', remoteport, rcvSize,'B'


def client():
    print '---------'
    print 'Enviando ',sizeData,'B de dados'
    print '---------'
    host = raw_input('Digite o IP do servidor: ')

    s = socket(AF_INET, SOCK_DGRAM)
    t1 = time.time()
    s.sendto(dados, (host, port))
    t2 = time.time()
    data, serverAddress = s.recvfrom(bufferSize)
    s.close();
    t3 = time.time()

    print '\n---------'
    print 'Chegada = ',data
    print '---------'
    print 'Tempo envio    = ',t2-t1
    print 'Tempo resposta = ',t3-t2
    print 'Tempo total    = ',t3-t1
    print 'Throughput     = ',sizeData*0.001 / (t3-t1),'KB/sec.'
main()