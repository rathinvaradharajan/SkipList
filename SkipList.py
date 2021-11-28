import random

from ElementNode import ElementNode


class SkipList:

    def __init__(self):
        self.head = ElementNode()

    @staticmethod
    def __get_height() -> int:
        height = 1
        roll = random.randint(0, 1)
        while roll != 0:
            height += roll
            roll = random.randint(0, 1)
        return height

    def search(self, value) -> bool:
        node = self.head
        while node is not None:
            while node.forward is not None and node.forward.value < value:
                node = node.forward

            if node.forward is not None and node.forward.value == value:
                return True
            node = node.down
        return False

    def add(self, value):
        node = self.head
        level_nodes = []
        while node is not None:
            while node.forward is not None and node.forward.value < value:
                node = node.forward
            if node.forward is not None and node.forward.value == value:
                return
            level_nodes.append(node)
            node = node.down

        height = self.__get_height()
        bottom = None
        while height > 0 and level_nodes:
            node = level_nodes.pop()
            bottom = ElementNode(value, node.forward, bottom)
            node.forward = bottom
            height -= 1

        start = self.head
        while height > 0:
            bottom = ElementNode(value, None, bottom)
            start = ElementNode(None, bottom, start)
            height -= 1
        self.head = start

    def remove(self, value):
        node = self.head
        while node.down is not None:
            while node.forward is not None and node.forward.value < value:
                node = node.forward
            if node.forward is not None and node.forward.value == value:
                break
            else:
                node = node.down

        while node is not None:
            while node.forward is not None and node.forward.value != value:
                node = node.forward
            node.forward = node.forward.forward
            node = node.down

    def print_levels(self) -> str:
        down = self.head
        forward = self.head
        result = ""
        while down is not None:
            result += "Level: "
            while forward is not None:
                result += "<Start>\t" if forward.value is None else str(forward.value) + "\t"
                forward = forward.forward
            result += "\n"
            down = down.down
            forward = down
        return result
