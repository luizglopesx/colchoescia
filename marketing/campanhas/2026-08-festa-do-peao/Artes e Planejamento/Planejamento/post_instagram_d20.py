"""Publica feed + story — Colchão D20 ComfortPedic (Festa do Peão, 05/08/2026 08h30 BRT)."""
import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo, publish_story

FEED_URL = "https://i.imgur.com/GAoj3be.png"
STORY_URL = "https://i.imgur.com/1skdEi7.png"

CAPTION = (
    "Segura, peão! 🤠\n\n"
    "Vai receber família ou amigos durante a Festa do Peão? Então prepare o quarto antes.\n\n"
    "Colchão D20 ComfortPedic por R$ 299 em até 12x sem juros. Barretos vai receber muita gente de 20 a 30 "
    "de agosto, e visita em casa merece colchão de verdade — nada de deixar pra última hora e dormir no improviso.\n\n"
    "Passe na loja ou ligue e fale com um vendedor:\n\n"
    "📍 Rua 20 esq. Av. 13 — Centro — Barretos\n"
    "📞 (17) 3325-6039\n\n"
    "Pensou Colchão, Colchões e Cia!\n\n"
    "#ColchoesECia #FestaDoPeao #Barretos #SeguraPeao #Colchao #QuartoDeVisitas #CasaPronta #DormirBem"
)

acc = _get_account('colchoes_e_cia')

print("=== FEED (D20 ComfortPedic) ===")
r = publish_photo(acc, FEED_URL, CAPTION)
print(json.dumps(r, indent=2, ensure_ascii=False))

print("\n=== STORY (D20 ComfortPedic) ===")
r2 = publish_story(acc, STORY_URL)
print(json.dumps(r2, indent=2, ensure_ascii=False))
