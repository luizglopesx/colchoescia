import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo

BASE = "https://raw.githubusercontent.com/luizglopesx/colchoescia/main"
PASTA = "marketing/conteudo/posts-conteudo-sono/post-dor-costas-2026-06"

CAPTION = (
    "Acorda todo dia com dor nas costas e acha que é normal?\n\n"
    "Não é.\n\n"
    "Dor nas costas de manhã é sinal de que o colchão perdeu o suporte. Ele não sustenta mais "
    "a coluna do jeito certo durante a noite — e o corpo paga o preço toda manhã.\n\n"
    "O problema é que a gente acostuma. A dor vira rotina. E você vai levando, sem associar ao colchão.\n\n"
    "Se isso tá acontecendo com você, passa na loja. A gente te mostra a diferença de deitar "
    "num colchão que ainda funciona de verdade.\n\n"
    "🛏️ Colchão de espuma e molas · Cama box · Cabeceira · Box baú\n"
    "📲 WhatsApp: (17) 3324-5765\n"
    "📞 Telefone: (17) 3325-6039\n"
    "📍 Rua 20 Esq. Av. 13 - Centro - Barretos\n\n"
    "#ColchoesECia #DorNasCostas #DormirBem #Colchao #SaudedoSono #CamaBox #LojaDeColchao #Barretos"
)

acc = _get_account('colchoes_e_cia')

print("=== FEED ===")
r = publish_photo(acc, f"{BASE}/{PASTA}/post.png", CAPTION)
print(json.dumps(r, indent=2, ensure_ascii=False))
