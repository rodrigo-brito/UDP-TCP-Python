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
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', port))
    s.listen(1)
    print 'Servidor esperando conexao...'
    while 1:
        conn, (host, remoteport) = s.accept()
        data = conn.recv(bufferSize)
        rcvSize = sys.getsizeof(data)
        conn.send('OK')
        conn.close()
        print 'Host = ', host, ':', remoteport, rcvSize,'B'


def client():
    print '---------'
    print 'Enviando ',sizeData,'B de dados'
    print '---------'
    host = raw_input('Digite o IP do servidor: ')

    s = socket(AF_INET, SOCK_STREAM)    
    t1 = time.time()    
    s.connect((host, port))    
    t2 = time.time()
    s.send(dados)    
    t3 = time.time()    
    data = s.recv(bufferSize)
    s.close();
    t4 = time.time()
    print '\n---------'
    print 'Chegada = ',data
    print '---------'
    print 'Tempo conexao  = ',t2-t1
    print 'Tempo envio    = ',t3-t2
    print 'Tempo resposta = ',t4-t3
    print 'Tempo total    = ',t4-t1
    print 'Throughput     = ',sizeData*0.001 / (t4-t1),
    print 'KB/sec.'
main()