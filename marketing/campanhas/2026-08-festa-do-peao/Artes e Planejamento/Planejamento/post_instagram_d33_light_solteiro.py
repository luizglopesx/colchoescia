"""Publica feed + story — Colchão D33 Light Solteiro (Festa do Peão, 03/08/2026 18h BRT)."""
import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo, publish_story

FEED_URL = "https://i.imgur.com/0BiDHFY.png"
STORY_URL = "https://i.imgur.com/hU28KWF.png"

CAPTION = (
    "Segura, peão! 🤠\n\n"
    "Visita não dorme no improviso — nem quando é só uma cama de solteiro.\n\n"
    "Colchão D33 Light solteiro por R$ 790 em até 12x sem juros. Ideal pra deixar o quarto de visitas "
    "pronto antes da Festa do Peão, de 20 a 30 de agosto em Barretos.\n\n"
    "Passe na loja ou ligue e fale com um vendedor:\n\n"
    "📍 Rua 20 esq. Av. 13 — Centro — Barretos\n"
    "📞 (17) 3325-6039\n\n"
    "Pensou Colchão, Colchões e Cia!\n\n"
    "#ColchoesECia #FestaDoPeao #Barretos #SeguraPeao #Colchao #QuartoDeVisitas #CasaPronta #DormirBem"
)

acc = _get_account('colchoes_e_cia')

print("=== FEED (D33 Light Solteiro) ===")
r = publish_photo(acc, FEED_URL, CAPTION)
print(json.dumps(r, indent=2, ensure_ascii=False))

print("\n=== STORY (D33 Light Solteiro) ===")
r2 = publish_story(acc, STORY_URL)
print(json.dumps(r2, indent=2, ensure_ascii=False))
