"""Publica feed + story — Cama Box Livorno Casal (Festa do Peão, 07/08/2026 08h30 BRT)."""
import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo, publish_story

FEED_URL = "https://i.imgur.com/nqWpB0j.png"
STORY_URL = "https://i.imgur.com/SI9xk6A.png"

CAPTION = (
    "Segura, peão! 🤠\n\n"
    "Quarto de visita capricho começa com cama de verdade. Cama Box Livorno casal por R$ 2.190 em até "
    "12x sem juros.\n\n"
    "Barretos recebe muita gente na Festa do Peão, de 20 a 30 de agosto. Deixe o quarto pronto antes que "
    "a visita chegue.\n\n"
    "Passe na loja ou ligue e fale com um vendedor:\n\n"
    "📍 Rua 20 esq. Av. 13 — Centro — Barretos\n"
    "📞 (17) 3325-6039\n\n"
    "Pensou Colchão, Colchões e Cia!\n\n"
    "#ColchoesECia #FestaDoPeao #Barretos #SeguraPeao #CamaBox #QuartoDeVisitas #CasaPronta #DormirBem"
)

acc = _get_account('colchoes_e_cia')

print("=== FEED (Cama Box Livorno Casal) ===")
r = publish_photo(acc, FEED_URL, CAPTION)
print(json.dumps(r, indent=2, ensure_ascii=False))

print("\n=== STORY (Cama Box Livorno Casal) ===")
r2 = publish_story(acc, STORY_URL)
print(json.dumps(r2, indent=2, ensure_ascii=False))
