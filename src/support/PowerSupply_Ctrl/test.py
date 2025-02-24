import tkinter as tk
import random


class DynamicGraph:
    def __init__(self, canvas, width, height, padding, max_points):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.padding = padding
        self.max_points = max_points
        self.values = []
        self.x_step = (self.width - 2 * self.padding) / (self.max_points - 1)

    def add_value(self, value):
        """Fügt einen neuen Wert hinzu und aktualisiert den Graphen."""
        self.values.append(value)
        if len(self.values) > self.max_points:
            self.values.pop(0)
        self.update_graph()

    def update_graph(self):
        """Zeichnet den Graphen basierend auf den aktuellen Werten."""
        self.canvas.delete("all")  # Löscht den vorherigen Graphen

        if len(self.values) < 2:
            return  # Zu wenige Werte, um einen Graphen zu zeichnen

        # Berechne Skalierung
        max_value = max(self.values)
        min_value = min(self.values)
        if max_value == min_value:  # Verhindere Division durch 0
            max_value += 1

        y_scale = (self.height - 2 * self.padding) / (max_value - min_value)

        # Transformiere Werte in Canvas-Koordinaten
        points = [
            (self.padding + i * self.x_step,
             self.height - self.padding - (value - min_value) * y_scale)
            for i, value in enumerate(self.values)
        ]

        # Zeichne Linien zwischen den Punkten
        for i in range(len(points) - 1):
            self.canvas.create_line(points[i], points[i + 1], fill="blue",
                                    width=2)

        # Zeichne Punkte
        for x, y in points:
            self.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="red")


def generate_random_value(min_value, max_value):
    """Generiert einen zufälligen Wert mit unterschiedlichen
    Wahrscheinlichkeiten pro Bereich.
    """
    # Wahrscheinlichkeit für jedes Segment definieren
    low_prob = 0.6   # 60% Wahrscheinlichkeit für niedrige Werte
    mid_prob = 0.3   # 30% Wahrscheinlichkeit für mittlere Werte
    high_prob = 0.1  # 10% Wahrscheinlichkeit für hohe Werte

    # Zufällige Auswahl des Segments basierend auf den Wahrscheinlichkeiten
    segment = random.choices(
        population=["low", "mid", "high"],
        weights=[low_prob, mid_prob, high_prob],
        k=1
    )[0]

    # Wertebereich des Segments anpassen
    if segment == "low":
        max_low = min(1000, max_value)  # Begrenze "low" auf maximal 1000
        random_float = random.random()
        value = int(min_value + (max_low - min_value) * (random_float ** 2))
    elif segment == "mid":
        min_mid = min(1000, max_value)  # Starte "mid" ab 1000
        max_mid = min(2000, max_value)  # Begrenze "mid" auf 5000
        random_float = random.random()
        value = int(min_mid + (max_mid - min_mid) * random_float)
    else:  # "high"
        min_high = max(1000, 2000)  # Starte "high" ab 5000
        random_float = random.random()
        value = int(min_high + (max_value - min_high) * (random_float ** 0.5))

    # Grenze sicherstellen
    value = max(min_value, min(max_value, value))
    print(f"Segment: {segment}, Wert: {value}")
    return value


def update_graph_periodically(graph, min_value, max_value, interval):
    """Fügt dem Graphen periodisch neue Werte hinzu."""
    new_value = generate_random_value(min_value, max_value)
    graph.add_value(new_value)
    graph.canvas.after(interval, update_graph_periodically, graph, min_value,
                       max_value, interval)


def main():
    # Konfiguration
    max_points = 50  # Maximale Anzahl der Punkte im Graphen
    min_value = 0    # Minimaler Wert
    max_value = 10000  # Maximaler Wert
    interval = 50   # Aktualisierungsintervall in Millisekunden
    canvas_width = 600
    canvas_height = 400
    padding = 50

    # Tkinter-Fenster erstellen
    root = tk.Tk()
    root.title("Fortlaufender Graph mit zufälligen Werten")
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height,
                       bg="white")
    canvas.pack()

    # Graphen-Objekt erstellen
    graph = DynamicGraph(canvas, canvas_width, canvas_height, padding,
                         max_points)

    # Graph regelmäßig aktualisieren
    update_graph_periodically(graph, min_value, max_value, interval)

    root.mainloop()


if __name__ == "__main__":
    main()
