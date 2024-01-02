import networkx as nx
import matplotlib.pyplot as plt
import math
import csv
import os
from Node import Node
from Vehicle import Vehicle
from queue import Queue
from queue import PriorityQueue


class Graph:

    def __init__(self, directed=False):
        self.m_name = 'braga.csv'
        self.m_nodes = []
        self.m_directed = directed
        self.m_graph = {}
        self.m_h = {}

    def __str__(self):
        out = ""
        for key in self.m_graph.keys():
            out = out + "node" + str(key) + ": " + str(self.m_graph[key]) + "/n"
        return out

    def getName(self):
        return self.m_name

    def setName(self, name):
        self.m_name = name

    def add_edge(self, node1, node2, weight):
        n1 = Node(node1)
        n2 = Node(node2)
        if n1 not in self.m_nodes:
            self.m_nodes.append(n1)
            self.m_graph[node1] = set()
        else:
            n1 = self.get_node_by_name(node1)

        if n2 not in self.m_nodes:
            self.m_nodes.append(n2)
            self.m_graph[node2] = set()
        else:
            n2 = self.get_node_by_name(node2)

        self.m_graph[node1].add((node2, weight))

        # Se o grafo for não direcionado, colocar a aresta inversa
        if not self.m_directed:
            self.m_graph[node2].add((node1, weight))

    def loadFromFile(self, filename):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, '..', 'graphs', filename)

        if not os.path.exists(file_path):
            print(f"Error: File '{filename}' not found in 'graphs' directory.")
            return

        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            adding_edges = True  # Flag to indicate whether to add edges or heuristic values
            next(reader, None)  # Para não inserir o primeiro header

            for row in reader:
                if not row:  # Blank line
                    adding_edges = False  # Trocar para adicionar heurísticas
                    next(reader, None)  # Para não inserir o segundo header
                elif adding_edges and len(row) == 3:
                    node1, node2, weight = row
                    self.add_edge(node1, node2, int(weight))
                elif not adding_edges and len(row) == 2:
                    # Assuming it's the second format (Node, Heuristica)
                    node, heuristica = row
                    if heuristica != "":
                        self.add_heuristica(node, int(heuristica))
                else:
                    print(f"Ignoring invalid row: {row}")

    def get_node_by_name(self, name):
        search_node = Node(name)
        for node in self.m_nodes:
            if node == search_node:
                return node
            else:
                return None

    def add_heuristica(self, node, estima):
        n1 = Node(node)
        if n1 in self.m_nodes:
            self.m_h[node] = estima

    def heuristica(self):
        nodos = self.m_graph.keys()
        for n in nodos:
            self.m_h[n] = 1  # define a heuristica para cada nodo como 1
        return True  # A atribuição de heuristica foi concluida com sucesso

    def getH(self, node):
        return self.m_h[node]

    def getNeighbours(self, nodo):
        lista = []
        for (adjacente, peso) in self.m_graph[nodo]:
            lista.append((adjacente, peso))
        return lista

    def getNodes(self):
        return self.m_nodes

    def get_arc_cost(self, node1, node2):
        custoT = math.inf
        a = self.m_graph[node1]
        for (nodo, custo) in a:
            if nodo == node2:
                custoT = custo
        return custoT

    def calcula_custo(self, caminho):
        # caminho até uma lista de nodes
        teste = caminho
        custo = 0
        i = 0
        while i + 1 < len(teste):
            custo = custo + self.get_arc_cost(teste[i], teste[i + 1])
            i = i + 1
        return custo

    def calculaTempoVeiculo(self, sol, veiculo, packages, stops=1):
        weight = 0
        # TODO: Calcular o n de paragens através do sol e dos packages
        for package in packages:
            weight += package.getWeight()
        return self.calcula_custo(sol) / veiculo.effectiveSpeed(weight) + (0.033 * stops)  # 2 minutos por paragem
        # TODO: Retorna -1 se o peso for demasiado para o tipo de veículo

    def imprime_aresta(self):
        listaA = ""
        for nodo in self.m_graph.keys():
            for (nodo2, custo) in self.m_graph[nodo]:
                listaA = listaA + nodo + " -> " + nodo2 + "  custo: " + str(custo) + ("\n")
        return listaA

    def desenha(self):
        lista_v = self.m_nodes
        lista_a = []
        g = nx.Graph()

        for nodo in lista_v:
            n = nodo.getName()
            g.add_node(n)
            for (adjacente, peso) in self.m_graph[n]:
                lista = (n, adjacente)
                # lista_a.append(lista)
                g.add_edge(n, adjacente, weight=peso)

        pos = nx.spring_layout(g)
        nx.draw_networkx(g, pos, with_labels=True, font_weight='bold')
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)
        plt.draw()
        plt.show()

    def getFastestOption(self, destination):
        # Initialize variables to keep track of the best solution and cost
        bestSol = None
        bestCusto = float('inf')  # Initialize with positive infinity

        # Check DFS
        sol, custo = self.procura_DFS(destination, 'Gualtar')
        if custo < bestCusto:
            bestSol, bestCusto = sol, custo

        # Check BFS
        sol, custo = self.procura_BFS(destination, 'Gualtar')
        if custo < bestCusto:
            bestSol, bestCusto = sol, custo

        # Check Greedy
        sol, custo = self.procura_Greedy(destination, 'Gualtar')
        if custo < bestCusto:
            bestSol, bestCusto = sol, custo

        # Check A* (replace with your actual arguments)
        sol, custo = self.procura_aStar(destination, 'Gualtar')
        if custo < bestCusto:
            bestSol, bestCusto = sol, custo

        # Check Uniform Cost (replace with your actual arguments)
        sol, custo = self.procura_custoUniforme(destination, 'Gualtar')
        if custo < bestCusto:
            bestSol, bestCusto = sol, custo

        # Check Iterative DFS (replace with your actual arguments)
        sol, custo = self.procura_iterativeDFS(destination, 'Gualtar')
        if custo < bestCusto:
            bestSol, bestCusto = sol, custo

        # Check Iterative A* (replace with your actual arguments)
        sol, custo = self.procura_iterativeAStar(destination, 'Gualtar')
        if custo < bestCusto:
            bestSol, bestCusto = sol, custo

        # Return the best solution and cost
        return bestSol, bestCusto


    ######################################################
    # Procura DFS
    ######################################################
    def procura_DFS(self, start, end, path=[], visited=set()):
        path.append(start)
        visited.add(start)

        if start == end:
            custoT = self.calcula_custo(path)
            return (path, custoT)
        for (adjacente, peso) in self.m_graph[start]:
            if adjacente not in visited:
                resultado = self.procura_DFS(adjacente, end, path, visited)
                if resultado is not None:
                    return resultado
        path.pop()
        return None

    #####################################################
    # Procura BFS
    ######################################################

    def procura_BFS(self, start, end):
        # definir nodos visitados, para evitar ciclos
        visited = set()
        fila = Queue()
        custo = 0
        # adicionar o nodo inicial à fila e aos visitados
        fila.put(start)
        visited.add(start)
        # garantir que o start node não tem pais
        parent = dict()
        parent[start] = None

        path_found = False
        while not fila.empty() and path_found == False:
            node_atual = fila.get()
            if node_atual == end:
                path_found = True
            else:
                for (adjacente, peso) in self.m_graph[node_atual]:
                    if adjacente not in visited:
                        fila.put(adjacente)
                        parent[adjacente] = node_atual
                        visited.add(adjacente)

        # construir o caminho
        path = []
        if path_found:
            path.append(end)
            while parent[end] is not None:
                path.append(parent[end])
                end = parent[end]
            path.reverse()
            # função que calcula custa caminho
            custo = self.calcula_custo(path)
        return (path, custo)

    #####################################################
    # Procura Greedy
    ######################################################

    def procura_Greedy(self, start, end):
        open_list = set([start])  # lista de nodos visitados, mas com vizinhos que ainda não foram visitados
        closed_list = set([])  # lista de nodos visitados
        parents = {}  # dicionário que mantem o antecessor de um nodo
        parents[start] = start
        while len(open_list) > 0:
            n = None
            # encontra nodo com a menor heuristica
            for v in open_list:
                if n is None or self.m_h[v] < self.m_h[n]:
                    n = v
            if n is None:
                print('Path does not exist!')
                return None
            if n == end:
                recons_path = []
                while parents[n] != n:
                    recons_path.append(n)
                    n = parents[n]
                recons_path.append(start)
                recons_path.reverse()
                return (recons_path, self.calcula_custo(recons_path))
            for (m, weight) in self.getNeighbours(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
            open_list.remove(n)
            closed_list.add(n)
        print('Path does not exist!')
        return None

    #####################################################
    # Procura A*
    #####################################################

    def procura_aStar(self, start, end):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = {start}
        closed_list = set([])

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[start] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start] = start
        # n = None
        while len(open_list) > 0:
            # find a node with the lowest value of f() - evaluation function
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n is None or g[v] + self.getH(v) < g[n] + self.getH(n):
                    n = v
            if n is None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == end:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start)

                reconst_path.reverse()

                return (reconst_path, self.calcula_custo(reconst_path))

            # for all neighbors of the current node do
            for (m, weight) in self.getNeighbours(n):  # definir função getneighbours  tem de ter um par nodo peso
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

    #####################################################
    # Custo Uniforme
    #####################################################

    def procura_custoUniforme(self, start, end):
        # Priority queue for UCS
        priority_queue = PriorityQueue()

        # Enqueue the start node with cost 0
        priority_queue.put((0, start))

        # Initialize visited set
        visited = set()

        # Dictionary to store the cost to reach each node along with the previous node
        cost_so_far = {start: (0, None)}

        while not priority_queue.empty():
            # Dequeue the node with the lowest cost
            current_cost, current_node = priority_queue.get()

            # Check if the goal node is reached
            if current_node == end:
                # Reconstruct the path
                path = [current_node]
                while current_node != start:
                    # Ensure that the current_node is in cost_so_far before trying to access it
                    if current_node not in cost_so_far:
                        print('Node not found.')
                        return None
                    aux = True
                    while aux:
                        current_node = cost_so_far[current_node][1]
                        if current_node in path:
                            del cost_so_far[current_node]
                        else:
                            aux = False
                    path.append(current_node)
                path.reverse()
                return path, current_cost

            # Mark the current node as visited
            visited.add(current_node)

            # Explore neighbors
            for neighbor, weight in self.getNeighbours(current_node):
                new_cost = current_cost + weight
                if neighbor not in visited:
                    # Update cost and enqueue the neighbor
                    cost_so_far[neighbor] = (new_cost, current_node)
                    priority_queue.put((new_cost, neighbor))
                    visited.add(neighbor)

        print('Path does not exist!')
        return None

    #####################################################
    # Iterative DFS
    #####################################################

    def procura_iterativeDFS(self, start, end, max_depth=100):
        for depth_limit in range(1, max_depth + 1):
            result = self.DFS_recursive(start, end, depth_limit, set())
            if result is not None:
                path, cost = result
                return path, cost

        print(f'Path does not exist within the depth limit of {max_depth}.')
        return None

    def DFS_recursive(self, current_node, end, depth_limit, visited):
        if current_node == end:
            return ([current_node], 0)

        if depth_limit == 0:
            return None

        visited.add(current_node)

        for neighbor, weight in self.getNeighbours(current_node):
            if neighbor not in visited:
                result = self.DFS_recursive(neighbor, end, depth_limit - 1, visited)
                if result is not None:
                    path, cost = result
                    return ([current_node] + path, cost + weight)

        return None

    #####################################################
    # Iterative A*
    #####################################################

    def procura_iterativeAStar(self, start, end, max_depth=100):
        for depth_limit in range(1, max_depth + 1):
            result = self.aStar_recursive(start, start, end, depth_limit)
            if result is not None:
                path, cost = result
                return path, cost

        print(f'Path does not exist within the depth limit of {max_depth}.')
        return None

    def aStar_recursive(self, start, current_node=None, end=None, depth_limit=100, visited=None):
        # Initialize visited set and depth_limit
        if visited is None:
            visited = set()

        # Local dictionary to keep track of parents and g_values
        parent = {}

        def reconstruct_path(node):
            path = [node]
            while node != start:
                if node not in parent:
                    print('Error: Node not found in parent dictionary during path reconstruction.')
                    return None
                node = parent[node][0]
                path.append(node)
            path.reverse()
            return path

        # Set initial values for start and end
        if current_node is None:
            current_node = start
        if end is None:
            end = start

        if current_node == end:
            return reconstruct_path(current_node), 0

        if depth_limit == 0:
            return None

        visited.add(current_node)

        # Calculate the heuristic value for the current node
        h_value = self.getH(current_node)

        # Priority queue to prioritize nodes with lower f values (g + h)
        priority_queue = PriorityQueue()
        priority_queue.put((0 + h_value, 0, current_node))

        while not priority_queue.empty():
            f_value, g_value, node = priority_queue.get()

            if node == end:
                # Reconstruct the path and return
                return reconstruct_path(node), g_value

            visited.add(node)

            for neighbor, weight in self.getNeighbours(node):
                if neighbor not in visited:
                    # Calculate the heuristic value for the neighbor
                    h_value_neighbor = self.getH(neighbor)
                    # Calculate the new g value
                    new_g_value = g_value + weight
                    # Calculate the new f value
                    new_f_value = new_g_value + h_value_neighbor

                    # Check if the neighbor is not in the parent dictionary or has a lower g value
                    if neighbor not in parent or new_g_value < parent[neighbor][1]:
                        # Add the neighbor to the priority queue with the new f value
                        priority_queue.put((new_f_value, new_g_value, neighbor))
                        # Update the parent of the neighbor in the local dictionary with both node and g_value
                        parent[neighbor] = (node, new_g_value)

        return None

    #####################################################
    # Ver se faz sentido ter mais algum
    #####################################################
