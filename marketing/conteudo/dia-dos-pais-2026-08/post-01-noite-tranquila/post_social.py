"""Publica feed + story no Instagram e feed no Facebook — Dia dos Pais Post 1 (04/08/2026 18h BRT)."""
import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account as _ig_account, publish_photo, publish_story
from facebook_publisher import _get_account as _fb_account, publish_post

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

ig = _ig_account('colchoes_e_cia')
fb = _fb_account('colchoes_e_cia')

print("=== INSTAGRAM FEED ===")
r1 = publish_photo(ig, FEED_URL, CAPTION)
print(json.dumps(r1, indent=2, ensure_ascii=False))

print("\n=== INSTAGRAM STORY ===")
r2 = publish_story(ig, STORY_URL)
print(json.dumps(r2, indent=2, ensure_ascii=False))

print("\n=== FACEBOOK FEED ===")
r3 = publish_post(fb, CAPTION, FEED_URL)
print(json.dumps(r3, indent=2, ensure_ascii=False))
