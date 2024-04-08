class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, nome, descricao, prioridade, categoria):
        tarefa = {"nome": nome, "descricao": descricao, "prioridade": prioridade, "categoria": categoria, "concluida": False}
        self.tarefas.append(tarefa)

    def listar_tarefas(self):
        for idx, tarefa in enumerate(self.tarefas, start=1):
            print(f"{idx}. Nome: {tarefa['nome']}, Prioridade: {tarefa['prioridade']}, Categoria: {tarefa['categoria']}, Concluída: {tarefa['concluida']}")

    def marcar_tarefa_concluida(self, indice_tarefa):
        if 0 <= indice_tarefa < len(self.tarefas):
            self.tarefas[indice_tarefa]['concluida'] = True
            print("Tarefa marcada como concluída.")
        else:
            print("Índice de tarefa inválido.")

    def exibir_tarefas_por_prioridade(self, prioridade):
        tarefas_filtradas = [tarefa for tarefa in self.tarefas if tarefa['prioridade'] == prioridade]
        if tarefas_filtradas:
            for tarefa in tarefas_filtradas:
                print(f"Nome: {tarefa['nome']}, Prioridade: {tarefa['prioridade']}, Categoria: {tarefa['categoria']}, Concluída: {tarefa['concluida']}")
        else:
            print("Nenhuma tarefa encontrada com a prioridade fornecida.")

    def exibir_tarefas_por_categoria(self, categoria):
        tarefas_filtradas = [tarefa for tarefa in self.tarefas if tarefa['categoria'] == categoria]
        if tarefas_filtradas:
            for tarefa in tarefas_filtradas:
                print(f"Nome: {tarefa['nome']}, Prioridade: {tarefa['prioridade']}, Categoria: {tarefa['categoria']}, Concluída: {tarefa['concluida']}")
        else:
            print("Nenhuma tarefa encontrada com a categoria fornecida.")


def main():
    gerenciador = GerenciadorTarefas()
    
    while True:
        print("\n=== Menu do Gerenciador de Tarefas ===")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Exibir Tarefas por Prioridade")
        print("5. Exibir Tarefas por Categoria")
        print("6. Sair")
        
        escolha = input("Digite sua escolha: ")

        if escolha == '1':
            nome = input("Digite o nome da tarefa: ")
            descricao = input("Digite a descrição da tarefa: ")
            prioridade = input("Digite a prioridade da tarefa: ")
            categoria = input("Digite a categoria da tarefa: ")
            gerenciador.adicionar_tarefa(nome, descricao, prioridade, categoria)
            print("Tarefa adicionada com sucesso.")
        elif escolha == '2':
            gerenciador.listar_tarefas()
        elif escolha == '3':
            indice_tarefa = int(input("Digite o índice da tarefa para marcar como concluída: ")) - 1
            gerenciador.marcar_tarefa_concluida(indice_tarefa)
        elif escolha == '4':
            prioridade = input("Digite a prioridade para filtrar as tarefas: ")
            gerenciador.exibir_tarefas_por_prioridade(prioridade)
        elif escolha == '5':
            categoria = input("Digite a categoria para filtrar as tarefas: ")
            gerenciador.exibir_tarefas_por_categoria(categoria)
        elif escolha == '6':
            print("Saindo...")
            break
        else:
            print("Escolha inválida. Por favor, tente novamente.")


if __name__ == "__main__":
    main()