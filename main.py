"""Terminal menu for the graph isomorphism project."""

from graph_input import get_graph_input
from graph_analysis import analyze_graph, compare_graphs
from isomorphism import check_isomorphism
from visualization import display_graphs


def graphs_are_ready(graph1, graph2):
    """Return True when the user has entered both graphs."""
    if graph1 is None or graph2 is None:
        print("Please enter both graphs first (menu options 1 and 2).")
        return False
    return True


def main():
    """Display the menu and run the option selected by the user."""
    graph1 = None
    graph2 = None

    while True:
        print("\nGraph Isomorphism Detection and Visualization")
        print("1. Enter Graph 1")
        print("2. Enter Graph 2")
        print("3. Display both graphs")
        print("4. Calculate vertex degrees and graph properties")
        print("5. Compare graph invariants")
        print("6. Check graph isomorphism")
        print("7. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            graph1 = get_graph_input("Graph 1")
        elif choice == "2":
            graph2 = get_graph_input("Graph 2")
        elif choice == "3":
            if graphs_are_ready(graph1, graph2):
                display_graphs(graph1, graph2)
        elif choice == "4":
            if graphs_are_ready(graph1, graph2):
                analyze_graph(graph1, "Graph 1")
                analyze_graph(graph2, "Graph 2")
        elif choice == "5":
            if graphs_are_ready(graph1, graph2):
                graph1_properties = analyze_graph(graph1, "Graph 1")
                graph2_properties = analyze_graph(graph2, "Graph 2")
                compare_graphs(graph1_properties, graph2_properties)
        elif choice == "6":
            if graphs_are_ready(graph1, graph2):
                check_isomorphism(graph1, graph2)
        elif choice == "7":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please choose a number from 1 to 7.")


if __name__ == "__main__":
    main()
