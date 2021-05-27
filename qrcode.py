import qrcode

img = qrcode.make("https://github.com/RizkiAsmoro")
img.save("github.jpg")