import pandas as pd
import glob
import os
from utils_log import log_decorator
# import pandera.pandas as pa
# import pandera.typing as pat
# from schema import VendasSchema
# from pathlib import Path
# from pandera.typing import Series

#@pa.check_output(VendasSchema)
@log_decorator
def extrair_dados(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    print(df_total)
    return df_total
@log_decorator
def transformar_dados(df: pd.DataFrame):
    df['Receita'] = df['Quantidade'] * df['Venda']
    print(df)
    return df
@log_decorator
def carregar_dados(df: pd.DataFrame, formatos: list):

    for formato in formatos:
        if formato == 'csv':
            df.to_csv("dados.csv", index=False)
        elif formato == 'parquet':
            df.to_parquet( "dados.parquet", index=False)
@log_decorator
def pipeline(pasta_entrada: str, formato_saida: str):
    dados = extrair_dados(pasta_entrada)
    dados_transformados = transformar_dados(dados)
    carregar_dados(dados_transformados, formato_saida)