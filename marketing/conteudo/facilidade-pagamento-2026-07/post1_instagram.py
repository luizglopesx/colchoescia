"""Publica feed + story do Post 1 — Facilidade de Pagamento Colchões e Cia (29/07/2026)."""
import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo, publish_story

FEED_URL = "https://i.imgur.com/xgKFs3k.png"
STORY_URL = "https://i.imgur.com/dwZtTFF.png"

CAPTION = (
    "Não espera pra dormir bem. 🛌\n\n"
    "Comprou hoje, já pode trocar de colchão — em até 12x sem juros, no seu ritmo.\n\n"
    "Passa na loja ou liga pra gente. A gente monta o parcelamento certo pra você.\n\n"
    "📍 Rua 20 Esq. Av. 13 — Centro — Barretos\n"
    "📞 (17) 3325-6039\n\n"
    "Pensou Colchão, Colchões e Cia!\n\n"
    "#ColchoesECia #Parcelamento #SemJuros #Colchao #LojaDeColchao #Barretos #DormirBem #ColchaoBom"
)

acc = _get_account('colchoes_e_cia')

print("=== FEED (Post 1 - Não Espera Pra Dormir Bem) ===")
r = publish_photo(acc, FEED_URL, CAPTION)
print(json.dumps(r, indent=2, ensure_ascii=False))

print("\n=== STORY (Post 1 - Não Espera Pra Dormir Bem) ===")
r2 = publish_story(acc, STORY_URL)
print(json.dumps(r2, indent=2, ensure_ascii=False))
