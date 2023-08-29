#!/usr/bin/python3
""" THis is file tha contains the singly linked list class node """


class Node:
    """ This is a class that contains the singly linked lists """

    def __init__(self, data, next_node=None):
        """ This is a method that initialize self """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ This is a method that return the node data """
        return self.__data

    @data.setter
    def data(self, value):
        """ This is a method that set the data to value """

        if type(value) is not int:
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """ This is a method that next node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ this is a method thate set the next node to the value """

        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ This is a class SinglyLinkedList with the associated node """

    def __init__(self):
        """ This is a method that initializated self """
        self.__head = []

    def __str__(self):
        """ This is a method that return the printed self """

        i = 0
        ch = ""
        for n in self.__head:
            ch += str(n.data)
            if i != len(self.__head) - 1:
                ch += "\n"
            i += 1

        return ch

    def sorted_insert(self, value):
        """ This is a method that insert a new node to the sotred position """

        new_node = Node(value)
        if len(self.__head) == 0:
            self.__head.append(new_node)
        else:
            chk = False
            i = 0
            for n in self.__head:
                if n.data >= value:
                    self.__head[i - 1].next_node = new_node
                    new_node.next_node = n
                    self.__head = self.__head[:i] + [new_node] + self.__head[i:]
                    chk = True
                    break
                i += 1

            if not chk:
                self.__head[-1].next_node = new_node
                self.__head.append(new_node)
