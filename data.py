class Nodes:
    def __init__(self, peiceodata):
        self.peiceofdata = peiceodata
        self.next = None
    def add(self, node):
        self.next = node
    def returnnextnode(self):
        return self.next
    def __str__(self):
        return str(self.peiceodata)
    