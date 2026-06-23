import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo

BASE = "https://raw.githubusercontent.com/luizglopesx/colchoescia/main"
PASTA = "marketing/conteudo/posts-conteudo-sono/post-casais-colchao-2026-06"

CAPTION = (
    "Você ri, mas já passou por isso.\n\n"
    "Um quer mole, o outro quer firme. Um esquenta à noite, o outro sente frio. Um mexe muito "
    "e acorda o outro. A cama vira campo de batalha — e de manhã os dois acordam mal.\n\n"
    "A boa notícia: isso tem solução.\n\n"
    "A gente tem colchões que equilibram os dois lados, e pode te ajudar a escolher o tamanho "
    "e o modelo certo pro casal. Sem compromisso, sem enrolação.\n\n"
    "Vem testar. Às vezes uma tarde na loja resolve anos de noite mal dormida.\n\n"
    "🛏️ Colchão de espuma e molas · Cama box · Cabeceira · Box baú\n"
    "📲 WhatsApp: (17) 3324-5765\n"
    "📞 Telefone: (17) 3325-6039\n"
    "📍 Rua 20 Esq. Av. 13 - Centro - Barretos\n\n"
    "#ColchoesECia #ColchaoDeCasal #DormirBem #Colchao #CamaBox #LojaDeColchao #Barretos"
)

acc = _get_account('colchoes_e_cia')

print("=== FEED ===")
r = publish_photo(acc, f"{BASE}/{PASTA}/post.png", CAPTION)
print(json.dumps(r, indent=2, ensure_ascii=False))
