import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo

BASE = "https://raw.githubusercontent.com/luizglopesx/colchoescia/main"
PASTA = "marketing/conteudo/posts-conteudo-sono/post-acorda-noite-2026-06"

CAPTION = (
    "1:39 da manhã. Você acorda sem motivo aparente.\n\n"
    "Tenta dormir de novo, vira pro outro lado, não consegue. De manhã acorda destruído.\n\n"
    "Pode não ser insônia. Colchão velho retém calor, perde o suporte em pontos específicos "
    "e faz o corpo compensar a posição durante a noite — aí você acorda.\n\n"
    "Não é frescura. É o colchão te impedindo de dormir direito.\n\n"
    "Se isso acontece com frequência, vale a pena vir até a loja. A gente te explica o que "
    "pode estar causando e te mostra as opções.\n\n"
    "🛏️ Colchão de espuma e molas · Cama box · Cabeceira · Box baú\n"
    "📲 WhatsApp: (17) 3324-5765\n"
    "📞 Telefone: (17) 3325-6039\n"
    "📍 Rua 20 Esq. Av. 13 - Centro - Barretos\n\n"
    "#ColchoesECia #Insonia #DormirBem #Colchao #SaudedoSono #LojaDeColchao #Barretos"
)

acc = _get_account('colchoes_e_cia')

print("=== FEED ===")
r = publish_photo(acc, f"{BASE}/{PASTA}/post.png", CAPTION)
print(json.dumps(r, indent=2, ensure_ascii=False))
