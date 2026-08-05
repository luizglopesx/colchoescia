"""Publica feed + story no Instagram — Promoção Festa do Peão Post 3 (14/08/2026 11h BRT)."""
import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo, publish_story

FEED_URL = "https://i.imgur.com/Pq84E86.png"
STORY_URL = "https://i.imgur.com/sPU6x3L.png"

CAPTION = (
    "Segura, peão! 🤠\n\n"
    "Últimos dias da promoção Festa do Peão na Colchões e Cia. Depois que a festa "
    "acaba, o preço também volta ao normal.\n\n"
    "Peças selecionadas com condições especiais só até 30 de agosto.\n\n"
    "Passe na loja ou ligue e fale com um vendedor:\n\n"
    "📍 Rua 20 esq. Av. 13 — Centro — Barretos\n"
    "📞 (17) 3325-6039\n\n"
    "Pensou Colchão, Colchões e Cia!\n\n"
    "#ColchoesECia #FestaDoPeao #Barretos #SeguraPeao #Promocao #UltimosDias"
)

acc = _get_account('colchoes_e_cia')

print("=== INSTAGRAM FEED ===")
r1 = publish_photo(acc, FEED_URL, CAPTION)
print(json.dumps(r1, indent=2, ensure_ascii=False))

print("\n=== INSTAGRAM STORY ===")
r2 = publish_story(acc, STORY_URL)
print(json.dumps(r2, indent=2, ensure_ascii=False))
