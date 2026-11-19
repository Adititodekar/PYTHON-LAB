"""Draw two graphs next to each other in one Matplotlib window."""

import matplotlib.pyplot as plt
import networkx as nx


def display_graphs(graph1, graph2):
    """Display Graph 1 and Graph 2 side by side."""
    # Create one figure with two side-by-side drawing areas.
    figure, axes = plt.subplots(1, 2, figsize=(10, 5))

    # Create a readable spring layout separately for each graph.
    graph1_positions = nx.spring_layout(graph1, seed=1)
    graph2_positions = nx.spring_layout(graph2, seed=1)

    # Draw the graph structure and its vertex labels in each drawing area.
    nx.draw(
        graph1,
        graph1_positions,
        ax=axes[0],
        with_labels=True,
        node_color="lightblue",
        node_size=900,
        font_size=10,
    )
    nx.draw(
        graph2,
        graph2_positions,
        ax=axes[1],
        with_labels=True,
        node_color="lightgreen",
        node_size=900,
        font_size=10,
    )

    axes[0].set_title("Graph 1")
    axes[1].set_title("Graph 2")

    # Add space around the drawings, then show the completed window.
    figure.tight_layout()
    plt.show()
