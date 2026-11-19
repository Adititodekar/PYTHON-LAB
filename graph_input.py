"""Create an undirected graph from information entered in the terminal."""

import networkx as nx


def read_nonnegative_integer(prompt):
    """Ask for a whole number that is zero or greater."""
    while True:
        value = input(prompt).strip()

        try:
            number = int(value)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if number < 0:
            print("Please enter zero or a positive number.")
            continue

        return number


def get_graph_input(graph_name="Graph"):
    """Read vertices and edges, then return them as a NetworkX graph."""
    print(f"\nEnter details for {graph_name}")

    vertex_count = read_nonnegative_integer("Number of vertices: ")
    graph = nx.Graph()
    labels = []

    for index in range(vertex_count):
        while True:
            label = input(f"Label for vertex {index + 1}: ").strip()

            if not label:
                print("A vertex label cannot be empty.")
            elif "," in label:
                print("Vertex labels cannot contain a comma.")
            elif label in labels:
                print("Each vertex must have a unique label.")
            else:
                labels.append(label)
                break

    graph.add_nodes_from(labels)
    maximum_edges = vertex_count * (vertex_count - 1) // 2
    while True:
        edge_count = read_nonnegative_integer("Number of edges: ")
        if edge_count <= maximum_edges:
            break
        print(
            f"A simple undirected graph with {vertex_count} vertices can have "
            f"at most {maximum_edges} edges. Please enter the edge count again."
        )

    for index in range(edge_count):
        while True:
            edge_text = input(
                f"Edge {index + 1} (enter two labels separated by a comma): "
            ).strip()
            endpoints = edge_text.split(",")

            if len(endpoints) != 2:
                print("Enter exactly two vertex labels separated by a comma.")
                continue

            first_vertex = endpoints[0].strip()
            second_vertex = endpoints[1].strip()

            if first_vertex not in graph or second_vertex not in graph:
                print("Both labels must match vertices entered above.")
            elif first_vertex == second_vertex:
                print("A vertex cannot be connected to itself in this project.")
            elif graph.has_edge(first_vertex, second_vertex):
                print("That edge has already been entered.")
            else:
                graph.add_edge(first_vertex, second_vertex)
                break

    print(
        f"{graph_name} created with {graph.number_of_nodes()} vertices "
        f"and {graph.number_of_edges()} edges."
    )
    return graph
