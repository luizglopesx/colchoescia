import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo, publish_story

BASE = "https://raw.githubusercontent.com/luizglopesx/colchoescia/main"
PASTA = "marketing/conteudo/post-sinais-trocar-colchao-2026-06"

CAPTION = (
    "Teu colchão não vai levantar a mão e pedir pra sair. Mas ele mostra.\n\n"
    "🛏️ Afundou no meio e você acorda no buraco\n"
    "🛏️ As molas fazem barulho cada vez que você vira\n"
    "🛏️ Acorda mais cansado do que foi dormir\n"
    "🛏️ Já passou dos 7, 8 anos de uso\n\n"
    "Se bateu 2 ou mais, tá na hora de vir conversar com a gente.\n\n"
    "Na Colchões e Cia você escolhe com calma, prova o colchão na loja e só "
    "leva quando tiver certeza. Sem pressa, sem pressão.\n\n"
    "🛏️ Colchão de espuma e molas · Cama box · Cabeceira · Box baú\n"
    "📲 Chama agora: (17) 3325-6039\n"
    "📍 Rua 20 Esq. Av. 13 - Centro - Barretos\n\n"
    "#ColchoesECia #Colchao #HoraDeTrocar #CamaBox #DormirBem "
    "#LojaDeColchao #PrecoJusto #Barretos"
)

acc = _get_account('colchoes_e_cia')

print("=== FEED ===")
r = publish_photo(acc, f"{BASE}/{PASTA}/post.png", CAPTION)
print(json.dumps(r, indent=2, ensure_ascii=False))

print("\n=== STORY ===")
r = publish_story(acc, f"{BASE}/{PASTA}/story.png")
print(json.dumps(r, indent=2, ensure_ascii=False))
