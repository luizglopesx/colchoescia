import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo, publish_story

BASE = "https://raw.githubusercontent.com/luizglopesx/colchoescia/main"
PASTA = "marketing/conteudo/post-vale-investimento-2026-06"

CAPTION = (
    "\"Tá caro trocar de colchão.\"\n\n"
    "A gente entende. Mas pensa: você passa 1/3 da vida em cima dele.\n\n"
    "Um colchão novo é mais barato que remédio pra dor nas costas. Mais "
    "barato que fisioterapia. Mais barato que noite mal dormida acumulada.\n\n"
    "Na Colchões e Cia o preço é justo e o parcelamento cabe no teu "
    "orçamento. Trocar de colchão não precisa doer no bolso.\n\n"
    "Doeu nas costas. Isso sim. 😄\n\n"
    "🛏️ Colchão de espuma e molas · Cama box · Cabeceira · Box baú\n"
    "📲 Chama agora: (17) 3325-6039\n"
    "📍 Rua 20 Esq. Av. 13 - Centro - Barretos\n\n"
    "#ColchoesECia #Colchao #ValeOInvestimento #CamaBox #DormirBem "
    "#LojaDeColchao #PrecoJusto #Barretos"
)

acc = _get_account('colchoes_e_cia')

print("=== FEED ===")
r = publish_photo(acc, f"{BASE}/{PASTA}/post.png", CAPTION)
print(json.dumps(r, indent=2, ensure_ascii=False))

print("\n=== STORY ===")
r = publish_story(acc, f"{BASE}/{PASTA}/story.png")
print(json.dumps(r, indent=2, ensure_ascii=False))
