"""Publica feed + story no Instagram — Dia dos Pais Post 1 (04/08/2026 18h BRT).

O post no Facebook foi agendado direto via API (facebook_publisher.py
schedule_post), sem passar pelo cron do GitHub — o agendamento nativo do
Facebook funciona bem, diferente do Instagram (por isso o workaround aqui).
"""
import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo, publish_story

FEED_URL = "https://i.imgur.com/8bXCzSW.png"
STORY_URL = "https://i.imgur.com/1L7PIQ3.png"

CAPTION = (
    "Feliz Dia dos Pais!\n\n"
    "A gente sempre lembra do pai com um presente, um almoço, uma mensagem. Mas "
    "tem uma coisa que ele também merece todo dia: uma noite de sono tranquila.\n\n"
    "Colchão velho, cama desconfortável, corpo que já acostumou com a dor — "
    "às vezes o descanso dele é o primeiro a ficar de lado. Vale a pena olhar "
    "pra isso também.\n\n"
    "Passa na loja com ele. A gente ajuda a escolher o colchão certo, sem "
    "enrolação.\n\n"
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
