import os
import sys

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 
                                               os.pardir)))

from main import process_narration

# Este é um script de teste que simula a chamada do agente.
# Ele passa a ferramenta `default_api` para a função `process_narration`.

if __name__ == '__main__':
    # Caminho para o arquivo de narração fornecido pelo usuário
    narration_filepath = "/home/ubuntu/upload/pasted_content.txt"
    video_title = "O Mistério de Varginha"

    print(f"Iniciando o teste de geração de imagens para o vídeo: {video_title}")
    print(f"Usando o texto de narração do arquivo: {narration_filepath}")

    # A ferramenta default_api é injetada pelo ambiente do agente.
    # Aqui, estamos simulando essa injeção.
    try:
        process_narration(narration_filepath, video_title, default_api)
        print("Teste de geração de imagens concluído com sucesso!")
    except NameError:
        print("Erro: 'default_api' não está definido. Este script deve ser executado pelo agente.")
    except Exception as e:
        print(f"Ocorreu um erro durante a execução do teste: {e}")


