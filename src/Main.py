import os
import csv
from Graph import Graph
from Courier import Courier
from Package import Package
from Node import Node


class Main:
    def __init__(self):
        self.graph = Graph()
        self.graph.loadFromFile('braga.csv')
        self.couriers = loadCouriers()
        self.packages = loadPackages()

    def mainPanel(self):
        saida = -1
        while saida != 0:
            print("1-Carregar outro grafo")
            print("2-Opções sobre o grafo")
            print("3-Algoritmos de procura")
            print("4-Imprimir estafetas")
            print("5-Imprimir pacotes")
            print("6-Associar encomendas a um estafeta")
            print("7-Entregar uma encomenda")
            print("0-Sair")

            try:
                saida = int(input("Introduza a sua opção -> "))
                if saida == 0:
                    print("A sair...")
                elif saida == 1:
                    while True:
                        print("Insira o nome do ficheiro a carregar ou 1 para ver as opções")
                        l = input()
                        graphs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'graphs')
                        filesInGraphs = os.listdir(graphs_dir)
                        if l == "1":
                            # Mostra os nomes dos ficheiros que podem ser carregados
                            print("Grafos disponíveis:")
                            for file_name in filesInGraphs:
                                print(file_name)

                            l2 = input("Prima Enter para continuar")
                        else:
                            if l in filesInGraphs:
                                self.graph.loadFromFile(l)
                                print("Loading was successful")
                                l2 = input("Prima Enter para continuar")
                                break
                            else:
                                print(f"Ficheiro {l} não existe, tente novamente")
                elif saida == 2:
                    print("1-Imprimir Grafo")
                    print("2-Desenhar Grafo")
                    print("3-Imprimir nodos do Grafo")
                    print("4-Imprimir arestas do Grafo")
                    print("0-Sair")
                    exit1 = 1
                    while exit1 != 0:
                        exit1 = int(input("Introduza a sua opção -> "))
                        if exit1 == 1:
                            print(self.graph)
                        elif exit1 == 2:
                            self.graph.desenha()
                        elif exit1 == 3:
                            print(self.graph.m_graph.keys())
                        elif exit1 == 4:
                            print(self.graph.imprime_aresta())
                    l = input("Prima Enter para continuar")
                elif saida == 3:
                    wrongLocations = True
                    while wrongLocations:
                        inicio = input("Nodo inicial -> ")
                        fim = input("Nodo final -> ")
                        if Node(inicio) in self.graph.m_nodes and Node(fim) in self.graph.m_nodes:
                            wrongLocations = False
                        if Node(inicio) not in self.graph.m_nodes:
                            print(f"{inicio} não é uma localização no grafo, insira outro local")
                        if Node(fim) not in self.graph.m_nodes:
                            print(f"{fim} não é uma localização no grafo, insira outro local")

                    print("1-DFS")
                    print("2-BFS")
                    print("3-Greedy")
                    print("4-A*")
                    print("5-Custo Uniforme")
                    print("6-Iterative DFS")
                    print("7-Iterative A*")
                    print("0-Sair")
                    exit2 = 1
                    while exit2 != 0:
                        exit2 = int(input("Introduza a sua opção -> "))
                        if exit2 == 1:
                            sol, cost = self.graph.procura_DFS(inicio, fim)
                        elif exit2 == 2:
                            sol, cost = self.graph.procura_BFS(inicio, fim)
                        elif exit2 == 3:
                            sol, cost = self.graph.procura_Greedy(inicio, fim)
                        elif exit2 == 4:
                            sol, cost = self.graph.procura_aStar(inicio, fim)
                        elif exit2 == 5:
                            sol, cost = self.graph.procura_custoUniforme(inicio, fim)
                        elif exit2 == 6:
                            sol, cost = self.graph.procura_iterativeDFS(inicio, fim)
                        elif exit2 == 7:
                            sol, cost = self.graph.procura_iterativeAStar(inicio, fim)
                        elif exit2 == 0:
                            break
                        print(sol, cost)
                        print(f"Bicileta: {cost / 10}")
                        print(f"Mota: {cost / 35}")
                        print(f"Carro: {cost / 50}")
                    l = input("Prima Enter para continuar")
                elif saida == 4:
                    for courier in self.couriers.values():
                        print(f"{courier.getName()};{courier.getNumber()};{courier.getRating()};{courier.getVehicle()};Free:{courier.getFree()}")
                    l = input("Prima Enter para continuar")
                elif saida == 5:
                    for package in self.packages.values():
                        print(f"{package.getId()};{package.getWeight()};{package.getVolume()};{package.getDeliveryDate()};{package.getPrice()};{package.getDestination()}")
                    l = input("Prima Enter para continuar")
                elif saida == 6:
                    for package in self.packages.values():
                        print(package)
                    print("Insira o número das encomendas que quer associar 1 a 1, clique -1 para parar")
                    packagesToInsert = []
                    aux = True
                    while aux:
                        packageNumber = int(input())
                        if packageNumber == -1:
                            aux = False
                        elif packageNumber in self.packages.keys():
                            packagesToInsert.append(packageNumber)
                        else:
                            print("Pacote não existente")
                    print("Insira o ID do estafeta:")
                    for courier in self.couriers.values():
                        print(courier)
                    aux = True
                    while aux:
                        courierID = int(input())
                        if courierID in self.couriers.keys():
                            aux = False
                        else:
                            print("ID inválido, insira novamente")
                    self.couriers[courierID].addDeliveries(packagesToInsert)
                    print("Pacotes associados ao estafeta")
                elif saida == 7:
                    print("Insira o ID do estafeta:")
                    for courier in self.couriers.values():
                        print(courier)
                    aux = True
                    while aux:
                        courierID = int(input())
                        if courierID in self.couriers.keys():
                            aux = False
                        else:
                            print("ID inválido, insira novamente")
                    print("Insira o ID da encomenda:")
                    courierDeliveries = self.couriers.get(courierID).getDeliveries()
                    for package in courierDeliveries:
                        print(package)
                    aux = True
                    while aux:
                        packageID = int(input())
                        if packageID in courierDeliveries:
                            aux = False
                        else:
                            print("ID inválido, insira novamente")
                    # TODO: GetFastestOption
                    # TODO: GetLessConsumingOption
                    # TODO: Add other packages that are on the way, if location in sol = [node]
                    # TODO: Add check for bad input, if not an int
                    # TODO: When delivered, add a price depending on the rush and the delivery method
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
                number = int(number)
                nrRatings = int(nrRatings)
                rating = float(rating)
                couriers[number] = Courier(name, vehicle, number, rating, nrRatings)
            else:
                print(f"Ignoring invalid row: {row}")

        return couriers


def loadPackages():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, '..', 'db', 'packages.csv')
    packages = {}  # TODO: HashMap may not be the best, maybe sorted array by destination or due date

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        # Ler o packageId do csv e atualizar quando o programa fechar
        # next(reader, None) para ignorar uma linha vazia
        packageIdLine = next(reader, None)
        if packageIdLine and len(packageIdLine) == 1:
            Package.packageId = int(packageIdLine[0])
        else:
            print("Error in reading the package id")
            return packages

        next(reader, None)  # Para não inserir o header

        for row in reader:
            if len(row) == 4:
                weight, volume, deliveryDate, destination = row
                # TODO: Maybe inserir bool de delivered ou não
                weight = float(weight)
                volume = float(volume)
                packageId = Package.getPackageId()
                packages[packageId] = Package(packageId, weight, volume, deliveryDate, destination)
            else:
                print(f"Ignoring invalid row: {row}")

        return packages


if __name__ == "__main__":
    Main().mainPanel()
