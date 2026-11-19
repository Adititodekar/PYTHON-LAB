# Graph Isomorphism Detection and Visualization

A terminal-based mini-project for entering two undirected graphs, comparing their basic properties, checking whether they are isomorphic, and displaying them side by side. It is intended for second-year IT students studying graph theory.

## Project files

- `main.py` displays the terminal menu and connects the modules.
- `graph_input.py` accepts vertex labels and edge connections and creates a graph.
- `graph_analysis.py` displays vertex degrees, the sorted degree sequence, vertex and edge counts, connected components, and connectedness. It also compares these properties.
- `isomorphism.py` uses NetworkX to check isomorphism and display a vertex mapping when one exists.
- `visualization.py` draws both graphs in one Matplotlib window.
- `requirements.txt` lists NetworkX and Matplotlib.

## Requirements

- Python 3
- NetworkX
- Matplotlib

Install the required libraries from this folder with:

```text
python -m pip install -r requirements.txt
```

## Run the project

From this folder, run:

```text
python main.py
```

Use the menu to enter Graph 1 and Graph 2 before choosing an analysis, comparison, visualization, or isomorphism option. Enter each edge as two existing vertex labels separated by a comma, for example `A,B`. Choose the exit option to close the program.

## Limitations

- The program handles simple undirected graphs. It does not allow self-loops or repeated edges.
- Graph invariants such as vertex count, edge count, degree sequence, and connected components can show that graphs are not isomorphic when they differ. Matching these properties alone does not prove isomorphism; NetworkX performs the final check.
- Matplotlib needs a working graphical display backend to open the visualization window. On systems where the Python Tk installation is unavailable, the graph panels can render with a non-window backend, but an interactive window will not open until that Python environment is repaired.

## Menu and graph input

The terminal menu lets you enter Graph 1 and Graph 2, display them, analyze their properties, compare invariants, check isomorphism, or exit. Enter both graphs before choosing an analysis, comparison, visualization, or isomorphism option.

Enter each edge as two existing vertex labels separated by a comma, such as `A,B`. Vertex labels must be unique and cannot contain commas. The program rejects self-loops and duplicate edges.
