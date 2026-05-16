from pathlib import Path 
import shutil

#Verificando a pasta do projeto 
pasta_projeto = Path(__file__).parent
print(f"--- Caminho da pasta do projeto ---\n {pasta_projeto}")

#criando nova pasta para os dados tratados análise exploratória
nova_pasta = pasta_projeto / "dados_tratados_analise_exploratoria"
nova_pasta.mkdir(exist_ok=True,parents=True)
print(f"pasta {nova_pasta} criada/já existe ")


#Movendo os arquivos "dados_tratados_exploracao.xls"
#shutil.move("dados_tratados_exploração.xlsx",nova_pasta)


#criando nova pasta para guardar os dados de pipilene limpeza de dados
nova_pasta_dados_tratados_pipeline = pasta_projeto / "pipeline/dadostratados"
nova_pasta_dados_tratados_pipeline.mkdir(exist_ok=True,parents=True)
print(f"Pasta criada {nova_pasta_dados_tratados_pipeline},ou já existente")

