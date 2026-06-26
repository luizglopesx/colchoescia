import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo

BASE = "https://raw.githubusercontent.com/luizglopesx/colchoescia/main"
PASTA = "marketing/conteudo/sono-semana-2/post-alergia-colchao-2026-07"

CAPTION = (
    "Você acorda e já começa: espirro atrás de espirro. Nariz trancado, coceira no céu da boca, coceira "
    "nos olhos. E acha que é rinite, poeira no quarto, tempo seco.\n\n"
    "Pode ser. Mas também pode ser o colchão.\n\n"
    "Colchão velho acumula ácaros, poeira, resíduos de pele, umidade. Você passa 8 horas por noite com "
    "o rosto ali, respirando isso. Com o tempo, vira gatilho de alergia, rinite alérgica e até dormência "
    "no rosto, se a alergia atacar os seios da face.\n\n"
    "A gente não pensa nisso — mas o colchão é o móvel que mais acumula sujeira invisível. E se ele tem "
    "mais de 5 anos, a chance de estar carregado de ácaros é enorme.\n\n"
    "O mais chato? É que você só descobre a diferença de dormir num colchão limpo e novo quando "
    "experimenta. Vem na loja. A gente te mostra.\n\n"
    "🛏️ Colchão de espuma e molas · Cama box · Cabeceira · Box baú\n"
    "📲 WhatsApp: (17) 3324-5765\n"
    "📞 Telefone: (17) 3325-6039\n"
    "📍 Rua 20 Esq. Av. 13 - Centro - Barretos\n\n"
    "#ColchoesECia #Alergia #Rinite #DormirBem #Colchao #SaudedoSono #CamaBox #LojaDeColchao #Barretos"
)

acc = _get_account('colchoes_e_cia')

print("=== FEED ===")
r = publish_photo(acc, f"{BASE}/{PASTA}/post.png", CAPTION)
print(json.dumps(r, indent=2, ensure_ascii=False))
