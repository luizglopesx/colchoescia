import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo, publish_story

BASE = "https://raw.githubusercontent.com/luizglopesx/colchoescia/main"
PASTA = "marketing/conteudo/post-vida-util-colchao-2026-06"

CAPTION = (
    "Colchão não dura pra sempre. E tudo bem — faz parte.\n\n"
    "Um colchão bom dura em média de 7 a 10 anos. Depois disso, a espuma "
    "perde a firmeza, as molas cansam, o suporte vai embora. E você nem "
    "percebe que tá dormindo mal — o corpo acostuma.\n\n"
    "Aí quando troca, a diferença é absurda.\n\n"
    "Vem na loja, experimenta um colchão novo. Só de deitar ali você já "
    "sente o que tava perdendo.\n\n"
    "🛏️ Colchão de espuma e molas · Cama box · Cabeceira · Box baú\n"
    "📲 Chama agora: (17) 3325-6039\n"
    "📍 Rua 20 Esq. Av. 13 - Centro - Barretos\n\n"
    "#ColchoesECia #Colchao #VidaUtilDoColchao #CamaBox #DormirBem "
    "#LojaDeColchao #PrecoJusto #Barretos"
)

acc = _get_account('colchoes_e_cia')

print("=== FEED ===")
r = publish_photo(acc, f"{BASE}/{PASTA}/post.png", CAPTION)
print(json.dumps(r, indent=2, ensure_ascii=False))

print("\n=== STORY ===")
r = publish_story(acc, f"{BASE}/{PASTA}/story.png")
print(json.dumps(r, indent=2, ensure_ascii=False))
