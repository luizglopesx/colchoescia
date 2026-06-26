import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo

BASE = "https://raw.githubusercontent.com/luizglopesx/colchoescia/main"
PASTA = "marketing/conteudo/sono-semana-2/post-tempo-trocar-2026-07"

CAPTION = (
    "Pergunta rápida: faz quanto tempo que você dorme no mesmo colchão?\n\n"
    "Se passou de 5 anos, provavelmente ele já não entrega o mesmo suporte de quando era novo. A espuma "
    "compacta, as molas perdem a firmeza, o conforto vai embora aos poucos — tão aos poucos que você "
    "nem percebe.\n\n"
    "Especialistas recomendam trocar o colchão a cada 5 a 7 anos. Mas a maioria das pessoas usa o mesmo "
    "por 10, 15 anos ou mais. E o corpo paga o preço: dor nas costas, noite mal dormida, cansaço de manhã.\n\n"
    "Não precisa ser assim. Vem na loja. A gente te ajuda a escolher o colchão certo — sem pressão, sem "
    "enrolação. Você sai de lá dormindo melhor na primeira noite.\n\n"
    "🛏️ Colchão de espuma e molas · Cama box · Cabeceira · Box baú\n"
    "📲 WhatsApp: (17) 3324-5765\n"
    "📞 Telefone: (17) 3325-6039\n"
    "📍 Rua 20 Esq. Av. 13 - Centro - Barretos\n\n"
    "#ColchoesECia #TrocarColchao #DormirBem #Colchao #SaudedoSono #CamaBox #LojaDeColchao #Barretos"
)

acc = _get_account('colchoes_e_cia')

print("=== FEED ===")
r = publish_photo(acc, f"{BASE}/{PASTA}/post.png", CAPTION)
print(json.dumps(r, indent=2, ensure_ascii=False))
