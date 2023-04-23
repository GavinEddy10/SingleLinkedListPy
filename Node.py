class Node:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def to_string(self):
        if self.next_node is None:
            print("{v: " + str(self.value) + ", -> } ", end="")
        else:
            print("{v: " + str(self.value) + ", -> " + str(self.next_node.get_value()) + "} ", end="")


# parameter n: node v: value i: index
class LinkedList:
    def __init__(self, head_node=None):
        self.head_node = head_node
        self.size = 0
        if self.head_node is not None:
            self.size = 1

    def get_head_node(self):
        return self.head_node

    def insert_beginning_n(self, new_head):  # new head
        new_head.set_next_node(self.head_node)
        self.head_node = new_head
        self.size += 1

    def print_list(self):
        current = self.get_head_node()
        for i in range(self.size):
            current.to_string()
            current = current.get_next_node()
        print()

    def get_v(self, value):
        current = self.get_head_node()
        for i in range(self.size):
            if current.get_value() == value:
                return current
        return None

    def get_i(self, index):
        current = self.get_head_node()
        for i in range(self.size):
            if i == index:
                return current
            current = current.get_next_node()
        return None

    def add_node_index_n(self, index, new_node):
        if index > self.size or index < 0:  # out bounds
            print("TRACEBACK ERROR: @ method 'add_node_index_n: index out of bounds Exception")
        elif index == 0:  # at front
            self.insert_beginning_n(new_node)
        elif index == self.size - 1:  # at end
            self.add_node_n(new_node)
        elif index == self.size:
            end = self.last_node()
            end.set_next_node(new_node)
        elif index < self.size:  # anywehre in between
            curr_node = self.get_i(index - 1)
            next_node = self.get_i(index)
            curr_node.set_next_node(new_node)
            new_node.set_next_node(next_node)
            self.size += 1

    def add_collection_n(self, collection):
        end_node = self.last_node()
        end_node.set_next_node(collection.get(0))
        self.size += len(collection) - 1

    def clear(self):
        self.size = 0
        self.head_node = None

    def contains_n(self, node):
        head = self.get_head_node()
        for i in range(self.size):
            if head == node:
                return True
            head = head.get_next_node()

    def head_value(self):
        return self.head_node.get_value()

    def last_node(self):
        return self.get_i(self.size - 1)

    def add_node_n(self, new_node):
        end_node = self.get_i(self.size - 1)
        end_node.set_next_node(new_node)
        self.size += 1

    def to_list(self):# returns list of values
        track = []
        for i in range(self.size):
            track.append(self.get_i(i).get_value())
        return track

    def lastIndexOf_v(self, value): #returns index -1 if not in bounds
        index = -1
        items = self.to_list()
        for i in range(len(items)):
            n = items[i]
            if n == value:
                index = i
        return index

    def firstIndexOf_v(self, value):# returns first occurance
        index = -1
        node = self.get_v(value)
        if self.contains_n(node):
            for i in range(self.size):
                if self.get_i(i).get_value() == value:
                    index = i
                    return index
        return index

    def get_size(self):
        return self.size

    def remove_node_v(self, value):
        current_node = self.head_node
        next_node = current_node.get_next_node()

        if current_node.get_value() == value:
            self.head_node = current_node.get_next_node()
            self.size -= 1
            return

        for i in range(self.size - 1):
            if next_node.get_value() == value:
                current_node.set_next_node(next_node.get_next_node())
                self.size -= 1
                return
            current_node = next_node
            next_node = next_node.get_next_node()
