"""Publica feed + story do Post 3 — Facilidade de Pagamento Colchões e Cia (03/08/2026)."""
import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo, publish_story

FEED_URL = "https://i.imgur.com/WkmkmEU.png"
STORY_URL = "https://i.imgur.com/bj07aWF.png"

CAPTION = (
    "Do jeito que cabe no seu mês. 💳\n\n"
    "Parcelamento sem juros, simples do começo ao fim.\n\n"
    "Passa na loja ou liga pra gente. A gente encontra o parcelamento certo pro seu bolso.\n\n"
    "📍 Rua 20 Esq. Av. 13 — Centro — Barretos\n"
    "📞 (17) 3325-6039\n\n"
    "Pensou Colchão, Colchões e Cia!\n\n"
    "#ColchoesECia #Parcelamento #SemJuros #Colchao #LojaDeColchao #Barretos #FacilidadeDePagamento #ColchaoBom"
)

acc = _get_account('colchoes_e_cia')

print("=== FEED (Post 3 - Do Jeito Que Cabe No Seu Mês) ===")
r = publish_photo(acc, FEED_URL, CAPTION)
print(json.dumps(r, indent=2, ensure_ascii=False))

print("\n=== STORY (Post 3 - Do Jeito Que Cabe No Seu Mês) ===")
r2 = publish_story(acc, STORY_URL)
print(json.dumps(r2, indent=2, ensure_ascii=False))
