#https://gist.github.com/nlap/56061e47a2a8d69eb5f3

from graph_tool.all import *
import matplotlib
import numpy as np

print "aqui empeizo"

adj = np.loadtxt("/home/rodrigo/PycharmProjects/BigData/Process_Data/AdjacentMatrix_distance_1000.dat",delimiter=' ',dtype=np.dtype('int32'))

#creamos el grafo no directo
g = graph_tool.Graph(directed = False)

g.add_vertex(len(adj))
edge_weights = g.new_edge_property('double')
edge_icount_p = g.new_edge_property('int')
edge_icount_p.a = edge_icount_p.a.max()-edge_icount_p.a

for i in range(adj.shape[0]):
    for j in range(adj.shape[1]):
        if adj[i,j] != 0:
            e = g.add_edge(i, j)
            edge_weights[e] = 10


#graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=8, output_size=(2000, 2000), output="two-nodes.png")
c = graph_tool.closeness(g, weight=edge_icount_p)
graph_tool.graph_draw(g, pos=g.vertex_index, vertex_fill_color=c,vertex_size=graph_tool.prop_to_size(c, mi=5, ma=15),vcmap=matplotlib.cm.gist_heat,vorder=c, output="polblogs_closeness.pdf")