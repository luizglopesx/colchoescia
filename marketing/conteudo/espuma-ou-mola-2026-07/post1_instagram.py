"""Publica feed + story do Post 1 — Espuma ou Mola? Colchões e Cia (22/07/2026)."""
import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo, publish_story

FEED_URL = "https://i.imgur.com/uVkiaBc.png"
STORY_URL = "https://i.imgur.com/Yag06qt.png"

CAPTION = (
    "Espuma ou molas? A dúvida que todo mundo tem antes de comprar. 🤔\n\n"
    "Cada colchão tem um jeito diferente de sustentar o corpo. Não existe um "
    "melhor pra todo mundo — existe o melhor pro seu jeito de dormir.\n\n"
    "Nos próximos posts a gente mostra a diferença entre os dois. E se quiser "
    "sentir na pele, é só vir na loja e testar.\n\n"
    "📍 Rua 20 Esq. Av. 13 — Centro — Barretos\n"
    "📞 (17) 3325-6039\n\n"
    "Pensou Colchão, Colchões e Cia!\n\n"
    "#ColchoesECia #ColchaoDeEspuma #ColchaoDeMolas #DormirBem #LojaDeColchao #Barretos #CamaBox"
)

acc = _get_account('colchoes_e_cia')

print("=== FEED (Post 1 - Espuma ou Molas?) ===")
r = publish_photo(acc, FEED_URL, CAPTION)
print(json.dumps(r, indent=2, ensure_ascii=False))

print("\n=== STORY (Post 1 - Espuma ou Molas?) ===")
r2 = publish_story(acc, STORY_URL)
print(json.dumps(r2, indent=2, ensure_ascii=False))
