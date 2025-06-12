#inicialização do nó
class Node:
    def __init__(self, content):
        self.content = content #corresponde a pergunta ou resposta do paciente
        self.left = None #lado esquerdo - 'sim'
        self.right = None #lado direito - 'não'
    
    #método para verificar se há filhos, se não tiver esse é o último elemento da árvore (vazio)
    def isLeaf(self):
        return self.left is None and self.right is None

#lógica das perguntas de decisão da árvore
class DecisionTree:
    def __init__(self):
        #estrutura inicial
        self.root = self.buildTree()
    
    def buildTree(self):
        #definindo as classificações de risco
        red = Node("Vermelho - Atendimento imediato")
        yellow = Node("Amarelo - Atendimento urgente") 
        green = Node("Verde - Pouco urgente")
        blue = Node("Azul - Sem urgência")
        
        #iniciando as perguntas pelas mais urgentes (final da árvore)
        case5 = Node("Está se sentindo muito fraco ou tonto?")
        case5.left = green  # CORRIGIDO: era 'verde' (não existe)
        case5.right = blue  # CORRIGIDO: era 'azul' (não existe)
        
        #pergunta sobre febre
        case4 = Node("Tem febre acima de 38°C?")
        case4.left = yellow #sim = amarelo
        case4.right = case5 #não = pergunta 5 (case5)
        
        #pergunta sobre intensidade da dor
        case3 = Node("A dor é forte ou insuportável?")
        case3.left = yellow #sim = amarelo
        case3.right = case4 #não = pergunta 4 (case4)
        
        #pergunta se tem dor
        case2 = Node("Está sentindo dor?")
        case2.left = case3 #sim = pergunta 3 (case3)
        case2.right = case4 #não = pergunta 4 (case4)
        
        #pergunta principal (primeira pergunta do sistema)
        case1 = Node("Está com falta de ar?")
        case1.left = red #sim = urgencia (transferido para a sistuação de urgencia)
        case1.right = case2  #não = prossegue para pergunta 2 (case2)
        
        #retorna a raiz da árvore
        return case1
    
    #interação inicial do sistema
    def start(self):
        print("Bem-vindo ao Sistema de Triagem Virtual!!")
        print("Responda com 'sim' ou 'não' às perguntas abaixo:\n")
        
        self.traverse(self.root)
    
    #método recursivo responsável pela navegação pela árvore
    def traverse(self, node):
        #ponto de parada: elemento "vazio", sem filhos
        if node.isLeaf():
            print(f"\nClassificação: {node.content}")
            return  
        
        #pergunta recursiva
        resposta = input(f"{node.content} (sim/não): ").strip().lower()
        
        #validação binária, sim ou não
        while resposta not in ['sim', 'não']:
            resposta = input("Por favor, responda apenas com 'sim' ou 'não': ").strip().lower()
        
        #tomada de decisão entre os caminhos
        if resposta == 'sim':
            self.traverse(node.left) #percorre o filho esquerdo
        else:
            self.traverse(node.right) #percorre o filho direito

#testes
triagem = DecisionTree() #instância da árvore
triagem.start() #iniciando o sistema de triagem
