import os
import csv
from Graph import Graph
from Courier import Courier
from Node import Node  # Pode não ser preciso


class Main:
    def __init__(self):
        self.graph = Graph()
        self.couriers = loadCouriers()

    def mainPanel(self):
        saida = -1
        while saida != 0:
            print("1-Carregar Grafo")
            print("2-Imprimir Grafo")
            print("3-Desenhar Grafo")
            print("4-Imprimir nodos do Grafo")
            print("5-Imprimir arestas do Grafo")
            print("6-Algoritmos de procura")
            print("7-Imprimir estafetas")
            print("0-Sair")

            try:
                saida = int(input("Introduza a sua opção -> "))
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
                            self.graph.loadFromFile(l)
                            print("Loading was successful")
                            l2 = input("Prima Enter para continuar")
                            break
                elif saida == 2:
                    print(self.graph)
                    l = input("Prima Enter para continuar")
                elif saida == 3:
                    self.graph.desenha()
                elif saida == 4:
                    print(self.graph.m_graph.keys())
                    l = input("Prima Enter para continuar")
                elif saida == 5:
                    print(self.graph.imprime_aresta())
                    l = input("Prima Enter para continuar")
                elif saida == 6:
                    inicio = input("Nodo inicial -> ")
                    fim = input("Nodo final -> ")
                    print("1-DFS")
                    print("2-BFS")
                    print("3-Greedy")
                    print("4-A*")
                    print("5-Custo Uniforme")
                    print("6-Iterative DFS")
                    print("7-Iterative A*")
                    print("0-Sair")
                    exit = 1
                    while exit != 0:
                        exit = int(input("Introduza a sua opção -> "))
                        if exit == 1:
                            sol, custo = self.graph.procura_DFS(inicio, fim, path=[], visited=set())
                            print(sol, custo)
                            print(f"Bicileta: {custo / 10}")
                            print(f"Mota: {custo / 35}")
                            print(f"Carro: {custo / 50}")
                        elif exit == 2:
                            sol, custo = self.graph.procura_BFS(inicio, fim)
                            print(sol, custo)
                            print(f"Bicileta: {custo / 10}")
                            print(f"Mota: {custo / 35}")
                            print(f"Carro: {custo / 50}")
                        elif exit == 3:
                            print(self.graph.procura_Greedy(inicio, fim))
                        elif exit == 4:
                            print(self.graph.procura_aStar(inicio, fim))
                        elif exit == 5:
                            print(self.graph.procura_custoUniforme(inicio, fim))
                        elif exit == 6:
                            print(self.graph.procura_iterativeDFS(inicio, fim))
                        elif exit == 7:
                            print(self.graph.procura_iterativeAStar(inicio, fim))
                    l = input("Prima Enter para continuar")
                elif saida == 7:
                    for courier in self.couriers.values():
                        print(f"{courier.getName()};{courier.getNumber()};{courier.getRating()};{courier.getVehicle()};Free:{courier.getFree()}")
                    l = input("Prima Enter para continuar")
                else:
                    print("Opção Inválida...")
                    l = input("Prima Enter para continuar")
            except KeyboardInterrupt:
                print("\nA sair...")
                break


def loadCouriers():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, '..', 'db', 'couriers.csv')
    couriers = {}

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader, None)  # Para não inserir o header

        for row in reader:
            if len(row) == 5:
                name, number, rating, nrRatings, vehicle = row
                couriers[number] = Courier(name, vehicle, number, rating, nrRatings)
            else:
                print(f"Ignoring invalid row: {row}")

        return couriers


if __name__ == "__main__":
    Main().mainPanel()
