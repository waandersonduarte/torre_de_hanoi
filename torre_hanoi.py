class Stack:
    
    def __init__(self):
        self.__container = []

    #Insere um elemento no top da pilha
    def push(self, item):
        self.__container.append(item)

    #Remove um elemento do topo da pilha
    def pop(self):
        return self.__container.pop()

    #Mostra o elemento do top
    def peek(self):
        return self.__container[-1]

    def __str__(self):
        return str(self.__container)

    def isEmpty(self):
        return self.__container == []


class Hanoi:

    #Construtor - Cria a torre_a, torre_b, torre_c
    #Adiciona os item 3, 2 e 1 na torre_a
    def __init__(self):
        self.movimentos = 0
        self.torre_a = Stack()
        self.torre_b = Stack()
        self.torre_c = Stack()
        self.torre_a.push(3)
        self.torre_a.push(2)
        self.torre_a.push(1)
        self.mostra_jogo()

        
    #Método movimenta(torre de origem, torre de destino)
    #Movimenta o elemento de uma torre para outra
    #def movimenta(self, torre_origem, torre_destino):
    def movimenta(self, torre_origem, torre_destino):
        if self.verifica_condicao(torre_origem, torre_destino):
            torre_destino.push(torre_origem.pop())
            self.movimentos += 1
            self.mostra_jogo()
        else:
            print("Movimento não é valido.")

    #mostra_jogo
    #Mostra os valores da torres a,b, e c
    def mostra_jogo(self):
        print('##################')
        print(f'Inicio de jogo') if self.movimentos == 0 else print(f'Movimento {self.movimentos}')
        print(f'Torre A: {self.torre_a}')
        print(f'Torre B: {self.torre_b}')
        print(f'Torre C: {self.torre_c}')
        print('') 

    #__Verifica_condicao
    #verifica se o elemento pode ser movido
    #maior nao pode ficar em cima do menor
    #e nao pode movimentar de uma torre sem elementos (vazia)
    def verifica_condicao(self, origem, destino):
        if origem.isEmpty() or not(destino.isEmpty()) and origem.peek() > destino.peek():
            return False
        return True
        

    #verifica_jogo_acabou
    def verifica_final(self):
        if f'{self.torre_c}' == '[3, 2, 1]':
            print(f'O jogo acabou. Você ganhou com {self.movimentos} movimentos.')


    #resolve
    def resolve_iterativa(self):
        jogo.movimenta(jogo.torre_a, jogo.torre_c)
        jogo.movimenta(jogo.torre_a, jogo.torre_b)
        jogo.movimenta(jogo.torre_c, jogo.torre_b)
        jogo.movimenta(jogo.torre_a, jogo.torre_c)
        jogo.movimenta(jogo.torre_b, jogo.torre_a)
        jogo.movimenta(jogo.torre_b, jogo.torre_c)
        jogo.movimenta(jogo.torre_a, jogo.torre_c)
        jogo.verifica_final()

    def resolve_recursiva(self, torre_origem, torre_destino, torre_auxiliar, n):
        if n == 1:
            self.movimenta(torre_origem, torre_destino)
        else:
            self.resolve_recursiva(torre_origem, torre_auxiliar, torre_destino, n-1)
            self.resolve_recursiva(torre_origem, torre_destino, torre_auxiliar, 1)
            self.resolve_recursiva(torre_auxiliar, torre_destino, torre_origem, n-1)

jogo = Hanoi()
jogo.resolve_iterativa()
#jogo.resolve_recursiva(jogo.torre_a, jogo.torre_c, jogo.torre_b, 3)