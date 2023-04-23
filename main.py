from Node import *

my_node = Node(1)
my_node2 = Node(198)
my_node3 = Node(200)
my_node4 = Node(300)
my_node5 = Node(8102)

list = LinkedList()
list.insert_beginning_n(my_node)
list.insert_beginning_n(my_node2)
list.insert_beginning_n(my_node4)
list.insert_beginning_n(my_node3)
list.print_list()
print()
print(list.lastIndexOf_v(1))
print()
list.print_list()



