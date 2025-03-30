import pandas as pd  # Importiert die Pandas-Bibliothek zur Datenverarbeitung
import seaborn as sns  # Importiert Seaborn für Visualisierungen
from matplotlib import pyplot as plt  # Importiert Matplotlib für Diagramme
from sklearn.cluster import KMeans  # Importiert KMeans für Clustering
from yellowbrick.cluster import KElbowVisualizer  # Importiert KElbowVisualizer zur Bestimmung der optimalen Cluster-Anzahl

# 1. Daten einlesen
df = pd.read_csv("csv_dateien/winequality-red.csv", delimiter=';')  # CSV-Datei einlesen und Semikolon als Trennzeichen nutzen

# 2. Datensatz erkunden
print("\nErste 5 Zeilen des DataFrames:")
print(df.head())  # Zeigt die ersten 5 Zeilen

print("\nLetzte 5 Zeilen des DataFrames:")
print(df.tail())  # Zeigt die letzten 5 Zeilen

# 3. Zusammenfassung des DataFrames
print("\nAllgemeine Informationen zum DataFrame:")
print(df.info())  # Zeigt Infos über Datentypen und fehlende Werte

print("\nStatistische Übersicht des DataFrames:")
print(df.describe())  # Zeigt statistische Kennzahlen wie Mittelwert, Standardabweichung etc.

# 4. Spalten auswählen
selected_columns = df[['alcohol', 'pH']]  # Wählt die Spalten 'alcohol' und 'pH' aus
print("\nErste 10 Zeilen der ausgewählten Spalten (Alkohol & pH):")
print(selected_columns.head(10))  # Zeigt die ersten 10 Zeilen dieser Spalten

# 5. Bedingte Auswahl (quality genau 8)
filtered_df_8 = df[df['quality'] == 8]  # Filtert Zeilen mit Qualitätswert 8
print("\nZeilen mit Qualität genau 8:")
print(filtered_df_8)

# 6. Mehrere Bedingungen (Alkoholgehalt > 12.5 und Qualität >= 7)
filtered_df = df[(df['alcohol'] > 12.5) & (df['quality'] >= 7)]  # Wählt Weine mit hohem Alkoholgehalt und guter Qualität
print("\nZeilen mit Alkoholgehalt > 12.5 und Qualität >= 7:")
print(filtered_df)

# 7. Neue Spalte hinzufügen (Dichte / Alkoholgehalt)
df['density_alcohol_ratio'] = df['density'] / df['alcohol']  # Erstellt eine neue Spalte als Verhältnis von Dichte zu Alkohol
print("\nErste Zeilen mit neuer Spalte (Dichte/Alkoholgehalt):")
print(df.head())

# 8. Werte in der quality-Spalte ändern
def quality_label(q):  # Funktion zur Umwandlung numerischer Qualität in Textlabels
    if q == 3:
        return "sehr schlecht"
    elif q == 4:
        return "schlecht"
    elif q == 5:
        return "okay"
    elif q == 6:
        return "gut"
    else:
        return "sehr gut"
df['quality_label'] = df['quality'].apply(quality_label)  # Wendet die Funktion auf die 'quality'-Spalte an
print("\nZuordnung der Qualitätswerte:")
print(df[['quality', 'quality_label']].head())

# 9. Entfernen der Zeilen mit pH-Wert kleiner als 3.0
df = df[df['pH'] >= 3.0]  # Entfernt alle Zeilen mit pH-Werten unter 3.0
print("\nErste Zeilen nach Entfernen von pH-Werten < 3.0:")
print(df.head())

# 10. Spaltenüberschriften ausgeben
print("\nSpaltenüberschriften des DataFrames:")
print(df.columns)

# 11. Spaltenüberschriften mit deutschen Bezeichnungen ersetzen
deutsch_columns = {  # Dictionary zur Umbenennung der Spalten
    'fixed acidity': 'fester Säuregehalt',
    'volatile acidity': 'flüchtiger Säuregehalt',
    'citric acid': 'Zitronensäure',
    'residual sugar': 'Restzucker',
    'chlorides': 'Chloride',
    'free sulfur dioxide': 'freies Schwefeldioxid',
    'total sulfur dioxide': 'Gesamtschwefeldioxid',
    'density': 'Dichte',
    'pH': 'pH-Wert',
    'sulphates': 'Sulfate',
    'alcohol': 'Alkohol',
    'quality': 'Qualität'
}
df.rename(columns=deutsch_columns, inplace=True)  # Wendet die Umbenennung an
print("\nErste Zeilen nach Umbenennung der Spalten:")
print(df.head())

# 12. Visualisierung (Scatterplot von Alkohol vs. Qualität)
print("\nErstelle Scatterplot für Alkohol vs. Qualität...")
sns.scatterplot(x=df['Alkohol'], y=df['Qualität'])  # Erstellt einen Streudiagramm für Alkohol und Qualität
plt.xlabel("Alkoholgehalt")
plt.ylabel("Qualität")
plt.title("Alkohol vs. Qualität")
plt.show()

# 13. KMeans Qualität
print("\n#13 KMeans Qualität")

# Daten ohne Zielspalte erzeugen
data_unknown = df.drop(['Qualität', 'quality_label'], axis=1)  # Entfernt Zielvariablen für unüberwachtes Clustering
print(data_unknown.dtypes)  # Zeigt Datentypen der verbleibenden Spalten

model = KMeans()  # Erstellt ein KMeans-Clustering-Modell

# Ermittle optimale Anzahl von Klassen
visualizer = KElbowVisualizer(model, k=(2, 9))  # Bestimmt optimale Clusteranzahl zwischen 2 und 9
visualizer.fit(data_unknown)
visualizer.show()

# n_clusters wird nach der graphischen Analyse initialisiert
kmeans = KMeans(n_clusters=4)  # Erstellt ein KMeans-Modell mit 4 Clustern

# Vorhersage der Klassen
pred = kmeans.fit_predict(data_unknown)  # Weist jeder Zeile eine Cluster-Klasse zu

# Zusammenfügen der Datensätze (Spalten)
data_new = pd.concat([df, pd.DataFrame(pred, columns=['label'])], axis=1)  # Fügt Cluster-Labels als neue Spalte hinzu
print(data_new)

# Speichern in neue CSV Datei
data_new.to_csv("csv_dateien/data_new.csv")  #Speichert das erweiterte Dataset als CSV
