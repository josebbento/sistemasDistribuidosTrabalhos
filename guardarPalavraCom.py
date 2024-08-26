from random import randint
from threading import Thread
lista = []
lista.sort

class apoio:
    """essa classe serve de apoio para o script principal
    """    
    
    def geraPalavra(max = 30):
        """o metodo gera palavras

        Args:
            max (int, optional): a quantidade máxima de caracteres que as palavras devem ter. Defaults to 30.

        Returns:
            string: a palavra gerada
        """        
        op = 'abcdefghijklmnopqrstuvwxyz'
        palavra = ''
        while True:
            l = randint(0, len(op) - 1)
            if len(palavra) >= max and len(palavra) != 0:
                return palavra
            elif op[l] != ' ':
                palavra += op[l]

    def colocaLista(lista, quant = 10):
        """o metodo gera e guarda as palavras em uma lista

        Args:
            lista (list): lista de destino
            quant (int, optional): quantidade de palavras. Defaults to 10.
        """        
        for i in range(quant):
            lista.append(apoio.geraPalavra(randint(1, 15)))

    def colocaArq(quant = 10, arquivo = "palavras.txt"):
        """o metodo gera e guarda as palavras em um arquivo

        Args:
            quant (int, optional): quantidade de palavras. Defaults to 10.
            arquivo (str, optional): arquivo de destino. Defaults to "palavras.txt".
        """        
        arq = open(arquivo,"w")
        for i in range(quant):
            arq.write(apoio.geraPalavra(randint(1, 15)) + '\n')

    def quick(lista):
        """o metodo ordena uma lista em ordem alfabética

        Args:
            lista (list): lista desordenada

        Returns:
            list: lista ordenada
        """        
        if(len(lista)>1):        
            piv=int(len(lista)/2)
            val=lista[piv]
            lft=[i for i in lista if i<val]
            mid=[i for i in lista if i==val]
            rgt=[i for i in lista if i>val]

            res=apoio.quick(lft)+mid+apoio.quick(rgt)
            return res
        else:
            return lista

if __name__ == '__main__':
    quant = 10
    lista1 = []

    t1 = Thread(target=apoio.colocaLista, args=(lista1, quant))
    t1.start()

    t2 = Thread(target=apoio.colocaArq, args=quant)
    t2.start

    t1.join(); t2.join

    lista2 = lista1.copy()
    lista1.sort()
    print(lista1)
    print(apoio.quick(lista2))
