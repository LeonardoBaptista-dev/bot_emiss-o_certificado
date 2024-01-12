from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import pandas as pd

def gerar_certificado(nome_curso, nome_participante, tipo_participacao, data_inicio, data_termino, carga_horaria, data_emissao_certificado):
    # Carrega a imagem de fundo do certificado
    imagem_certificado = Image.open("certificado_gerado.png")  # Substitua com o caminho para sua imagem de fundo

    # Inicializa o objeto ImageDraw para desenhar no certificado
    desenhador = ImageDraw.Draw(imagem_certificado)

    # Define a fonte e o tamanho do texto
    fonte = ImageFont.load_default()

    # Adiciona os dados ao certificado
    dados_certificado = {
        "Nome do Curso": nome_curso,
        "Nome Participante": nome_participante,
        "Tipo de Participação": tipo_participacao,
        "Data do Início": data_inicio,
        "Data do Término": data_termino,
        "Carga Horária (horas)": carga_horaria,
        "Data da Emissão do Certificado": data_emissao_certificado.strftime("%d/%m/%Y")
    }

    for linha, (chave, valor) in enumerate(dados_certificado.items()):
        texto = f"{chave}: {valor}"
        desenhador.text((100, 100 + linha * 30), texto, font=fonte, fill="black")  # Ajuste as coordenadas conforme necessário

    # Salva o certificado gerado
    imagem_certificado.save(f"certificado_{nome_participante.replace(' ', '_')}.png")

if __name__ == "__main__":
    # Lê a planilha
    df = pd.read_excel("dados_cursos.xlsx")

    # Itera sobre as linhas da planilha
    for index, row in df.iterrows():
        nome_curso = row["Nome do Curso"]
        nome_participante = row["Nome Participante"]
        tipo_participacao = row["Tipo de Participação"]
        data_inicio = row["Data do Início"]
        data_termino = row["Data do Término"]
        carga_horaria = row["Carga Horária (horas)"]
        data_emissao_certificado = datetime.now()  # Você pode ajustar conforme necessário

        # Chama a função para gerar o certificado
        gerar_certificado(nome_curso, nome_participante, tipo_participacao, data_inicio, data_termino, carga_horaria, data_emissao_certificado)
