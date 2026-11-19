"""Streamlit interface for the graph isomorphism mini-project."""

import matplotlib.pyplot as plt
import networkx as nx
import streamlit as st
from networkx.algorithms import isomorphism


def create_graph(vertex_text, edge_text, graph_name):
    """Create a graph from comma-separated labels and one edge per line."""
    graph = nx.Graph()

    # Read vertex labels, while allowing an empty graph when no labels are given.
    if vertex_text.strip():
        labels = [label.strip() for label in vertex_text.split(",")]
        if any(not label for label in labels):
            return None, f"{graph_name}: vertex labels cannot be empty."
        if len(labels) != len(set(labels)):
            return None, f"{graph_name}: vertex labels must be unique."
    else:
        labels = []

    graph.add_nodes_from(labels)

    # Each non-empty line should contain exactly two comma-separated labels.
    edge_lines = [line.strip() for line in edge_text.splitlines() if line.strip()]
    for line_number, edge_line in enumerate(edge_lines, start=1):
        endpoints = [endpoint.strip() for endpoint in edge_line.split(",")]

        if len(endpoints) != 2 or not endpoints[0] or not endpoints[1]:
            return None, (
                f"{graph_name}: edge line {line_number} must contain two labels "
                "separated by a comma, for example A,B."
            )

        first_vertex, second_vertex = endpoints
        if first_vertex not in graph or second_vertex not in graph:
            return None, f"{graph_name}: edge line {line_number} uses an unknown vertex label."
        if first_vertex == second_vertex:
            return None, f"{graph_name}: self-loops are not allowed."
        if graph.has_edge(first_vertex, second_vertex):
            return None, f"{graph_name}: duplicate edges are not allowed."

        graph.add_edge(first_vertex, second_vertex)

    return graph, None


def analyze_graph(graph):
    """Return vertex degrees and the basic graph properties."""
    degrees = dict(graph.degree())
    vertex_count = graph.number_of_nodes()

    # NetworkX defines connectedness for non-empty undirected graphs.
    if vertex_count == 0:
        component_count = 0
        connected = False
    else:
        component_count = nx.number_connected_components(graph)
        connected = nx.is_connected(graph)

    return {
        "degrees": degrees,
        "degree_sequence": sorted(degrees.values()),
        "vertex_count": vertex_count,
        "edge_count": graph.number_of_edges(),
        "component_count": component_count,
        "connected": connected,
    }


def show_graph_analysis(graph_name, properties):
    """Display degrees, degree sequence, and graph properties."""
    st.subheader(f"{graph_name} analysis")
    st.write("**Degree of each vertex**")
    st.write(properties["degrees"])
    st.write("**Sorted degree sequence**")
    st.write(properties["degree_sequence"])

    first_row = st.columns(3)
    first_row[0].metric("Vertices", properties["vertex_count"])
    first_row[1].metric("Edges", properties["edge_count"])
    first_row[2].metric("Connected components", properties["component_count"])
    st.write(f"**Connected:** {'Yes' if properties['connected'] else 'No'}")


def show_graphs(graph1, graph2):
    """Draw both graphs in one side-by-side Matplotlib figure."""
    figure, axes = plt.subplots(1, 2, figsize=(10, 4))

    positions1 = nx.spring_layout(graph1, seed=1)
    positions2 = nx.spring_layout(graph2, seed=1)

    nx.draw(
        graph1,
        positions1,
        ax=axes[0],
        with_labels=True,
        node_color="lightblue",
        node_size=800,
        font_size=10,
    )
    nx.draw(
        graph2,
        positions2,
        ax=axes[1],
        with_labels=True,
        node_color="lightgreen",
        node_size=800,
        font_size=10,
    )

    axes[0].set_title("Graph 1")
    axes[1].set_title("Graph 2")
    figure.tight_layout()
    st.pyplot(figure)
    plt.close(figure)


st.set_page_config(page_title="Graph Isomorphism", layout="wide")
st.title("Graph Isomorphism Detection and Visualization")
st.write(
    "Enter two undirected graphs to compare their properties, visualize them, "
    "and check whether they are isomorphic."
)

with st.form("graph_input_form"):
    graph1_column, graph2_column = st.columns(2)

    with graph1_column:
        st.subheader("Graph 1")
        vertex_text1 = st.text_input(
            "Vertex labels (comma-separated)", placeholder="A, B, C"
        )
        edge_text1 = st.text_area(
            "Edges (one per line, such as A,B)", placeholder="A,B\nB,C"
        )

    with graph2_column:
        st.subheader("Graph 2")
        vertex_text2 = st.text_input(
            "Vertex labels (comma-separated)", placeholder="1, 2, 3"
        )
        edge_text2 = st.text_area(
            "Edges (one per line, such as 1,2)", placeholder="1,2\n2,3"
        )

    submitted = st.form_submit_button("Analyze both graphs")

if submitted:
    graph1, error1 = create_graph(vertex_text1, edge_text1, "Graph 1")
    graph2, error2 = create_graph(vertex_text2, edge_text2, "Graph 2")

    if error1:
        st.error(error1)
    if error2:
        st.error(error2)

    if not error1 and not error2:
        st.header("Graph visualizations")
        show_graphs(graph1, graph2)

        properties1 = analyze_graph(graph1)
        properties2 = analyze_graph(graph2)

        analysis_column1, analysis_column2 = st.columns(2)
        with analysis_column1:
            show_graph_analysis("Graph 1", properties1)
        with analysis_column2:
            show_graph_analysis("Graph 2", properties2)

        st.header("Graph invariant comparison")
        invariant_rows = []
        invariant_names = [
            ("vertex_count", "Number of vertices"),
            ("edge_count", "Number of edges"),
            ("degree_sequence", "Sorted degree sequence"),
            ("component_count", "Connected components"),
            ("connected", "Connected status"),
        ]

        for key, name in invariant_names:
            first_value = properties1[key]
            second_value = properties2[key]
            invariant_rows.append(
                {
                    "Property": name,
                    "Graph 1": first_value,
                    "Graph 2": second_value,
                    "Result": "Match" if first_value == second_value else "Different",
                }
            )
        st.table(invariant_rows)
        st.caption(
            "Matching invariants are necessary for isomorphism, but they do not "
            "prove that two graphs are isomorphic."
        )

        st.header("Isomorphism result")
        # This NetworkX check provides the final isomorphism decision.
        are_isomorphic = nx.is_isomorphic(graph1, graph2)

        if are_isomorphic:
            st.success("ISOMORPHIC: the graphs have the same structure.")

            # GraphMatcher supplies one mapping from Graph 1 to Graph 2.
            matcher = isomorphism.GraphMatcher(graph1, graph2)
            vertex_mapping = next(matcher.isomorphisms_iter())
            st.write("**Vertex mapping (Graph 1 -> Graph 2)**")
            st.write(vertex_mapping)
        else:
            st.error(
                "NOT ISOMORPHIC: no adjacency-preserving vertex mapping exists."
            )
