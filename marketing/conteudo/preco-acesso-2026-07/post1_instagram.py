"""Publica feed + story do Post 1 — Preço e Acesso Colchões e Cia (15/07/2026)."""
import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo, publish_story

FEED_URL = "https://i.imgur.com/0HM4gBa.png"
STORY_URL = "https://i.imgur.com/3X0P2gi.png"

CAPTION = (
    "Colchão bom não precisa ser caro. 💰\n\n"
    "Qualidade de verdade com preço que cabe na sua realidade. Sem enrolação, "
    "sem promessa vazia — só colchão bom pra você dormir melhor.\n\n"
    "Passa na loja ou chama no WhatsApp. A gente te mostra o preço na hora.\n\n"
    "📍 Rua 20 Esq. Av. 13 — Centro — Barretos\n"
    "📱 WhatsApp: (17) 3325-6039\n\n"
    "Pensou Colchão, Colchões e Cia!\n\n"
    "#ColchoesECia #PrecoJusto #Colchao #LojaDeColchao #Barretos #Oferta #ColchaoBom"
)

acc = _get_account('colchoes_e_cia')

print("=== FEED (Post 1 - Colchão Bom Não Precisa Ser Caro) ===")
r = publish_photo(acc, FEED_URL, CAPTION)
print(json.dumps(r, indent=2, ensure_ascii=False))

print("\n=== STORY (Post 1 - Colchão Bom Não Precisa Ser Caro) ===")
r2 = publish_story(acc, STORY_URL)
print(json.dumps(r2, indent=2, ensure_ascii=False))
