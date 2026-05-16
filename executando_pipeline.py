from dados import PipelineDados

#definindo a variável que irá compor nossa base de dados 
caminho = "base_vendas_tecnologia_pipeline.xlsx"

#variavel da classe 
pipeline = PipelineDados(caminho)
pipeline.execute()

