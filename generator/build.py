import json
import random
import uuid
from .blocks import *

def make_theme():
    adj = random.choice(adjetivos)
    dom = random.choice(dominios)
    foco = random.choice(focos)

    return {
        "id": str(uuid.uuid4())[:8],
        "título": f"{adj} da {dom} em {foco}",
        "descrição": (
            f"Explora a ontologia da {dom} quando mediada por {foco}: "
            "quais entidades conceituais aparecem, como se articulam as "
            "propriedades essenciais e implicações para agência."
        ),
        "pergunta_central": random.choice(perguntas),
        "subperguntas": [
            f"Como definimos identidade ontológica para {foco}?",
            f"Que critérios justificam responsabilidade quando {foco} opera?",
            f"Que categorias precisam ser reformadas para acomodar {foco}?"
        ],
        "escopo": random.choice(["teórico","aplicado","híbrido"]),
        "métodos_sugeridos": random.sample(metodos, 3),
        "palavras_chave": random.sample(keywords_base, 6),
        "implicacoes_eticas": [
            "potencial deslocamento de responsabilidade humana",
            "risco de reificação de agentes artificiais"
        ],
        "provocacao_pratica": (
            "Construir um protótipo conceitual mapeando entidades e relações "
            "e testar com estudo de caso aplicado."
        ),
        "nivel": random.choice(["exploratório","mestrado","doutorado","pôster/conferência"])
    }

def generate(n=10):
    return [make_theme() for _ in range(n)]
