"""Publica feed + story do Post 2 — Espuma Com Firmeza De Verdade, Colchões e Cia (24/07/2026)."""
import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo, publish_story

FEED_URL = "https://i.imgur.com/pNdJkVB.png"
STORY_URL = "https://i.imgur.com/a9wC3dk.png"

CAPTION = (
    "Espuma com firmeza de verdade. 🛌\n\n"
    "O colchão de espuma é mais denso e mantém a base firme a noite toda, sem "
    "afundar com o tempo. Ótimo pra quem gosta de dormir numa superfície mais "
    "dura e sente falta de sustentação.\n\n"
    "Vem na loja sentir a diferença. A gente te ajuda a escolher o modelo certo.\n\n"
    "📍 Rua 20 Esq. Av. 13 — Centro — Barretos\n"
    "📞 (17) 3325-6039\n\n"
    "Pensou Colchão, Colchões e Cia!\n\n"
    "#ColchoesECia #ColchaoDeEspuma #DormirBem #ConfortoNaCama #LojaDeColchao #Barretos"
)

acc = _get_account('colchoes_e_cia')

print("=== FEED (Post 2 - Espuma Com Firmeza De Verdade) ===")
r = publish_photo(acc, FEED_URL, CAPTION)
print(json.dumps(r, indent=2, ensure_ascii=False))

print("\n=== STORY (Post 2 - Espuma Com Firmeza De Verdade) ===")
r2 = publish_story(acc, STORY_URL)
print(json.dumps(r2, indent=2, ensure_ascii=False))
