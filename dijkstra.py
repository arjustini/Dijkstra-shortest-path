#!/usr/bin/env python3

import json
import sys


def main(graph, source, dest):

    with open(graph) as json_file:
        data = json.load(json_file)

    nodelist = []
    distances = {}
    visited = {}
    

    for nodes in data:
        if nodes['src'] not in nodelist:
            nodelist.append(nodes['src'])

    unvisited = {}
    for node in nodelist:
        unvisited[node] = None

    
    current = source
    currentDist = 0
    unvisited[current] = currentDist


    for nodes in nodelist:
        distances[nodes] = []
        for node in data:
            if node['src'] == nodes:
                distances[nodes].append((node['w'], node['dst']))
    
    nodesprevious = {}
    while True:
        for dist,adjacent in distances[current]:
            if adjacent in unvisited:
                newDist= currentDist + int(dist)
                if unvisited[adjacent] is None or unvisited[adjacent] > newDist:
                    nodesprevious[adjacent] = (current, newDist)
                    unvisited[adjacent] = newDist 
        visited[current] = currentDist
        del unvisited[current]
        if len(unvisited) == 0:
            break
        neighbors = []
        for node in unvisited.items():
            if node[1] != None:
                neighbors.append(node)
        current = min(neighbors, key = lambda t : t[1])[0]
        currentDist = min(neighbors, key = lambda t : t[1])[1]
    
    path = []
    node = dest
    while node != source:
        path.append(node)
        node = nodesprevious[node][0]
    path.append(source)
    path.reverse()
    print(path)

 #   print(visited)

    
    
if __name__ == '__main__':

    if len(sys.argv) != 4:
        print('Usage:%s  <file> <source> <destination>')
        sys.exit(-1)

      
    graphfile = sys.argv[1]
    sourcenode = sys.argv[2]
    destnode = sys.argv[3]
    main(graphfile, sourcenode, destnode)