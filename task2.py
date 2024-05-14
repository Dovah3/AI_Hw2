import matplotlib.pyplot as plt
import networkx as nx

class KSARegionGraph():
    def __init__(self):
        """
        Initializes a KSARegionGraph object.
        """
        self.num_vertices = 13
        self.adjacency_matrix = [[0 for _ in range(13)] for _ in range(13)]
        self.region_names = [
            "Tabuk", "Jouf", "Northern", "Hail", "Madinah", "Qaseem",
            "Makkah", "Riyadh", "Baha", "Asir", "Najran", "Jazan", "Eastern"
        ]
        self.node_colors = ['grey', 'green', 'brown']
        self.num_colors = 3

    def is_safe(self, vertex, color_assignment, color):
        """
        Checks if assigning a color to a vertex is safe(does not conflict with neighboring vertices).

        Args:
            vertex (int): The index of the vertex (region).
            color_assignment (list): List representing the color assignment to vertices.
            color (int): The color to be assigned to the vertex.

        Returns:
            bool: True if the color assignment is safe, False otherwise.
        """
        for i in range(self.num_vertices):
            if self.adjacency_matrix[vertex][i] == 1 and color_assignment[i] == color:
                return False
        return True

    def graph_coloring_util(self, color_assignment, vertex):
        """
        function for recursively coloring the graph.
        Args:
            color_assignment (list): List representing the color assignment to vertices.
            vertex (int): The current vertex being processed.

        Returns:
            bool: True if a valid coloring is found, False otherwise.
        """
        if vertex == self.num_vertices:
            return True

        for color in range(1, self.num_colors + 1):
            if self.is_safe(vertex, color_assignment, color):
                color_assignment[vertex] = color
                if self.graph_coloring_util(color_assignment, vertex + 1):
                    return True
                color_assignment[vertex] = 0

    def graph_coloring(self):
        """
        Performs graph coloring using backtracking.

        Returns:
            bool: True if a valid coloring is found, False otherwise.
        """
        color_assignment = [0] * self.num_vertices
        if self.graph_coloring_util(color_assignment, 0) == None:
            print("Solution doesnt exist.")
            return False

        print("Solution exists and following are the assigned colors:")
        print(color_assignment)
        print('='*200)
        print('[', end='')
        for i, color in enumerate(color_assignment):
            if i != 12:
                print(f'{self.region_names[i]}: {self.node_colors[color-1]}', end=' ')
            else:
                print(f'{self.region_names[i]}: {self.node_colors[color-1]}]', end=' ')

        self.plot_graph(color_assignment)
        return True

    def plot_graph(self, color_assignment):
        """
        Plots the graph with colored vertices using NetworkX and Matplotlib.
        """
        G = nx.Graph()
        for i in range(self.num_vertices):
            G.add_node(i, label=self.region_names[i], color= get_color(i, color_assignment))

        for i in range(self.num_vertices):
            for j in range(i+1, self.num_vertices):
                if self.adjacency_matrix[i][j] == 1:
                    G.add_edge(i, j)

        pos = nx.spring_layout(G)

        node_labels = nx.get_node_attributes(G, 'label')
        node_colors = nx.get_node_attributes(G, 'color')

        nx.draw(G, pos, with_labels=False, node_color=[node_colors[i] for i in G.nodes()], node_size=3000, node_shape='o', linewidths=2, edgecolors='black')
        nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=10, font_color='black')

        plt.title("KSA Map Graph")
        plt.show()


def get_color(vertice_index, color_assignment):
    """
    Returns the color of the vertice

    Args:
        vertice_index (int): The index of the vertice.
        color_assignment (list): List representing the color assignment to vertices.

    Returns:
        str: The color associated with the region.
    """
    color = color_assignment[vertice_index]
    if color == 1:
        return 'grey'
    elif color == 2:
        return 'green'
    elif color == 3:
        return 'brown'

if __name__ == "__main__":
    ksa_graph = KSARegionGraph()

    # ["Tabuk", "Jouf", "Northern", "Hail", "Madinah", "Qaseem", "Makkah", "Riyadh", "Baha", "Asir", "Najran", "Jazan", "Eastern"]

    ksa_graph.adjacency_matrix = [
        [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], # Tabuk
        [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], # Jouf
        [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], # Northern
        [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], # Hail
        [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0], # Madinah
        [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1], # Qaseem
        [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0], # Makkah
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1], # Riyadh
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0], # Baha
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0], # Asir
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1], # Najran
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], # Jazan
        [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0]  # Eastern
    ]

    ksa_graph.graph_coloring()
