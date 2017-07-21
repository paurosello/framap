def get_styles():
    return {
                "graph": {
                    "label": "Module",
                    "fontsize": "16",
                    "fontcolor": "white",
                    "bgcolor": "#333333",
                    "rankdir": "BT",
                    "size": "2,2"
                },
                "nodes": {
                    "fontname": "Helvetica",
                    "shape": "hexagon",
                    "fontcolor": "white",
                    "color": "white",
                    "style": "filled",
                    "fillcolor": "#006699"
                },
                "edges": {
                    "style": "dashed",
                    "color": "white",
                    "arrowhead": "open",
                    "fontname": "Courier",
                    "fontsize": "12",
                    "fontcolor": "white"
                }
            }

def apply_styles(graph, styles):
    graph.graph_attr.update(
        ('graph' in styles and styles['graph']) or {}
    )
    graph.node_attr.update(
        ('nodes' in styles and styles['nodes']) or {}
    )
    graph.edge_attr.update(
        ('edges' in styles and styles['edges']) or {}
    )
    return graph
