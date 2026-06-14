# Agente de Geração de Vídeos para YouTube

Este projeto tem como objetivo criar um agente em Python capaz de gerar imagens a partir de um texto de narração, que podem ser posteriormente utilizadas para a criação de vídeos para o YouTube. O agente irá analisar o texto fornecido, identificar conceitos-chave e gerar imagens visuais correspondentes, organizando-as de forma estruturada para facilitar a edição de vídeo.

## Funcionalidades:

- Análise de texto para extração de palavras-chave/conceitos.
- Geração de imagens visuais com base nos conceitos extraídos.
- Organização estruturada das imagens geradas e metadados.

## Como usar:

Instruções detalhadas serão fornecidas nas próximas fases do desenvolvimento.

## Estrutura do Projeto:

```
youtube_video_agent/
├── src/                 # Código-fonte do agente
├── data/                # Dados auxiliares ou de configuração
├── images/              # Imagens geradas
├── README.md            # Este arquivo
├── requirements.txt     # Dependências do projeto
└── todo.md              # Tarefas do projeto
```




## Uso:

Para usar o agente, você precisará fornecer o texto da narração e um título para o vídeo. O agente irá:

1. Analisar o texto da narração para extrair palavras-chave.
2. Gerar imagens com base nessas palavras-chave.
3. Salvar as imagens geradas na pasta `images/`.
4. Criar um arquivo JSON de metadados na pasta `data/` que mapeia o texto da narração e as palavras-chave às imagens geradas.

### Exemplo de execução (pelo agente):

```python
# Este é um exemplo de como o agente chamaria a função principal
from main import process_narration

sample_narration = """
Neste vídeo, vamos explorar a beleza da natureza, desde florestas exuberantes até oceanos profundos.
Descubra a vida selvagem e os ecossistemas incríveis que nosso planeta oferece.
"""
sample_video_title = "Beleza da Natureza"

# O agente passaria a ferramenta default_api para a função
process_narration(sample_narration, sample_video_title, default_api)
```

Após a execução, você encontrará as imagens geradas na pasta `youtube_video_agent/images/` e o arquivo de metadados correspondente na pasta `youtube_video_agent/data/`.


