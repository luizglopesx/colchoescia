"""Publica feed + story — Colchão D33 Light Casal (Festa do Peão, 05/08/2026 12h15 BRT)."""
import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo, publish_story

FEED_URL = "https://i.imgur.com/8c20roU.png"
STORY_URL = "https://i.imgur.com/MJdQExz.png"

CAPTION = (
    "Segura, peão! 🤠\n\n"
    "Vai receber visita durante a Festa do Peão? Prepare o quarto com um colchão que aguenta o tranco.\n\n"
    "Colchão D33 Light casal por R$ 1.190 em até 12x sem juros. Conforto de verdade pra família e amigos "
    "dormirem bem em Barretos, de 20 a 30 de agosto.\n\n"
    "Passe na loja ou ligue e fale com um vendedor:\n\n"
    "📍 Rua 20 esq. Av. 13 — Centro — Barretos\n"
    "📞 (17) 3325-6039\n\n"
    "Pensou Colchão, Colchões e Cia!\n\n"
    "#ColchoesECia #FestaDoPeao #Barretos #SeguraPeao #Colchao #QuartoDeVisitas #CasaPronta #DormirBem"
)

acc = _get_account('colchoes_e_cia')

print("=== FEED (D33 Light Casal) ===")
r = publish_photo(acc, FEED_URL, CAPTION)
print(json.dumps(r, indent=2, ensure_ascii=False))

print("\n=== STORY (D33 Light Casal) ===")
r2 = publish_story(acc, STORY_URL)
print(json.dumps(r2, indent=2, ensure_ascii=False))
