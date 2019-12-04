from PIL import Image, ImageDraw, ImageFont

CONVIDADOS = ["Karla", "Erik", "Oliver", "Guido"]

LEFT_BORDER = 100

font1 = ImageFont.truetype("./font1.ttf", size=35)
font2 = ImageFont.truetype("./font2.ttf", size=35)

for convidado in CONVIDADOS:
    imagem = Image.open("./template.png").convert("RGBA")

    lapis = ImageDraw.Draw(imagem)

    lapis.text((125, 100), text=f"Olá {convidado}", fill="#000", font=font1)

    lapis.line((LEFT_BORDER, 145, 398, 145), fill="#ccc", width=5)

    lapis.text(
        (LEFT_BORDER, 160),
        text="Venha ao meu aniversário",
        fill="#000",
        font=font2,
    )

    lapis.text(
        (LEFT_BORDER, 200), text="Dia 31/03/2020", fill="#000", font=font2
    )

    lapis.text((LEFT_BORDER, 280), text="Abraços!", fill="#000", font=font2)

    imagem.save(f"./convite_{convidado}.png")
