import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo

BASE = "https://raw.githubusercontent.com/luizglopesx/colchoescia/main"
PASTA = "marketing/conteudo/posts-conteudo-sono/post-colchao-afundando-2026-07"

CAPTION = (
    "Você olha pro colchão e ele tá afundado no meio. Aquele buraco que vai ficando maior a cada mês.\n\n"
    "O problema não é só estético. Quando o colchão perde o suporte, sua coluna desalinha durante a noite "
    "inteira. O corpo tenta compensar — e você acorda com dor nas costas, torcicolo, aquela sensação de "
    "que dormiu torto.\n\n"
    "A gente acostuma com o desconforto. Mas o corpo não.\n\n"
    "Se o colchão já tá marcado, com depressão no meio ou nas bordas, talvez seja hora de trocar. Vem na "
    "loja. A gente te mostra a diferença de deitar num colchão que ainda tá inteiro de verdade.\n\n"
    "🛏️ Colchão de espuma e molas · Cama box · Cabeceira · Box baú\n"
    "📲 WhatsApp: (17) 3324-5765\n"
    "📞 Telefone: (17) 3325-6039\n"
    "📍 Rua 20 Esq. Av. 13 - Centro - Barretos\n\n"
    "#ColchoesECia #ColchaoAfundado #DormirBem #Colchao #SaudedoSono #CamaBox #LojaDeColchao #Barretos"
)

acc = _get_account('colchoes_e_cia')

print("=== FEED ===")
r = publish_photo(acc, f"{BASE}/{PASTA}/post.png", CAPTION)
print(json.dumps(r, indent=2, ensure_ascii=False))
