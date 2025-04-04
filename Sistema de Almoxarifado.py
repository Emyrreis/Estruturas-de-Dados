# Inicialização da lista vazia 
class Lista:
    def __init__(self):
        self.lista = []

    def push(self, item):
        self.lista.append(item)

    def pop(self):
        if not self.is_empty():
            return self.lista.pop()
        else:
            print("Lista vazia!")
            return None

    def peek(self):
        if not self.is_empty():
            return self.lista[-1]
        else:
            print("Lista vazia!")
            return None

    def is_empty(self):
        return len(self.lista) == 0

    def size(self):
        return len(self.lista)


# Sistema de Almoxarifado simples
class Almoxarifado:
    def __init__(self):
        self.estoque = Lista()
    
    def adicionar(self, item):
        self.estoque.push(item)
        print(f"Item {item} adicionado")
    
    def retirar(self):
        item = self.estoque.pop()
        if item:
            print(f"Item {item} retirado")
        return item
    
    def proximo_item(self):
        return self.estoque.peek()
    
    def quantidade(self):
        return self.estoque.size()
    
    def buscar_item(self, item_procurado):
        temp = Lista()
        encontrado = False
        itens_removidos = []
        
        while not self.estoque.is_empty():
            atual = self.estoque.pop()
            itens_removidos.append(atual)
            
            if atual == item_procurado:
                encontrado = True
                break
            
            temp.push(atual)
        
        # Devolvendo itens para o estoque
        if encontrado:
            print(f"Para acessar {item_procurado}, precisou remover: {itens_removidos[:-1]}")
        else:
            print(f"Item {item_procurado} não encontrado")
            # Adicionando todos de volta
            itens_removidos.reverse()
            for item in itens_removidos:
                self.estoque.push(item)
            return False
        
        # Devolvendo os itens temporários
        while not temp.is_empty():
            self.estoque.push(temp.pop())
        
        # Devolvendo o item encontrado
        self.estoque.push(item_procurado)
        return True


# Teste
almoxarifado = Almoxarifado()
almoxarifado.adicionar("Caneta")
almoxarifado.adicionar("Caderno") 
almoxarifado.adicionar("Régua")

print(f"Próximo item: {almoxarifado.proximo_item()}")
print(f"Total de itens: {almoxarifado.quantidade()}")

almoxarifado.buscar_item("Caneta")
almoxarifado.retirar()