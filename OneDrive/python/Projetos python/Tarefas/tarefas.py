class Tarefa:
    def __init__(self, titulo, descricao, status):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
    def __str__(self):
        return f'Titulo: {self.titulo}\nDescrição: {self.descricao}\nStatus:{self.status}'

class Atividade:
    def __init__(self):
        self.tarefas = []
    
    def adicionarObjeto(self, objeto):
        self.tarefas.append(objeto) 
    
    def removerObjeto(self, objeto):
        self.tarefas.remove(objeto)
    
    def criarTarefa(self):
        titulo = input("Digite o titulo da tarefa: ")
        descricao = input("Descreva a tarefa (Max 100 caracteres): ")
        print('')
        
        while len(descricao) > 100:
            print("Limite excedido! Digite novamente com até 100 palavras")
            descricao = input("Descreva novamente a tarefa (Max 100 caracteres): ")
        
        if len(descricao) < 100:
            status = 'Não iniciado'
            tarefa = Tarefa(titulo, descricao, status)
            
            self.adicionarObjeto(tarefa)
            
        
        print(tarefa)
        print('')
    
    def listarHistorico(self):
        print('Lista de tarefas: \n')
        for tarefa in self.tarefas:
            print(f'{tarefa} \n')    

    def redefinirStatus(self):
        tituloPesquisa = input("Digite o titulo da tarefa que deseja alterar o status: ")
        selecaoStatus = ['1. Em andamento', '2. Concluido']
        
        for tarefa in self.tarefas:
            if tarefa.titulo == tituloPesquisa:
                print(f"Tarefa {tituloPesquisa} encontrada! Selecione o status atual da tarefa:")
                for statusAtual in selecaoStatus:
                    print(statusAtual)
                alterarStatus = int(input('Digite uma das opções acima: '))
                if alterarStatus == 1:
                    tarefa.status = 'Em andamento'
                    print(f'Status alterado para "{tarefa.status}"')
                
                elif alterarStatus == 2:
                    tarefa.status = 'Concluido'
                    print(f'Status alterado para "{tarefa.status}"\n')
                    print(tarefa)
                
                else:
                    return
                
            else:
                print('Digite uma opção valida!')
    
    def procurarTarefa(self):
            procurarTitulo = input('Digite o titulo da tarefa que deseja identificar: ')
            encontrada = False
            
            for tarefa in self.tarefas:
                if tarefa.titulo == procurarTitulo:
                    print('')
                    encontrada = True
                    print('Tarefa detectada:')
                    print(f'{tarefa} \n')
            
            if not encontrada:
                print('Tarefa não detectada. Tente novamente!')
    
    def excluirTarefa(self):
        procurarTituloRemove = input('Digite o titulo da tarefa que deseja remover: ')
        encontrada = False
            
        for tarefa in self.tarefas:
            if tarefa.titulo == procurarTituloRemove:  
                print('')
                encontrada = True
                print('Tarefa detectada:')
                print(f'{tarefa} \n')
                validacaoRemove = input(f'Deseja remover a tarefa {tarefa.titulo}? (Digite[Sim] ou [Não])').upper().strip()
                
                if validacaoRemove == 'SIM':
                    self.removerObjeto(tarefa)
                    print(f'Tarefa {tarefa.titulo} removida!')
                    
                elif validacaoRemove == 'NÃO' or validacaoRemove == 'NAO' :
                    print(f'Você optou por não remover a tarefa {tarefa.titulo}')
            
            if not encontrada:
                print('Tarefa não detectada. Tente novamente!')
                    
                        

atividade = Atividade()

opcoes_menu = ['1. Criar tarefa', '2. Historico de tarefas', '3. redefinir status', '4. Procurar tarefa', '5. Remover tarefa', '6. Encerrar']

while True:
    print("Menu opções:")
    for i in opcoes_menu:
        print(i)

    try:
        menu = int(input("Selecione uma das opções: "))
        
        if menu == 1:
            atividade.criarTarefa()
        elif menu == 2:
            atividade.listarHistorico()
        elif menu == 3:
            atividade.redefinirStatus()
        elif menu == 4:
            atividade.procurarTarefa()
        elif menu == 5:
            atividade.excluirTarefa()
        elif menu == 6:
            print('Sistema encerrado!')
            break
        else:
            print("Opção inválida! Escolha um número entre 1 e 6.")

    except ValueError:
        print("Entrada inválida! Digite um número correspondente ao menu.")

        
        
        