import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

# Inicializa o Faker para dados fictícios
fake = Faker()

# Gera dados fictícios para 100 participantes
dados = []
for _ in range(100):
    nome_curso = fake.job()  # Gera um nome de curso aleatório
    nome_participante = fake.name()
    tipo_participacao = random.choice(['Presencial', 'Online'])
    data_inicio = fake.date_between(start_date='-365d', end_date='today')
    data_termino = data_inicio + timedelta(days=random.randint(1, 30))
    carga_horaria = random.randint(10, 40)
    data_emissao_certificado = data_termino + timedelta(days=random.randint(1, 7))
    
    dados.append([nome_curso, nome_participante, tipo_participacao, data_inicio, data_termino, carga_horaria, data_emissao_certificado])

# Cria um DataFrame com os dados
colunas = ['Nome do Curso', 'Nome Participante', 'Tipo de Participação', 'Data do Início', 'Data do Término', 'Carga Horária (horas)', 'Data da Emissão do Certificado']
df = pd.DataFrame(dados, columns=colunas)

# Salva o DataFrame em um arquivo .xlsx
df.to_excel('dados_cursos.xlsx', index=False)
