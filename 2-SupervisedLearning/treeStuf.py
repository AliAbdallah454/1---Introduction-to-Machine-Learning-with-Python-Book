import graphviz

with open("tree.dot") as f:
 dot_graph = f.read()
graphviz.Source(dot_graph)
