import pandas as pd
import numpy as np
import os
from sqlalchemy import create_engine
from app.conf import DB_URI

def load_csv_file():
    path = os.path.join(os.path.curdir, "data/respostas.csv")
    df = pd.read_csv(path)
    df.columns = ["data", "nps", "nps_beleza", "sexo", "sugestao"]
    return df

def nps_calc(dataframe):
    dataframe = dataframe.copy()
    dataframe["nps_desc"] = "neutra"
    dataframe.nps_desc = np.where((dataframe.nps>=9) & (dataframe.nps<=10), "promotora", dataframe.nps_desc)
    dataframe.nps_desc = np.where((dataframe.nps<6), "detratora", dataframe.nps_desc)
    return dataframe

def insert_rows_db():
    NOME_TABELA = "respostas_nps"
    engine = create_engine(DB_URI)
    df = nps_calc(load_csv_file())
    df.to_sql(NOME_TABELA, engine, if_exists='replace', index=False)
