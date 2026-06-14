import json
import os

def save_metadata(data, filename="metadata.json", output_dir="../data"):
    """Salva os metadados fornecidos em um arquivo JSON no diretório especificado.

    Args:
        data (dict): Os dados (metadados) a serem salvos.
        filename (str): O nome do arquivo JSON (padrão: "metadata.json").
        output_dir (str): O diretório onde o arquivo JSON será salvo (padrão: "../data").

    Returns:
        str: O caminho completo para o arquivo JSON salvo.
    """
    # Garante que o diretório de saída exista, criando-o se necessário.
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)
    # Abre o arquivo em modo de escrita e salva os dados JSON com formatação indentada.
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Metadados salvos em: {filepath}")
    return filepath

def load_metadata(filename="metadata.json", input_dir="../data"):
    """Carrega os metadados de um arquivo JSON do diretório especificado.

    Args:
        filename (str): O nome do arquivo JSON (padrão: "metadata.json").
        input_dir (str): O diretório de onde o arquivo JSON será carregado (padrão: "../data").

    Returns:
        dict: Os metadados carregados do arquivo JSON, ou um dicionário vazio se o arquivo não existir.
    """
    filepath = os.path.join(input_dir, filename)
    # Verifica se o arquivo existe antes de tentar carregá-lo.
    if not os.path.exists(filepath):
        print(f"Arquivo de metadados não encontrado: {filepath}")
        return {}
    # Abre o arquivo em modo de leitura e carrega os dados JSON.
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"Metadados carregados de: {filepath}")
    return data


