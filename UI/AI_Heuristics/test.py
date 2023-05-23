import py4cytoscape as cy
import networkx as nx

# Create a hierarchical graph
G = nx.DiGraph()
G.add_edge("A", "B")
G.add_edge("A", "C")
G.add_edge("B", "D")
G.add_edge("B", "E")
G.add_edge("C", "F")

# Convert the graph to a dictionary
network_data = {
    "nodes": [
        {"data": {"id": node}}
        for node in G.nodes()
    ],
    "edges": [
        {"data": {"source": edge[0], "target": edge[1]}}
        for edge in G.edges()
    ]
}

# Connect to Cytoscape
cytoscape = cy.CytoscapeConnection()

# Add the network to Cytoscape
cytoscape.add_network_from_dict(network_data)

# Apply the radial layout in Cytoscape
cytoscape.layout.apply(name='radial')

# Display the graph in Cytoscape
cytoscape.window.fit_content()

# Close the connection
cytoscape.close()
