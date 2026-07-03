"""Publica feed + story do Post 1 — Anúncio Geral Colchões e Cia (06/07/2026)."""
import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo, publish_story

FEED_URL = "https://i.imgur.com/OipuBpU.png"
STORY_URL = "https://i.imgur.com/Ny6m52O.png"

CAPTION = (
    "Dormir bem não é luxo. É coisa de quem sabe onde comprar. 🛏️\n\n"
    "A gente existe pra isso: colchão bom, preço justo, sem conversa fiada. "
    "Entrega e montagem grátis, parcelamento sem juros e aquele atendimento "
    "de vizinho que você já conhece.\n\n"
    "Vem dar uma olhada. Sem compromisso.\n\n"
    "📍 Rua 20 Esq. Av. 13 — Centro — Barretos\n"
    "📱 WhatsApp: (17) 3324-5765\n\n"
    "Pensou Colchão, Colchões e Cia!\n\n"
    "#ColchoesECia #DormirBem #Colchao #LojaDeColchao #Barretos #PrecoJusto #QualidadeDeSono"
)

acc = _get_account('colchoes_e_cia')

print("=== FEED (Post 1 - Dormir Bem) ===")
r = publish_photo(acc, FEED_URL, CAPTION)
print(json.dumps(r, indent=2, ensure_ascii=False))

print("\n=== STORY (Post 1 - Dormir Bem) ===")
r2 = publish_story(acc, STORY_URL)
print(json.dumps(r2, indent=2, ensure_ascii=False))
