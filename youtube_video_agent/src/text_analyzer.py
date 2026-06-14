import re

def analyze_text(text):
    """Analisa o texto para extrair palavras-chave simples.
    Atualmente, considera palavras com mais de 4 letras como palavras-chave.
    Remove pontuações e converte o texto para minúsculas para padronização.
    Retorna uma lista de palavras-chave únicas.
    """
    # Remove caracteres que não são letras ou espaços e converte para minúsculas
    text = re.sub(r'[^a-zA-Z\s]+', '', text.lower())
    words = text.split() # Divide o texto em palavras
    # Filtra palavras com mais de 4 letras para serem consideradas palavras-chave
    keywords = [word for word in words if len(word) > 4]
    return list(set(keywords)) # Retorna palavras-chave únicas para evitar duplicações

if __name__ == '__main__':
    # Exemplo de uso do analisador de texto
    sample_text = """
    Olá a todos! No vídeo de hoje, vamos explorar as maravilhas do universo.
    Falaremos sobre estrelas distantes, galáxias misteriosas e a possibilidade de vida em outros planetas.
    Preparem-se para uma jornada incrível pelo cosmos!
    """
    
    keywords = analyze_text(sample_text)
    print(f"Texto de exemplo: {sample_text}")
    print(f"Palavras-chave extraídas: {keywords}")


