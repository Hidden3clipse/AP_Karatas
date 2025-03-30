import matplotlib.pyplot as plt  # Import der Matplotlib-Bibliothek für Diagramme
import pandas as pd  # Import der Pandas-Bibliothek zur Datenverarbeitung

# CSV-Datei einlesen und in einen DataFrame speichern
df = pd.read_csv("csv_dateien/iris (1).csv")

# Erstellen eines Scatterplots mit Matplotlib
plt.scatter(df["sepal_length"], df["sepal_width"], c="blue", alpha=0.5)
# -> "sepal_length" wird auf der x-Achse dargestellt, "sepal_width" auf der y-Achse
# -> c="blue" färbt die Punkte blau
# -> alpha=0.5 macht die Punkte halbtransparent

plt.xlabel("Sepal Length")  # Achsenbeschriftung für die x-Achse
plt.ylabel("Sepal Width")   # Achsenbeschriftung für die y-Achse
plt.title("Scatterplot: Sepal Length vs. Sepal Width")  # Diagrammtitel
plt.show()  # Diagramm anzeigen


# --- Alternative Visualisierung mit Seaborn ---

import seaborn as sns  # Import der Seaborn-Bibliothek für schöne Diagramme
import matplotlib.pyplot as plt  # Matplotlib erneut importieren (optional)

# Scatterplot mit Seaborn erstellen, mit zusätzlicher Farbcodierung nach "species"
sns.scatterplot(data=df, x="sepal_length", y="sepal_width", hue="species")

plt.xlabel("Sepal Length")  # Achsenbeschriftung für die x-Achse
plt.ylabel("Sepal Width")   # Achsenbeschriftung für die y-Achse
plt.title("Scatterplot: Sepal Length vs. Sepal Width nach Species")  # Diagrammtitel
plt.show()  # Diagramm anzeigen

# --> Vorteile von Seaborn:
# 1. Farbige Punkte je nach "species", wodurch Unterschiede zwischen Arten sichtbar werden.
# 2. Automatische Legende, die zeigt, welche Farbe zu welcher Spezies gehört.

# Ein Plot ist eine grafische Darstellung von Daten. In Python werden Plots häufig mit Bibliotheken wie Matplotlib
# und Seaborn erstellt, um Zusammenhänge zwischen Datenpunkten zu visualisieren. Ein Scatterplot (Streudiagramm) ist
# eine Art von Plot, bei dem einzelne Punkte auf einer x-y-Achse dargestellt werden, um Muster oder Korrelationen zwischen
# zwei Variablen zu erkennen.
