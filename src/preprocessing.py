import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

################################
# One hot encoder              #
################################

def one_hot_encoder(df):
    """Applies one hot encoder to the feature "escuela". We only keep n - 1 features, n being the
    amount of different shcools. """
    letters = ["A", "B", "C", "D", "E", "F", "G"] #no me quedo con el H
    for i in range(len(letters)):
        df.insert(i, letters[i], (df["escuela"] == letters[i]).astype(int)) #position, name, info
    df = df.drop(columns=["escuela"]) #we don't need it anymore
    return df

################################
# Limpiar dataset              #
################################

def gestionar_valores_faltantes(df):
    """Manejo los valores faltantes (Nan)
    Dependiendo del caso imputo el dato o bien lo corrijo"""

    #df = df.fillna({"pisos": 1}) 
    df = df.dropna() #elimino las filas que tienen nan 
    return df

def fix_data(df):
    """:
    - one hot encoding to "escuela"
    - "semestre" is no longer a categorical feature: it is an ordinal
    - separation of "rendimiento" between "rendimiento_bin" (pass or fail),
    and "rendimiento_mul" (different scales for passing) 
    """
    df["escuela"] = df["escuela"].str.upper()
    df = one_hot_encoder(df) #one hot encoding of "escuela"

    dict_semesters = {"2022-1": 1, "2022-2": 2, "2023-1": 3, "2023-2": 4, "2024-1": 5, "2024-2": 6}
    df["semestre"] = df["semestre"].map(dict_semesters)

    dict_performance_bin = {"Excelente": 1, "Bueno": 1, "Regular": 1, "Insuficiente": 0}
    dict_performance_mult = {"Excelente": 3, "Bueno": 2, "Regular": 1, "Insuficiente": 0}
    df["rendimiento_bin"] = df["rendimiento"].map(dict_performance_bin)
    df["rendimiento_mult"] = df["rendimiento"].map(dict_performance_mult)
    df = df.drop(columns = "rendimiento")
    #elimino datos corrompidosjjjjjj
    return df