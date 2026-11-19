"""Calculate and compare basic properties of undirected graphs."""

import networkx as nx


def analyze_graph(graph, graph_name="Graph"):
    """Display and return the degrees and basic properties of one graph."""
    # Store each vertex degree in a dictionary, with the vertex as its key.
    vertex_degrees = dict(graph.degree())

    # Sort the degree values to form the graph's degree sequence.
    degree_sequence = sorted(vertex_degrees.values())

    vertex_count = graph.number_of_nodes()
    edge_count = graph.number_of_edges()

    # The empty graph has no connected components and is not connected.
    if vertex_count == 0:
        component_count = 0
        is_connected = False
    else:
        component_count = nx.number_connected_components(graph)
        is_connected = nx.is_connected(graph)

    print(f"\n{graph_name} analysis")
    print("Vertex degrees:")
    for vertex, degree in vertex_degrees.items():
        print(f"  {vertex}: {degree}")
    print(f"Sorted degree sequence: {degree_sequence}")
    print(f"Number of vertices: {vertex_count}")
    print(f"Number of edges: {edge_count}")
    print(f"Number of connected components: {component_count}")
    print(f"Connected: {'Yes' if is_connected else 'No'}")

    # Return the values so another part of the program can compare them.
    return {
        "vertex_degrees": vertex_degrees,
        "degree_sequence": degree_sequence,
        "vertex_count": vertex_count,
        "edge_count": edge_count,
        "component_count": component_count,
        "is_connected": is_connected,
    }


def compare_graphs(graph1_properties, graph2_properties):
    """Print whether selected properties match between two graphs."""
    property_names = [
        ("vertex_count", "Number of vertices"),
        ("edge_count", "Number of edges"),
        ("degree_sequence", "Sorted degree sequence"),
        ("component_count", "Number of connected components"),
        ("is_connected", "Connected status"),
    ]

    print("\nGraph property comparison")
    for key, description in property_names:
        first_value = graph1_properties[key]
        second_value = graph2_properties[key]

        if first_value == second_value:
            result = "Match"
        else:
            result = "Different"

        print(f"{description}: {result} (Graph 1: {first_value}; Graph 2: {second_value})")
