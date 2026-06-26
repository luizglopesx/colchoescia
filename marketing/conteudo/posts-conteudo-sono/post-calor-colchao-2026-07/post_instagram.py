import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo

BASE = "https://raw.githubusercontent.com/luizglopesx/colchoescia/main"
PASTA = "marketing/conteudo/posts-conteudo-sono/post-calor-colchao-2026-07"

CAPTION = (
    "Tá frio lá fora, mas você acorda suando. O lençol grudado, o travesseiro quente, aquela sensação "
    "de que dormiu numa estufa.\n\n"
    "Pode não ser o clima. Colchão velho retém calor. A espuma se compacta com o tempo e perde a "
    "respiração — o calor do corpo não dissipa mais. Resultado: você passa a noite suando, acorda "
    "desconfortável e nem associa ao colchão.\n\n"
    "Um colchão novo, com material que respira, muda isso na primeira noite.\n\n"
    "Se você acorda suando com frequência, passa na loja. A gente te mostra modelos que não viram "
    "forno durante a noite.\n\n"
    "🛏️ Colchão de espuma e molas · Cama box · Cabeceira · Box baú\n"
    "📲 WhatsApp: (17) 3324-5765\n"
    "📞 Telefone: (17) 3325-6039\n"
    "📍 Rua 20 Esq. Av. 13 - Centro - Barretos\n\n"
    "#ColchoesECia #CalorNoColchao #DormirBem #Colchao #SaudedoSono #CamaBox #LojaDeColchao #Barretos"
)

acc = _get_account('colchoes_e_cia')

print("=== FEED ===")
r = publish_photo(acc, f"{BASE}/{PASTA}/post.png", CAPTION)
print(json.dumps(r, indent=2, ensure_ascii=False))
