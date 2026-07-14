"""Publica feed + story do Post 2 — Preço e Acesso Colchões e Cia (17/07/2026)."""
import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo, publish_story

FEED_URL = "https://i.imgur.com/mhyMjcT.png"
STORY_URL = "https://i.imgur.com/p87z7TW.png"

CAPTION = (
    "Parcela que cabe no bolso. 💳\n\n"
    "Colchão novo em até 12x sem juros e sem entrada no carnê. Do jeito que o "
    "povo gosta, sem letra miúda.\n\n"
    "Passa na loja ou chama no WhatsApp. O Joaquim monta o parcelamento certo pra você.\n\n"
    "📍 Rua 20 Esq. Av. 13 — Centro — Barretos\n"
    "📱 WhatsApp: (17) 3325-6039\n\n"
    "Pensou Colchão, Colchões e Cia!\n\n"
    "#ColchoesECia #Parcelamento #Colchao #LojaDeColchao #Barretos #Oferta #SemJuros"
)

acc = _get_account('colchoes_e_cia')

print("=== FEED (Post 2 - Parcela Que Cabe No Bolso) ===")
r = publish_photo(acc, FEED_URL, CAPTION)
print(json.dumps(r, indent=2, ensure_ascii=False))

print("\n=== STORY (Post 2 - Parcela Que Cabe No Bolso) ===")
r2 = publish_story(acc, STORY_URL)
print(json.dumps(r2, indent=2, ensure_ascii=False))
