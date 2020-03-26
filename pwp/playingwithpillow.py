from PIL import Image, ImageDraw, ImageFont


def main():
    img = Image.new('RGB', (400, 120), color = (0x11, 0xCC, 0xCC))
    mc_font = ImageFont.truetype("S:/Fonts/1 Minecraft-Regular.otf", 32)

    canvas = ImageDraw.Draw(img)

    canvas.text((10, 10), "Hello world!", font=mc_font, fill=(0xFF, 0xFF, 0x00))

    img.save('pil_text_font.png')


# This is needed, or else calling `python -m pwp` will mean that main() is called twice
if __name__ == "__main__":
    main()
