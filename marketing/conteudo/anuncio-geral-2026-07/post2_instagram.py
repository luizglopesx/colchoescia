"""Publica feed + story do Post 2 — Anúncio Geral Colchões e Cia (08/07/2026)."""
import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo, publish_story

FEED_URL = "https://i.imgur.com/TnycqK4.png"
STORY_URL = "https://i.imgur.com/uBSo2F5.png"

CAPTION = (
    "Preço de vizinho. Qualidade de verdade. 💰\n\n"
    "Colchão novo com parcelamento que cabe no seu bolso: em até 12x sem juros "
    "e sem entrada no carnê. Do jeito que o povo gosta.\n\n"
    "Passa na loja ou chama no WhatsApp. O Joaquim separa o melhor colchão pra você.\n\n"
    "📍 Rua 20 Esq. Av. 13 — Centro — Barretos\n"
    "📱 WhatsApp: (17) 3324-5765\n\n"
    "Pensou Colchão, Colchões e Cia!\n\n"
    "#ColchoesECia #PrecoDeVizinho #Colchao #LojaDeColchao #Barretos #Oferta #Parcelamento"
)

acc = _get_account('colchoes_e_cia')

print("=== FEED (Post 2 - Preço de Vizinho) ===")
r = publish_photo(acc, FEED_URL, CAPTION)
print(json.dumps(r, indent=2, ensure_ascii=False))

print("\n=== STORY (Post 2 - Preço de Vizinho) ===")
r2 = publish_story(acc, STORY_URL)
print(json.dumps(r2, indent=2, ensure_ascii=False))
