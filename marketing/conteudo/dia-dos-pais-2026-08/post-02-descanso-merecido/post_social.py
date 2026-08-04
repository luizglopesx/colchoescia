"""Publica feed + story no Instagram — Dia dos Pais Post 2 (06/08/2026 18h BRT).

O post no Facebook foi agendado direto via API (facebook_publisher.py
schedule_post), sem passar pelo cron do GitHub — o agendamento nativo do
Facebook funciona bem, diferente do Instagram (por isso o workaround aqui).
"""
import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo, publish_story

FEED_URL = "https://i.imgur.com/4JqNulK.png"
STORY_URL = "https://i.imgur.com/FTemwU7.jpeg"

CAPTION = (
    "Feliz Dia dos Pais pra todo pai que cuida, resolve e não para.\n\n"
    "Ele cuida da casa, da família, do trabalho. Que tal, nesse dia, cuidar "
    "um pouco do descanso dele?\n\n"
    "Um colchão bom não é luxo — é o que faz ele acordar disposto pra dar "
    "conta de tudo de novo.\n\n"
    "Vem na Colchões e Cia escolher o colchão ideal pra ele.\n\n"
    "🛏️ Colchão de espuma e molas · Cama box · Cabeceira · Box baú\n"
    "📞 Telefone: (17) 3325-6039\n"
    "📍 Rua 20 Esq. Av. 13 - Centro - Barretos\n\n"
    "#DiaDosPais #ColchoesECia #DormirBem #Colchao #SaudedoSono #LojaDeColchao #Barretos"
)

acc = _get_account('colchoes_e_cia')

print("=== INSTAGRAM FEED ===")
r1 = publish_photo(acc, FEED_URL, CAPTION)
print(json.dumps(r1, indent=2, ensure_ascii=False))

print("\n=== INSTAGRAM STORY ===")
r2 = publish_story(acc, STORY_URL)
print(json.dumps(r2, indent=2, ensure_ascii=False))
