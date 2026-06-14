import os
import sys
import json

# Adiciona o diretório raiz do projeto (onde main.py está) ao sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.text_analyzer import analyze_text
from src.image_generator import generate_images_from_text
from src.metadata_manager import save_metadata

def process_narration(narration_filepath, video_title, api_tool):
    """Processa o texto da narração de um arquivo, gera imagens e salva metadados.
    """
    with open(narration_filepath, "r", encoding="utf-8") as f:
        narration_text = f.read()

    output_image_dir = "images"
    output_data_dir = "data"
    os.makedirs(output_image_dir, exist_ok=True)
    os.makedirs(output_data_dir, exist_ok=True)

    print("Analisando o texto da narração...")
    keywords = analyze_text(narration_text)
    print(f"Palavras-chave extraídas: {keywords}")

    print("Gerando imagens...")
    generated_image_paths = generate_images_from_text(narration_text, output_image_dir, api_tool)
    print(f"Caminhos das imagens geradas: {generated_image_paths}")

    metadata = {
        "video_title": video_title,
        "narration_text": narration_text,
        "keywords": keywords,
        "generated_images": generated_image_paths
    }

    print("Salvando metadados...")
    clean_video_title = video_title.replace(" ", "_").lower()
    metadata_filepath = save_metadata(metadata, filename=f"{clean_video_title}_metadata.json", output_dir=output_data_dir)
    print(f"Metadados salvos em: {metadata_filepath}")
    
    return metadata_filepath

# A função principal que o agente chamará
def run_agent(narration_filepath, video_title, api_tool):
    return process_narration(narration_filepath, video_title, api_tool)