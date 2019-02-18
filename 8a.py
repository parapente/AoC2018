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


def sum_metadata(n):
    total = 0
    for node in n:
        for m in node.metadata:
            total += m
        total += sum_metadata(node.children)
    return total


with open('8.dat') as f:
    data = f.read()
license = data.split('\n')
license.pop()
license = [int(n) for n in license[0].split(' ')]
nodes = []
index = 0
nodes.append(read_header())
total = sum_metadata(nodes)
print('Sum of metadata: ', total)
