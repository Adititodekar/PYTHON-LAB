"""Check whether two graphs are isomorphic and show a vertex mapping."""

import networkx as nx
from networkx.algorithms import isomorphism


def check_isomorphism(graph1, graph2):
    """Print and return the isomorphism result and its vertex mapping."""
    # NetworkX checks whether a structure-preserving vertex mapping exists.
    are_isomorphic = nx.is_isomorphic(graph1, graph2)

    if are_isomorphic:
        print("ISOMORPHIC")

        # GraphMatcher finds one mapping from graph1's vertices to graph2's.
        matcher = isomorphism.GraphMatcher(graph1, graph2)
        vertex_mapping = next(matcher.isomorphisms_iter())

        print("Vertex mapping (Graph 1 -> Graph 2):")
        for first_vertex, second_vertex in vertex_mapping.items():
            print(f"  {first_vertex} -> {second_vertex}")

        return True, vertex_mapping

    print("NOT ISOMORPHIC")
    print("No adjacency-preserving mapping exists between these graphs.")
    return False, {}
