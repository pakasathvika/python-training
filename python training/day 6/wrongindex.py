class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def pop(self):
        if not self.tail:
            return None
        data = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return data

    def peek(self):
        if self.tail:
            return self.tail.data
        return None

    def is_empty(self):
        return self.head is None

def find_first_unmatched_closing(s):
    st = DoubleLinkedList()
    for i, char in enumerate(s):
        if char in '({[':
            st.append((char, i))
        else:
            if st.is_empty():
                return i + 1
            top, pos = st.peek()
            if (char == ']' and top == '[') or (char == '}' and top == '{') or (char == ')' and top == '('):
                st.pop()
            else:
                return i + 1
    return -1 if st.is_empty() else s.index(st.head.data[0]) + 1

# Test the function with the provided inputs
s1 = "(([{}]))"
s2 = "[{()]]"

print(find_first_unmatched_closing(s1))  
print(find_first_unmatched_closing(s2)) 
