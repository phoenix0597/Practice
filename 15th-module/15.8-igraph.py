import igraph as ig

# Создание пустого графа
graph = ig.Graph()

# Добавление вершин
graph.add_vertices(4)

# Добавление рёбер
graph.add_edges([(0, 1), (1, 2), (2, 3), (3, 0)])

# Получение списка вершин и рёбер
nodes = graph.vs
edges = graph.es

# Визуализация графа
layout = graph.layout("circle")
# ig.plot(graph, layout=layout, vertex_color='lightblue', edge_color='gray')
ig.plot(graph, "my_graph.pdf", layout=layout, vertex_color='lightblue', edge_color='gray')

