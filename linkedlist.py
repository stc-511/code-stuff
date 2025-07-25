from data import Nodes

class Linkedlist:
    def __init__(self):
        size = 0
        head = None
    def get(self, posistion):
        nodeon = self.head
        for i in range(posistion):
            nodeon = nodeon.next
        return nodeon.peiceodata
    def add(self, value, posistion):
        self.size += 1
        node = Nodes(value)
        if posistion == 0:
            node.add(self.head)
            self.head = node
        else:
            nodeon = self.head
            for i in range(posistion - 1):
                nodeon = nodeon.next
            nodeonon = nodeon.next
            node.add(nodeon)
