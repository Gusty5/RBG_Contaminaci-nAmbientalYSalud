import pandas as pd
df = pd.read_csv("../data/calidad_aire_2025.csv")

df_sum = df.groupby(["Entidad", "Municipio"], as_index=False).sum(numeric_only=True)
df_sum.to_csv("../data_util/Emisiones_municipio.csv", index=False)