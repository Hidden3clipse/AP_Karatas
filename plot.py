
import  matplotlib.pyplot as plt
import pandas as pd


df=pd.read_csv("csv_dateien/iris (1).csv")


plt.scatter(df["sepal_length"],df["sepal_width"],c="blue",alpha=0.5)

plt.xlabel("SepalLength")
plt.ylabel("SepalWidth")
plt.title("Scatterplot:SepalLengthvs.SepalWidth")
plt.show()



import seaborn as sns
import matplotlib.pyplot as plt

sns.scatterplot(data=df,x="sepal_length",y="sepal_width",hue="species")

plt.xlabel("SepalLength")
plt.ylabel("SepalWidth")
plt.title("Scatterplot:SepalLengthvs.SepalWidthnachSpecies")
plt.show()

#--> Vorteile: Farbunterscheidung, automatische Legende
