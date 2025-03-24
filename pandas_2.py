#Wenn eine CSV-Datei keine Spaltenüberschriften hat, können Sie wie folgt welche definieren:
#df.columns = ["Länge Kelchblatt", "Breite Kelchblatt", "Länge Blütenblatt", "Breite Blütenblatt", "Pflanzenart"]


# Vorhandene Spaltenüberschriften können Sie wie folgt definieren:
#df.rename(columns={
#		"Länge Kelchblatt": "Kelch_L", "Breite Kelchblatt": "Kelch_B", "Länge Blütenblatt": "Blüte_L", "Breite Blütenblatt": "Blüte_B", "Pflanzenart": "Art"
#		}, inplace=True)


#Spaltenüberschriften löschen: df.columns = range(df.shape[1])