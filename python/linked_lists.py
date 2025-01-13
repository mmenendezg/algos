class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        if self.data:
            return str(self.data)
        else:
            return "Null"

    def __bool__(self):
        if self.data:
            return True
        else:
            return False

    def append(self, next_node):
        self.next = next_node
        self.next.prev = self

    def prepend(self, prev_node):
        self.prev = prev_node
        self.prev.next = self


class LinkedList:
    def __init__(self, list_values=None):
        self.size = 0
        self.head = None
        self.tail = None

        if list_values:
            self.insert_values(list_values)

    def insert_at_head(self, data):
        if self.head is None:
            self.head = Node(data, self.tail)

        node = Node(data, self.head)
        self.head = node
        self.size += 1

    def insert_at_tail(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_tail(data)

    def insert_after_value(self, key_value, value):
        if self.head is None:
            raise IndexError("List is empty")
        node = self.head

    def insert(self, index, data):
        assert index >= 0, "Not a valid index"
        assert index <= len(self), "Not a valid index"

        if index == 0:
            self.insert_at_head(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove(self, index):
        assert index >= 0, "Not a valid index"
        assert index < len(self), "Not a valid index"

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                return
            itr = itr.next
            count += 1

    def __str__(self):
        if self.head is None:
            print("[ Null ]")
            return
        current = self.head
        llstr = "[ "
        while current:
            llstr += str(current.data)
            if current.next:
                llstr += "  "
            current = current.next
        llstr += " ]"
        return llstr

    def __len__(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
