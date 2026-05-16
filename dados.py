import pandas as pd 
import shutil
from pathlib import Path
import logging

logging.basicConfig(
    filename='pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class PipelineDados:

    def __init__(self,caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo
        self.df = None

    def lendo_arquivo(self):
        try:
            self.df = pd.read_excel(self.caminho_arquivo)  

            logging.info(
                f"Arquivo '{self.caminho_arquivo}' carregado com sucesso")      

        except FileNotFoundError:
            logging.error(f"Erro: arquivo '{self.caminho_arquivo}' não encontrado")
            
        except Exception as e:
            logging.error(f"Ocorreu um erro ao ler o arquivo: {e}")    

    def limpeza_dados(self):
        self.df = self.df.dropna(subset=["nome_produto"])
        logging.info("Ajuste feito - Limpeza de dados")

    def padronizando_colunas(self):
        self.df["data_venda"] = pd.to_datetime(self.df["data_venda"],errors="coerce")
        self.df["id_venda"] =  self.df["id_venda"].astype(str)
        self.df["nome_produto"] = self.df["nome_produto"].str.strip().str.capitalize()
        self.df["categoria"] = self.df["categoria"].str.strip().str.capitalize()
        self.df["vendedor"] = self.df["vendedor"].str.strip().str.title()
        logging.info("Ajuste feito - padronização das colunas realizados")

    def salvando_arquivo(self):
        pipeline = Path("pipeline")
        pipeline.mkdir(exist_ok=True)

        caminho_completo = pipeline / "dados_tratados_pipeline.xlsx"
        self.df.to_excel(caminho_completo, index=False)
        logging.info("Aqruivo tratado salvo!")

    def execute(self):
        self.lendo_arquivo()
        self.limpeza_dados()
        self.padronizando_colunas()
        self.salvando_arquivo()

        logging.info("Pipeline executado com sucesso")




if __name__ == "__main__":


    caminho_arquivo = "nome_do_arquivo.xlsx"
    pipeline = PipelineDados(caminho_arquivo)
    pipeline.execute()

        









        