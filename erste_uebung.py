import pandas as pd


#Übung 1: Daten einlesen und inspizieren
#1. Daten einlesen: Laden Sie den Datensatz iris.csv in einen Pandas DataFrame.
#2. Datensatz erkunden: Zeigen Sie die ersten und die letzten Zeilen des DataFrames an.
#3. Zusammenfassung: Erhalten Sie eine Zusammenfassung des DataFrames mit Informationen zu jeder Spalte (Datentypen, Anzahl der Nicht-Null-Einträge usw.).
def mylog(msg):
    print("*"*50)
    print(msg)
    print("*"*50)


mylog("Datei einlesen")
df = pd.read_csv('csv_dateien/iris (1).csv')
mylog("Erste 5 Zeilen ausgeben")
print(df.head())
mylog("letzte 10 Zeilen ausgeben")
print(df.tail(10))
mylog("Datentyp ausgeben")
print(type(df))
mylog("Spaltennamen ausgeben")
print(df.columns)
mylog("Anzahl der Zeilen und Spalten ausgeben")
print(df.shape)
mylog("Informatioene zum DataFrame ausgeben")
print(df.info())





#Übung 2: Auswahl und Filterung
#4. Spalten auswählen: Wählen Sie die Spalten sepal_length und sepal_width aus und zeigen Sie die ersten 10 Zeilen an.
#5. Bedingte Auswahl: Filteren Sie die Daten, um nur die Zeilen anzuzeigen, bei denen die species 'setosa' ist.
#6. Mehrere Bedingungen: Finden Sie alle Einträge, bei denen die petal_length größer als 1.5 ist und die species 'versicolor' ist.

mylog("Spalte 'sepal.length' ausgeben")
print(df.head(10)['sepal.length'])

mylog("Spalte 'sepal.width' ausgeben")
print(df.head(10)['sepal.width'])

mylog("gleichzeitige Ausgabe von zwei Spalten")
df_2 = df[['sepal.length', 'sepal.width']]
print(df_2.head(10))

mylog("Bedingte Auswahl")
setosa = df[df['species'] == 'Setosa']
mylog(setosa)

mehrere = df[(df['species'] == 'Versicolor') & (df['petal.length'] > 1.5)]
mylog(mehrere)






#Übung 3: Datenbearbeitung
#7. Neue Spalte hinzufügen: Berechnen Sie die Fläche des Sepal (Sepal Length * Sepal Width) und fügen Sie sie als neue Spalte sepal_area hinzu.
#8. Werte ändern: Ersetzen Sie in der species-Spalte die Werte 'setosa', 'versicolor' und 'virginica' durch 'S', 'Ve' und 'Vi'. (Methode replace)
#9. Zeilen löschen: Entfernen Sie alle Zeilen, in denen die sepal_length kleiner als 4.5 ist.

# 7. Neue Spalte 'sepal_area' hinzufügen
mylog("sepel_area hinzufügen")
df["sepal_area"] = df["sepal.length"] * df["sepal.width"]
print(df.head(10))

# 8. Werte in der Spalte 'species' ersetzen
mylog("Werte ersetzen")
df["species"] = df["species"].replace({
    "Setosa": "S",
    "Versicolor": "Ve",
    "Virginica": "Vi"
})
print(df.head(10))

# 9. Zeilen löschen, wenn 'sepal_length' kleiner als 4.5 ist
mylog("Zeile löschen")
df = df[df["sepal.length"] >= 4.5]
print(df.head(10))




