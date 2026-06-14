import os
import sys

# Adiciona o diretório pai (youtube_video_agent) ao sys.path
# Isso permite que os módulos dentro de src sejam importados corretamente
# quando os scripts são executados de dentro do diretório src ou do diretório raiz do projeto.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 
                                               os.pardir)))

from src.text_analyzer import analyze_text

def generate_image_for_keyword(keyword, output_dir, api_tool):
    """Gera uma imagem para uma única palavra-chave.

    Args:
        keyword (str): A palavra-chave para a qual gerar a imagem.
        output_dir (str): O diretório onde a imagem gerada será salva.
        api_tool: A ferramenta da API (ex: default_api) para chamar media_generate_image.

    Returns:
        str: O caminho para a imagem gerada.
    """
    # Define o caminho completo para salvar a imagem, substituindo espaços por underscores no nome do arquivo.
    image_path = os.path.join(output_dir, f'{keyword.replace(" ", "_")}.png')
    # Cria um prompt descritivo para a geração da imagem.
    prompt = f"A high-quality image representing the concept of {keyword}"
    
    print(f"Gerando imagem para: {keyword} em {image_path}")
    # Chama a ferramenta de geração de imagem da API.
    api_tool.media_generate_image(
        prompt=prompt, 
        path=image_path, 
        status=f"Gerando imagem para a palavra-chave: {keyword}",
        aspect_ratio="square" # Define a proporção da imagem como quadrada.
    )
    print(f"Imagem gerada e salva em: {image_path}")
    return image_path


def generate_images_from_text(text, output_dir, api_tool):
    """Analisa o texto, extrai palavras-chave e gera uma imagem para cada uma.

    Args:
        text (str): O texto da narração a ser analisado.
        output_dir (str): O diretório para salvar as imagens geradas.
        api_tool: A ferramenta da API para geração de imagens.

    Returns:
        list: Uma lista de caminhos para as imagens geradas.
    """
    # Analisa o texto para obter as palavras-chave.
    keywords = analyze_text(text)
    generated_image_paths = []
    # Itera sobre cada palavra-chave para gerar uma imagem.
    for keyword in keywords:
        path = generate_image_for_keyword(keyword, output_dir, api_tool)
        generated_image_paths.append(path)
    return generated_image_paths


