"""Publica feed + story do Post 3 — Molas Com Maciez Que Acolhe, Colchões e Cia (27/07/2026)."""
import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo, publish_story

FEED_URL = "https://i.imgur.com/UyfEzmY.png"
STORY_URL = "https://i.imgur.com/g7y1hfD.png"

CAPTION = (
    "Molas com maciez que acolhe. 🌬️\n\n"
    "O colchão de molas vem com camadas de conforto por cima, deixando a "
    "superfície mais macia sem perder a ventilação. Ótimo pra quem gosta de "
    "uma cama mais aconchegante e sente calor durante o sono.\n\n"
    "Espuma ou molas, a gente tem os dois. Vem na loja testar e decidir com o "
    "corpo, não só o preço.\n\n"
    "📍 Rua 20 Esq. Av. 13 — Centro — Barretos\n"
    "📞 (17) 3325-6039\n\n"
    "Pensou Colchão, Colchões e Cia!\n\n"
    "#ColchoesECia #ColchaoDeMolas #DormirBem #LojaDeColchao #Barretos #CamaBox"
)

acc = _get_account('colchoes_e_cia')

print("=== FEED (Post 3 - Molas Com Maciez Que Acolhe) ===")
r = publish_photo(acc, FEED_URL, CAPTION)
print(json.dumps(r, indent=2, ensure_ascii=False))

print("\n=== STORY (Post 3 - Molas Com Maciez Que Acolhe) ===")
r2 = publish_story(acc, STORY_URL)
print(json.dumps(r2, indent=2, ensure_ascii=False))
