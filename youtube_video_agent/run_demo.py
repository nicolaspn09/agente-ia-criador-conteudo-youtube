import os
import sys

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))

from main import run_agent

if __name__ == "__main__":
    # Exemplo de uso
    narration_file = r"C:\Users\nicol\Downloads\Narrador.txt"  # Caminho para o arquivo de narração
    video_title = "Meu Video Incrível"
    # api_tool = "openai"  # Ou outro serviço de geração de imagens

    metadata_file = run_agent(narration_file, video_title, default_api)
    print(f"Processamento concluído. Metadados salvos em: {metadata_file}")

# if __name__ == '__main__':
#     narration_filepath = "/home/ubuntu/upload/pasted_content.txt"
#     video_title = "O Mistério de Varginha"

#     print(f"Iniciando a demonstração para o vídeo: {video_title}")
#     print(f"Usando o texto de narração do arquivo: {narration_filepath}")

#     try:
#         # O default_api é injetado pelo ambiente do agente
#         run_agent(narration_filepath, video_title, default_api)
#         print("Demonstração concluída com sucesso!")
#     except NameError:
#         print("Erro: \'default_api\' não está definido. Este script deve ser executado pelo agente.")
#     except Exception as e:
#         print(f"Ocorreu um erro durante a execução da demonstração: {e}")


