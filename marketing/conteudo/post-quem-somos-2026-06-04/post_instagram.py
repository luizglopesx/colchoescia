import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo, publish_story

BASE = "https://raw.githubusercontent.com/luizglopesx/colchoescia/main"
PASTA = "marketing/conteudo/post-quem-somos-2026-06-04/instagram"

CAPTION = (
    "A gente nao complica o que e simples.\n\n"
    "Somos uma loja de colchoes que fala direto com o cliente "
    "- sem enrolacao, sem promessa grande demais, sem preco escondido.\n\n"
    "Produto bom. Preco que cabe no bolso. Atendimento que respeita o seu tempo.\n\n"
    "E assim que a Colchoes e Cia funciona desde o comeco.\n\n"
    "Quer conhecer? Chama no WhatsApp ou passa na loja.\n\n"
    "#ColchoesECia #Colchao #CamaBox #Cabeceira #BoxBau #DormirBem #LojaDeColchao #PrecoJusto"
)

acc = _get_account('colchoes_e_cia')

print("=== FEED ===")
r = publish_photo(acc, f"{BASE}/{PASTA}/post.png", CAPTION)
print(json.dumps(r, indent=2, ensure_ascii=False))

print("\n=== STORY ===")
r = publish_story(acc, f"{BASE}/{PASTA}/story.png")
print(json.dumps(r, indent=2, ensure_ascii=False))
