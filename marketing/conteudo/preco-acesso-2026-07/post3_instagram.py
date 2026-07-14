"""Publica feed + story do Post 3 — Preço e Acesso Colchões e Cia (20/07/2026)."""
import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo, publish_story

FEED_URL = "https://i.imgur.com/oaDpRRK.png"
STORY_URL = "https://i.imgur.com/rWoDLUZ.png"

CAPTION = (
    "Preço claro, sem pegadinha. 🔍\n\n"
    "O que você vê na loja é o que você paga. Sem letra miúda, sem taxa "
    "escondida — do jeito que a gente sempre fez.\n\n"
    "Passa na loja ou chama no WhatsApp. Preço na lata, sem enrolação.\n\n"
    "📍 Rua 20 Esq. Av. 13 — Centro — Barretos\n"
    "📱 WhatsApp: (17) 3324-5765\n\n"
    "Pensou Colchão, Colchões e Cia!\n\n"
    "#ColchoesECia #PrecoClaro #Colchao #LojaDeColchao #Barretos #Oferta #SemPegadinha"
)

acc = _get_account('colchoes_e_cia')

print("=== FEED (Post 3 - Preço Claro, Sem Pegadinha) ===")
r = publish_photo(acc, FEED_URL, CAPTION)
print(json.dumps(r, indent=2, ensure_ascii=False))

print("\n=== STORY (Post 3 - Preço Claro, Sem Pegadinha) ===")
r2 = publish_story(acc, STORY_URL)
print(json.dumps(r2, indent=2, ensure_ascii=False))
