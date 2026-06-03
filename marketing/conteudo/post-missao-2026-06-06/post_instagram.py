import sys, json
sys.path.insert(0, '.claude/skills/int-instagram/scripts')
from instagram_publisher import _get_account, publish_photo, publish_story

BASE = "https://raw.githubusercontent.com/luizglopesx/colchoescia/main"
PASTA = "marketing/conteudo/post-missao-2026-06-06/instagram"

CAPTION = (
    "Dormir mal nao e normal. E sinal de que algo precisa mudar.\n\n"
    "A gente acredita que todo mundo merece uma cama boa "
    "- nao so quem tem dinheiro sobrando.\n\n"
    "E por isso que a Colchoes e Cia existe: pra trazer qualidade e preco justo "
    "pra quem realmente precisa dormir bem.\n\n"
    "Passa la, a gente explica sem pressa. Voce decide na hora certa.\n\n"
    "Chama no WhatsApp ou vem direto na loja.\n\n"
    "#ColchoesECia #DormirBem #Colchao #CamaBox #QualidadeDeVida #DescansoDeVerdade #PrecoJusto"
)

acc = _get_account('colchoes_e_cia')

print("=== FEED ===")
r = publish_photo(acc, f"{BASE}/{PASTA}/post.png", CAPTION)
print(json.dumps(r, indent=2, ensure_ascii=False))

print("\n=== STORY ===")
r = publish_story(acc, f"{BASE}/{PASTA}/story.png")
print(json.dumps(r, indent=2, ensure_ascii=False))
