import os
from Graph import Graph
from Node import Node  # Pode não ser preciso


def main():
    g = Graph()

    saida = -1
    while saida != 0:
        print("1-Carregar Grafo")
        print("2-Imprimir Grafo")
        print("3-Desenhar Grafo")
        print("4-Imprimir nodos do Grafo")
        print("5-Imprimir arestas do Grafo")
        print("6-DFS")
        print("7-BFS")
        print("8-Greedy")
        print("9-A*")
        print("0-Sair")

        try:
            saida = int(input("introduza a sua opção -> "))
            if saida == 0:
                print("A sair...")
            elif saida == 1:
                while True:
                    print("Insira o nome do ficheiro a carregar ou prima 1 para ver as opções")
                    l = input()
                    if l == "1":
                        # Mostra os nomes dos ficheiros que podem ser carregados
                        graphs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'graphs')
                        files_in_graphs = os.listdir(graphs_dir)

                        print("Grafos disponíveis:")
                        for file_name in files_in_graphs:
                            print(file_name)

                        l2 = input("Prima Enter para continuar")
                    else:
                        g.loadFromFile(l)
                        print("Loading was successful")
                        l2 = input("Prima Enter para continuar")
                        break
            elif saida == 2:
                print(g)
                l = input("Prima Enter para continuar")
            elif saida == 3:
                g.desenha()
            elif saida == 4:
                print(g.m_graph.keys())
                l = input("Prima Enter para continuar")
            elif saida == 5:
                print(g.imprime_aresta())
                l = input("Prima Enter para continuar")
            elif saida == 6:
                inicio = input("Nodo inicial -> ")
                fim = input("Nodo final -> ")
                sol, custo = g.procura_DFS(inicio, fim, path=[], visited=set())
                print(sol, custo)
                print(f"Bicileta: {custo / 10}")
                print(f"Mota: {custo / 35}")
                print(f"Carro: {custo / 50}")
                l = input("Prima Enter para continuar")
            elif saida == 7:
                inicio = input("Nodo inicial -> ")
                fim = input("Nodo final -> ")
                sol, custo = g.procura_BFS(inicio, fim)
                print(sol, custo)
                print(f"Bicileta: {custo / 10}")
                print(f"Mota: {custo / 35}")
                print(f"Carro: {custo / 50}")
                l = input("Prima Enter para continuar")
            elif saida == 8:
                inicio = input("Nodo inicial -> ")
                fim = input("Nodo final -> ")
                print(g.procura_Greedy(inicio, fim))
                l = input("Prima Enter para continuar")
            elif saida == 9:
                inicio = input("Nodo inicial -> ")
                fim = input("Nodo final -> ")
                print(g.procura_aStar(inicio, fim))
                l = input("Prima Enter para continuar")
            else:
                print("Opção Inválida...")
                l = input("Prima Enter para continuar")
        except KeyboardInterrupt:
            print("\nA sair...")
            break


if __name__ == "__main__":
    main()
