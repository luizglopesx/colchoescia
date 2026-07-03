"""Publica feed + story do Post 3 — Anúncio Geral Colchões e Cia (10/07/2026)."""
import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo, publish_story

FEED_URL = "https://i.imgur.com/pOqntMg.png"
STORY_URL = "https://i.imgur.com/cTHAFCT.png"

CAPTION = (
    "Seu sono merece o melhor. E o melhor sempre coube aqui. 😴\n\n"
    "Colchão novo, entrega rápida em Barretos, montagem grátis na hora. "
    "Sem estresse, sem enrolação.\n\n"
    "Dormir bem não precisa ser complicado. Dá um pulo na loja ou manda um oi no WhatsApp.\n\n"
    "📍 Rua 20 Esq. Av. 13 — Centro — Barretos\n"
    "📱 WhatsApp: (17) 3324-5765\n\n"
    "Pensou Colchão, Colchões e Cia!\n\n"
    "#ColchoesECia #SonoDeQualidade #Colchao #LojaDeColchao #Barretos #DormirBem #EntregaGratis"
)

acc = _get_account('colchoes_e_cia')

print("=== FEED (Post 3 - Seu Sono Merece) ===")
r = publish_photo(acc, FEED_URL, CAPTION)
print(json.dumps(r, indent=2, ensure_ascii=False))

print("\n=== STORY (Post 3 - Seu Sono Merece) ===")
r2 = publish_story(acc, STORY_URL)
print(json.dumps(r2, indent=2, ensure_ascii=False))
