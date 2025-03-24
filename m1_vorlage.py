import pandas as pd

def mylog(msg):
    print("*"*50)
    print(msg)
    print("*"*50)


mylog("Datei einlesen")
df = pd.read_csv('csv_dateien/mushrooms.csv')
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

mylog("Spalte 'class' ausgeben")
print(df['class'])
mylog("Datentyp der Spalte 'class' ausgeben")
print(type(df['class']))

mylog("Bedingte Auswahl")
eatable = df[df['class'] == 'e']
mylog(eatable)

eatable_x = df[(df['class'] == 'e') & (df['cap-shape'] == 'x')]
mylog(eatable_x)

df_cleaned = df[df['class'] != 'n']