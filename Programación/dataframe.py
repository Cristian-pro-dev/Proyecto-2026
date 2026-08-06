import pandas as pd 

datos = {
    "Nombre" : ["Cristian", "Ana", "Alan", "Alexa", "Gabriel"],
    "Carrera" : ["IA", "ISC", "IQ", "IA", "DATA"],
    "Profesor" : ["Montiel", "Gerardo", "Mujica", "Sonia", "Aquino"],
    "Practica" : ["Segunda", "Tercera", "Cuarta", "Segunda", "Primera"],
    "Calificacion" : [9.5, 8.7, 7.8, 6.9, 9.3]
}

df = pd.DataFrame(datos)

print(df)
print("\n")
print(df[["Nombre", "Calificacion"]])
print("\n")
print(df.iloc[2])
print("\n")
df.info()
print("\n")
df.describe()

