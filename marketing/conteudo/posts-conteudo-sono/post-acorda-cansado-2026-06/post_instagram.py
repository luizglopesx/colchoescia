import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo

BASE = "https://raw.githubusercontent.com/luizglopesx/colchoescia/main"
PASTA = "marketing/conteudo/posts-conteudo-sono/post-acorda-cansado-2026-06"

CAPTION = (
    "Você deita cedo, dorme as horas certas — e acorda do mesmo jeito: cansado.\n\n"
    "Pode não ser a noite que foi curta. Na maioria das vezes, o problema está onde você dorme.\n\n"
    "Colchão velho perde o suporte sem avisar. O corpo acostuma com o desconforto. Você nem "
    "percebe que tá dormindo mal — até trocar e sentir a diferença na primeira noite.\n\n"
    "Se você acorda com dor nas costas, sensação de noite mal dormida ou levanta cansado todo "
    "dia: talvez seja hora de olhar pro colchão.\n\n"
    "Vem na loja. A gente te ajuda a escolher sem enrolação.\n\n"
    "🛏️ Colchão de espuma e molas · Cama box · Cabeceira · Box baú\n"
    "📲 WhatsApp: (17) 3324-5765\n"
    "📞 Telefone: (17) 3325-6039\n"
    "📍 Rua 20 Esq. Av. 13 - Centro - Barretos\n\n"
    "#ColchoesECia #DormirBem #Colchao #SaudedoSono #AcordaCansado #CamaBox #LojaDeColchao #Barretos"
)

acc = _get_account('colchoes_e_cia')

print("=== FEED ===")
r = publish_photo(acc, f"{BASE}/{PASTA}/post.png", CAPTION)
print(json.dumps(r, indent=2, ensure_ascii=False))
