import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo, publish_story

BASE = "https://raw.githubusercontent.com/luizglopesx/colchoescia/main"
PASTA = "marketing/conteudo/post-diferenciais-2026-06-07/instagram"

CAPTION = (
    "Preco justo nao e sorte - e uma escolha que a gente faz todo dia.\n\n"
    "Na Colchoes e Cia voce nao precisa ficar adivinhando quanto vai custar. "
    "A gente mostra o preco, explica o produto e deixa voce decidir sem pressao.\n\n"
    "Colchao de espuma, colchao de molas, cama box, cabeceira, box bau. "
    "Tudo que o seu quarto precisa, num lugar so.\n\n"
    "Vem conhecer a loja ou chama no WhatsApp - sem compromisso.\n\n"
    "#ColchoesECia #Colchao #CamaBox #Cabeceira #BoxBau #PrecoJusto #LojaDeColchao #DormirBem"
)

acc = _get_account('colchoes_e_cia')

print("=== FEED ===")
r = publish_photo(acc, f"{BASE}/{PASTA}/post.png", CAPTION)
print(json.dumps(r, indent=2, ensure_ascii=False))

print("\n=== STORY ===")
r = publish_story(acc, f"{BASE}/{PASTA}/story.png")
print(json.dumps(r, indent=2, ensure_ascii=False))
