"""Publica feed + story do Post 2 — Facilidade de Pagamento Colchões e Cia (31/07/2026)."""
import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo, publish_story

FEED_URL = "https://i.imgur.com/7O6KbHJ.png"
STORY_URL = "https://i.imgur.com/4xBv4ia.png"

CAPTION = (
    "Compra fácil, sem enrolação. 📋\n\n"
    "Parcelamento simples, direto com quem atende você — sem complicação pra fechar.\n\n"
    "Passa na loja ou liga pra gente. A gente resolve rápido, sem rodeio.\n\n"
    "📍 Rua 20 Esq. Av. 13 — Centro — Barretos\n"
    "📞 (17) 3325-6039\n\n"
    "Pensou Colchão, Colchões e Cia!\n\n"
    "#ColchoesECia #Parcelamento #SemJuros #Colchao #LojaDeColchao #Barretos #ComprasFaceis #ColchaoBom"
)

acc = _get_account('colchoes_e_cia')

print("=== FEED (Post 2 - Compra Fácil, Sem Enrolação) ===")
r = publish_photo(acc, FEED_URL, CAPTION)
print(json.dumps(r, indent=2, ensure_ascii=False))

print("\n=== STORY (Post 2 - Compra Fácil, Sem Enrolação) ===")
r2 = publish_story(acc, STORY_URL)
print(json.dumps(r2, indent=2, ensure_ascii=False))
