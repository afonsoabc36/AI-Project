import os
import csv
from Graph import Graph
from Courier import Courier
from Package import Package
from Vehicle import Vehicle
from Node import Node


class Main:
    def __init__(self):
        self.graph = Graph()
        self.graph.loadFromFile('braga.csv')
        self.couriers = loadCouriers()
        self.time = '29/12/2023T09:00'
        self.packages = self.loadPackages()
        self.deliveredPackages = {}
        self.vehicleList = ['Bicycle', 'Motorcycle', 'Car']
        self.courierWage = 4.32

    def mainPanel(self):
        saida = -1
        while saida != 0:
            print("1-Carregar outro grafo")
            print("2-Opções sobre o grafo")
            print("3-Algoritmos de procura")
            print("4-Imprimir estafetas")
            print("5-Imprimir pacotes por entregar")
            print("6-Imprimir pacotes entregues")
            print("7-Associar encomendas a um estafeta")
            print("8-Entregar uma encomenda")
            print("9-Avaliar uma entrega")
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
                                self.graph.setName(l)
                                l2 = input("Prima Enter para continuar")
                                break
                            else:
                                print(f"Ficheiro {l} não existe, tente novamente")
                elif saida == 2:
                    print("1-Imprimir Grafo")
                    print("2-Desenhar Grafo")
                    print("3-Imprimir nodos do Grafo")
                    print("4-Imprimir arestas do Grafo")
                    print("5-Adicionar congestionamento")
                    print("6-Adicionar estradas cortadas")
                    print("7-Adicionar ligação")
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
                        elif exit1 == 5:
                            wrongLocations = True
                            while wrongLocations:
                                inicio = input("Nodo 1 -> ")
                                fim = input("Nodo 2 -> ")
                                if Node(inicio) in self.graph.m_nodes and Node(fim) in self.graph.m_nodes:
                                    wrongLocations = False
                                if Node(inicio) not in self.graph.m_nodes:
                                    print(f"{inicio} não é uma localização no grafo, insira outro local")
                                if Node(fim) not in self.graph.m_nodes:
                                    print(f"{fim} não é uma localização no grafo, insira outro local")

                            while True:
                                print("Insira o nível de congestionamento")
                                print("1-Leve")
                                print("2-Médio")
                                print("3-Elevado")
                                l = int(input())

                                if 0 < l < 4:
                                    if not (self.graph.addTraffic(l,inicio,fim)):
                                        print(f"Não há ligação direta entre {inicio} e {fim}")
                                    break
                                else:
                                    print("Valor inválido. Tente novamente")
                        elif exit1 == 6:
                            wrongLocations = True
                            while wrongLocations:
                                inicio = input("Nodo 1 -> ")
                                fim = input("Nodo 2 -> ")
                                if Node(inicio) in self.graph.m_nodes and Node(fim) in self.graph.m_nodes:
                                    wrongLocations = False
                                if Node(inicio) not in self.graph.m_nodes:
                                    print(f"{inicio} não é uma localização no grafo, insira outro local")
                                if Node(fim) not in self.graph.m_nodes:
                                    print(f"{fim} não é uma localização no grafo, insira outro local")

                            if not (self.graph.blockRoad(inicio,fim)):
                                print("Não há ligação direta ou a remoção isola um dos nodos, quer continuar?")
                                print("1-Sim")
                                print("0-Não")
                                l = int(input())
                                if l == 1:
                                    self.graph.blockRoad(inicio,fim,True)
                            else:
                                print(f"Ligação entre {inicio} e {fim} removida")
                        elif exit1 == 7:
                            wrongLocations = True
                            while wrongLocations:
                                inicio = input("Nodo 1 -> ")
                                fim = input("Nodo 2 -> ")
                                if Node(inicio) in self.graph.m_nodes and Node(fim) in self.graph.m_nodes:
                                    wrongLocations = False
                                if Node(inicio) not in self.graph.m_nodes:
                                    print(f"{inicio} não é uma localização no grafo, insira outro local")
                                if Node(fim) not in self.graph.m_nodes:
                                    print(f"{fim} não é uma localização no grafo, insira outro local")

                            weight = int(input("Insira a distância entre os nodos: "))
                            while True:
                                if weight > 0:
                                    self.graph.add_edge(inicio, fim, weight)
                                    print(f"Ligação entre {inicio} e {fim} com peso {weight} inserida com sucesso")
                                    break
                                else:
                                    print("Insira um valor superior a 0")

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
                        else:
                            print()
                        print(sol, cost)
                    l = input("Prima Enter para continuar")
                elif saida == 4:
                    for courier in self.couriers.values():
                        print(
                            f"{courier.getName()};{courier.getNumber()};{courier.getRating()};{courier.getVehicle()};Free:{courier.getFree()}")
                    l = input("Prima Enter para continuar")
                elif saida == 5:
                    for package in self.packages.values():
                        print(package)
                    l = input("Prima Enter para continuar")
                elif saida == 6:
                    for package in self.deliveredPackages.values():
                        print(package)
                    l = input("Prima Enter para continuar")
                elif saida == 7:
                    for package in self.packages.values():
                        print(package)
                    print("Insira o número das encomendas que quer associar 1 a 1, insira -1 para parar")
                    packagesToInsert = {}
                    aux = True
                    while aux:
                        packageNumber = int(input())
                        if packageNumber == -1:
                            aux = False
                        elif packageNumber in self.packages.keys():
                            packagesToInsert[packageNumber] = self.packages.get(packageNumber)
                        else:
                            print("Pacote não existente")
                    print("Insira o ID do estafeta ou 0 para sair:")
                    for courier in self.couriers.values():
                        print(courier)
                    aux = True
                    while aux:
                        courierID = int(input())
                        if courierID == 0:
                            aux = False
                        elif courierID in self.couriers.keys():
                            self.couriers[courierID].addDeliveries(packagesToInsert)
                            print("Pacotes associados ao estafeta")
                            aux = False
                        else:
                            print("ID inválido, insira novamente")
                elif saida == 8:
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
                    if len(courierDeliveries) == 0:
                        print(f"Entregador {self.couriers.get(courierID).getName()} não tem encomendas associadas")
                        break
                    for package in courierDeliveries.values():
                        print(package)
                    aux = True
                    while aux:
                        packageID = int(input())
                        if packageID in courierDeliveries.keys():
                            aux = False
                        else:
                            print("ID inválido, insira novamente")

                    packageToDeliver = self.packages.get(packageID)
                    sol, cost = self.graph.procura_aStar(packageToDeliver.getDestination(), 'Gualtar')
                    sol.reverse()

                    print("Melhor caminho: ", sol)
                    print("Distância: ", cost, "km")

                    delivery = [packageToDeliver]

                    aux = False
                    for package in courierDeliveries.values():
                        if package.getId() == packageID:
                            continue
                        if package.getDestination() in sol:
                            aux = True
                            break
                    tamanho = 1
                    if aux:
                        print("Deseja entregar outras encomendas pelo caminho?")
                        print("Nota, isto pode causar atrasos na entrega da encomenda que pretende entregar")
                        print("1-Sim")
                        print("0-Não")
                        l = int(input())
                        if l == 1:
                            totalWeight = 0
                            for package in courierDeliveries.values():
                                if package.getPackageId() == packageID:
                                    continue
                                possibleWeight = totalWeight + package.getWeight()
                                if package.getDestination() in sol and possibleWeight < Vehicle(
                                        'Car').getTotalMaxWeight():
                                    delivery.append(package)
                        tamanho = len(delivery)
                        if tamanho > 1:
                            print(f"A entregar {tamanho} pacotes")
                        else:
                            print(f"A entregar {tamanho} pacote")

                    data = {}
                    for item in self.vehicleList:
                        vehicle = Vehicle(item)
                        time = round(self.graph.calculaTempoVeiculo(sol, vehicle, delivery), 2)
                        tripCost = round(vehicle.getTripCost(cost, time, self.courierWage), 2)
                        data[item] = (time, tripCost)
                        hours = int(time)
                        minutes = int((time - hours) * 60)
                        print(f"Time expected with {item}: {hours}h{minutes}m")
                        print(f"Cost of the trip: {tripCost}")

                    vehicle = ""
                    deliveryWeight = 0
                    for pack in delivery:
                        deliveryWeight += pack.getWeight()

                    while True:
                        print("\n1-Escolha mais rápida")
                        print("2-Escolha mais económica")
                        print("3-Escolha ecológica")
                        print("4-Entrega com um veículo em específico")
                        l = int(input())

                        if l == 1:
                            minTime = float('inf')
                            for key, (time, tripCost) in data.items():
                                if time < minTime and Vehicle(key).canDeliver(deliveryWeight):
                                    vehicle = key
                                    minTime = time
                            break
                        elif l == 2:
                            minCost = float('inf')
                            for key, (time, tripCost) in data.items():
                                if tripCost < minCost and Vehicle(key).canDeliver(deliveryWeight):
                                    vehicle = key
                                    minCost = tripCost
                            break
                        elif l == 3:
                            carbonEmission = float('inf')
                            vehicle = ""
                            for item in self.vehicleList:
                                choice = Vehicle(item)
                                if choice.canDeliver(deliveryWeight):
                                    carbonTotal = choice.getCarbonEmission() * cost
                                    if carbonTotal < carbonEmission:
                                        carbonEmission = carbonTotal
                                        vehicle = item
                            break
                        elif l == 4:
                            print("Opções dispovíveis:")
                            options = []
                            for item in self.vehicleList:
                                if Vehicle(item).canDeliver(deliveryWeight):
                                    print(item)
                                    options.append(item)
                            while True:
                                print("Insira a sua escolha:")
                                vehicle = input()
                                if vehicle not in options:
                                    print(f"{vehicle} não existe, tente novamente")
                                else:
                                    break
                            break
                        else:
                            print("Escolha inválida, tente novamente")

                    if not (self.onTime(delivery, sol, vehicle)):
                        print("Este método de envio faz com que o pacote não chegue a horas, quer continuar?")
                        print("1-Sim")
                        print("0-Não")
                        l = int(input())
                        if l == 0:
                            continue

                    print(f"A entregar a encomenda com {vehicle}, confirma?")
                    print("1-Sim")
                    print("0-Não")
                    while True:
                        l = int(input())
                        if l == 1:
                            self.deliver(delivery, cost, courierID, vehicle)
                            break
                        elif l == 0:
                            print("A cancelar a entrega")
                            break
                        else:
                            print("Escolha inválida, tente novamente")
                elif saida == 9:
                    while True:
                        print("Insira o número da encomenda a avaliar:")
                        for package in self.deliveredPackages.values():
                            if package.notReviewed():
                                print(package)
                        packageID = int(input())
                        if packageID not in self.deliveredPackages.keys():
                            print(f"Pacote {packageID} não existe, insira novamente")
                            continue
                        packageToReview = self.deliveredPackages.get(packageID)

                        while True:
                            print("Insira uma avaliação de 1 a 5 à entrega:")
                            packageRating = int(input())
                            if 1 <= packageRating <= 5:
                                break
                            else:
                                print("Avaliação inválida, insira um número de 1 a 5")

                        packageToReview.setRating(packageRating)
                        self.couriers.get(packageToReview.getCourier()).updateRating(packageRating)
                        break
                else:
                    print("Opção Inválida...")
                    l = input("Prima Enter para continuar")
            except KeyboardInterrupt:
                print("\nA sair...")
                break
            except ValueError:
                print("Entrada inválida.")

    def deliver(self, delivery, distance, courierID, vehicle):
        for package in delivery:
            packageID = package.getId()
            self.packages.pop(packageID, None)
            package.setPrice(distance, vehicle)
            package.setCourier(courierID)
            self.deliveredPackages[packageID] = package

    def timeToEachLocation(self, path, listOfDestinations, item, delivery):
        dictionary = {}
        counter = 0
        for destination in listOfDestinations:
            sol, cost = self.graph.procura_aStar(destination, 'Gualtar')
            vehicle = Vehicle(item)
            time = round(self.graph.calculaTempoVeiculo(sol, vehicle, delivery), 2)
            hours = int(time)
            minutes = int((time - hours) * 60)
            dictionary[destination] = minutes + counter
            counter += 2
        return dictionary

    def onTime(self, delivery, solution, vehicle):
        stops = []
        for package in delivery:
            destination = package.getDestination()
            if destination not in stops:
                stops.append(destination)

        arrivalTime = self.timeToEachLocation(solution, stops, vehicle,delivery)

        onTime = True
        for package in delivery:
            if not (package.arriveOnTime(arrivalTime[package.getDestination()], self.time)):
                onTime = False
                break

        return onTime

    def loadPackages(self):
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
                    packages[packageId] = Package(packageId, weight, volume, deliveryDate, destination, self.time)
                else:
                    print(f"Ignoring invalid row: {row}")

            return packages


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


if __name__ == "__main__":
    Main().mainPanel()
