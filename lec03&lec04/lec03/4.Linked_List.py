class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def append(self, data):
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def insert(self, data, position):
        if position < 0:
            print("插入位置无效")
            return
        
        new_node = Node(data)
        
        if position == 0 or self.is_empty():
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev = None
            count = 0
            
            while current and count < position:
                count += 1
                prev = current
                current = current.next
            
            if not current and count < position:
                print("插入位置超出链表长度")
                return
            
            prev.next = new_node
            new_node.next = current
    
    def delete(self, key):
        if self.is_empty():
            print("链表为空")
            return
        
        if self.head.data == key:
            self.head = self.head.next
            return
        
        current = self.head
        prev = None
        
        while current and current.data != key:
            prev = current
            current = current.next
        
        if not current:
            print("未找到指定元素")
            return
        
        prev.next = current.next
    
    def search(self, key):
        if self.is_empty():
            print("链表为空")
            return
        
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        
        return False
    
    def display(self):
        if self.is_empty():
            print("链表为空")
            return
        
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# 测试链表操作
linked_list = LinkedList()

# 增加元素
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

# 显示链表
linked_list.display()  # 输出: 1 2 3

# 插入元素
linked_list.insert(4, 1)
linked_list.insert(5, 0)

# 显示链表
linked_list.display()  # 输出: 5 1 4 2 3

# 删除元素
linked_list.delete(1)

# 显示链表
linked_list.display()  # 输出: 5 4 2 3

# 查找元素
print(linked_list.search(2))  # 输出: True
print(linked_list.search(6))  # 输出: False
