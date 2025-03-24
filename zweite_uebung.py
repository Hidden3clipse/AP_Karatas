import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Daten einlesen und inspizieren
#1. Daten einlesen: Laden Sie den Datensatz wine-red.csv in einen Pandas DataFrame.
#2. Datensatz erkunden: Zeigen Sie die ersten und die letzten Zeilen des DataFrames an.
#3. Zusammenfassung: Erhalten Sie eine Zusammenfassung des DataFrames mit Informationen zu jeder Spalte (Datentypen, Anzahl der Nicht-Null-Einträge usw.).
def mylog(msg):
    print("*"*50)
    print(msg)
    print("*"*50)


mylog("Datei einlesen")
df = pd.read_csv('csv_dateien/winequality-red.csv', delimiter=';')
mylog("Erste 5 Zeilen ausgeben")
print(df.head())
mylog("Informatioene zum DataFrame ausgeben")
print(df.info())


#Auswahl und Filterung
#4. Spalten auswählen: Wählen Sie die Spalten alcohol und ph aus und zeigen Sie die ersten 10 Zeilen an.
#5. Bedingte Auswahl: Filteren Sie die Daten, um nur die Zeilen anzuzeigen, bei denen die quality genau 8 ist.
#6. Mehrere Bedingungen: Finden Sie alle Einträge, bei denen der Alkoholgehalt größer als 12.5 ist und die Qualität mindestens 7 ist.

mylog("gleichzeitige Ausgabe von zwei Spalten")
df_2 = df[['pH', 'alcohol']]
print(df_2.head(10))

mylog("Bedingte Auswahl")
quality = df[df['quality'] == 8]
mylog(quality)

mylog("mehrere Bedingungen")
mehrere = df[(df['alcohol'] > 12.5) & (df['quality'] >= 7)]
mylog(mehrere)




#Datenbearbeitung
#7. Neue Spalte hinzufügen: Berechnen Sie den density_alcohol_ratio (Dichte / Alkoholgehalt) und fügen Sie ihn als neue Spalte hinzu.
#8. Werte ändern:
#8. Ersetzen Sie die Werte in der quality-Spalte wie folgt:
#	Qualität 3 → "sehr schlecht"
#	Qualität 4 → "schlecht"
#	Qualität 5 → "okay"
#	Qualität 6 → "gut"
#	Qualität 7+ → "sehr gut"

# 7. Neue Spalte hinzufügen
mylog("density_alcohol_ratio hinzufügen")
df["density_alcohol_ratio"] = df["density"] * df["alcohol"]
print(df.head(10))


# 8. Werte in der Spalte ersetzen
mylog("Werte ersetzen")
df["quality"] = df["quality"].replace({
    "3": "sehr schlecht",
    "4": "schlecht",
    "5": "okay",
    "6": "gut",
    "7": "sehr gut",
})
print(df.head(10))



#10. Entfernen Sie alle Zeilen, in denen der pH-Wert kleiner als 3.0 ist.
mylog("Zeile löschen")
df = df[df["pH"] >= 3.0]
print(df.head(10))

#11. Geben Sie die Spaltenüberschriften aus.
mylog("Spaltenüberschriften ausgeben")
print(df.columns)


#12. Ersetzen Sie die Spaltenüberschriften mit deutschen Bezeichnern.
mylog("Spaltenüberschriften mit deutschen Bezeichnern")
df.rename(columns={
        'fixed acidity': 'feste Säure', 'volatile acidity': 'flüchtige Säure', 'citric acid': 'Zitronensäure', 'residual sugar': 'Restzucker',
        'chlorides': 'Chloride', 'free sulfur dioxide': 'freier Schwefeldioxid', 'total sulfur dioxide': 'gesamter Schwefeldioxid', 'density': 'Dichte',
        'pH': 'pH-Wert', 'sulphates': 'Sulfate', 'alcohol': 'Alkohol', 'quality': 'Qualität', 'density_alcohol_ratio': 'Dichte-Alkohol-Verhältnis'
		}, inplace=True)
print(df.columns)





#Visualisierung
#13. Plotten Sie Alkohol vs Qualität mit Seaborn (Scatterplot)
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Alkohol', y='Qualität', hue='Qualität', data=df, alpha=0.6, s=70)
plt.title('Alkohol vs. Qualität (Eingefärbt nach Qualität)')
plt.legend(title='Qualität')
plt.show()
