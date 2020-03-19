from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    # Add vertex for parent and child
    # Add edge for parent/child pair written as (parent, child) mentioned in ReadMe.
    # New path list
    # For each parents, find path to starting node
    # if path is longer than previous, new path will replace old path
    # Return ancestor unless starting node has no parents
    g = Graph()

    for (parent, child) in ancestors:
        g.add_vertex(parent)
        g.add_vertex(child)

    # Need to have to for loops for vertex and edge otherwise it throws an error.
    for (parent, child) in ancestors:
        g.add_edge(parent, child)

    new_path = []

    for (parent, child) in ancestors:
        path = g.dfs(parent, starting_node)
        if path is not None and len(path) > len(new_path):
            new_path = path.copy()
    if len(new_path) <= 1:
        return -1
    return new_path[0]
