"""Publica feed + story do Post 3 — Preço e Acesso Colchões e Cia (20/07/2026)."""
import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo, publish_story

FEED_URL = "https://i.imgur.com/kKUP1O4.png"
STORY_URL = "https://i.imgur.com/9GDa2uF.png"

CAPTION = (
    "Colchão pra cada bolso. 🛏️\n\n"
    "Tem opção boa em toda faixa de preço — do simples ao completo. "
    "Ninguém sai daqui sem solução pra dormir melhor.\n\n"
    "Passa na loja ou liga pra gente. A gente acha o colchão certo pro seu bolso.\n\n"
    "📍 Rua 20 Esq. Av. 13 — Centro — Barretos\n"
    "📞 (17) 3325-6039\n\n"
    "Pensou Colchão, Colchões e Cia!\n\n"
    "#ColchoesECia #ColchaoPraTodoMundo #Colchao #LojaDeColchao #Barretos #Oferta #PrecoAcessivel"
)

acc = _get_account('colchoes_e_cia')

print("=== FEED (Post 3 - Colchão Pra Cada Bolso) ===")
r = publish_photo(acc, FEED_URL, CAPTION)
print(json.dumps(r, indent=2, ensure_ascii=False))

print("\n=== STORY (Post 3 - Colchão Pra Cada Bolso) ===")
r2 = publish_story(acc, STORY_URL)
print(json.dumps(r2, indent=2, ensure_ascii=False))
