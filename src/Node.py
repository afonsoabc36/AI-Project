class Node:

    def __init__(self, name, id=-1):
        self.m_id = id
        self.m_name = str(name)
        # posteriormente podera ser colocado um objeto que armazena informação em cada nodo...

    def __str__(self):
        return "node" + self.m_name

    def __repr__(self):
        return "node" + self.m_name

    def setId(self, id):
        self.m_id = id

    def getId(self):
        return self.m_id

    def setName(self, name):
        self.m_name = name

    def getName(self):
        return self.m_name

    def __eq__(self, other):
        return self.m_name == other.m_name  # Ver se é preciso também testar o id...

    def __hash__(self):
        return hash(self.m_id)
