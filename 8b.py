#!/usr/bin/python3


class Node:

    def __init__(self):
        self.children = []
        self.metadata = []


def read_header():
    global index
    newnode = Node()
    children = license[index]
    index += 1
    countmeta = license[index]
    index += 1
    for child in range(children):
        newnode.children.append(read_header())
    for j in range(countmeta):
        newnode.metadata.append(license[index])
        index += 1
    return newnode


def get_value(n):
    total = 0
    if not n.children:
        for m in n.metadata:
            total += m
    else:
        for m in n.metadata:
            print(m-1, len(n.children))
            if m-1 < len(n.children):
                total += get_value(n.children[m-1])
    return total


with open('8.dat') as f:
    data = f.read()
license = data.split('\n')
license.pop()
license = [int(n) for n in license[0].split(' ')]
nodes = []
index = 0
nodes.append(read_header())
total = get_value(nodes[0])
print('Sum of metadata: ', total)
