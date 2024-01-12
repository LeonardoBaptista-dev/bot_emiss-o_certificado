from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

def criar_certificado(nome_curso, nome_participante, tipo_participacao, data_inicio, data_termino, carga_horaria, data_emissao_certificado):
    # Cria uma imagem em branco
    imagem_certificado = Image.new('RGB', (800, 600), 'lightblue')
    desenhador = ImageDraw.Draw(imagem_certificado)

    # Define a fonte e o tamanho do texto
    fonte_titulo = ImageFont.load_default()
    fonte_texto = ImageFont.load_default()

    # Adiciona elementos ao certificado
    desenhador.text((200, 50), f"Certificado de Conclusão", font=fonte_titulo, fill="darkblue")
    desenhador.text((50, 120), f"Curso: {nome_curso}", font=fonte_texto, fill="darkblue")
    desenhador.text((50, 170), f"Participante: {nome_participante}", font=fonte_texto, fill="darkblue")
    desenhador.text((50, 220), f"Tipo de Participação: {tipo_participacao}", font=fonte_texto, fill="darkblue")
    desenhador.text((50, 270), f"Data de Início: {data_inicio}", font=fonte_texto, fill="darkblue")
    desenhador.text((50, 320), f"Data de Término: {data_termino}", font=fonte_texto, fill="darkblue")
    desenhador.text((50, 370), f"Carga Horária: {carga_horaria} horas", font=fonte_texto, fill="darkblue")
    desenhador.text((50, 420), f"Data de Emissão: {data_emissao_certificado.strftime('%d/%m/%Y')}", font=fonte_texto, fill="darkblue")

    # Salva o certificado gerado
    imagem_certificado.save("certificado_gerado.png")

if __name__ == "__main__":
    # Dados fictícios para o certificado
    nome_curso = "Curso de Exemplo"
    nome_participante = "João da Silva"
    tipo_participacao = "Presencial"
    data_inicio = "01/01/2022"
    data_termino = "15/01/2022"
    carga_horaria = "20"
    data_emissao_certificado = datetime.now()

    # Gera o certificado com os dados fornecidos
    criar_certificado(nome_curso, nome_participante, tipo_participacao, data_inicio, data_termino, carga_horaria, data_emissao_certificado)
