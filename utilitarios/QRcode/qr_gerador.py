import qrcode

img = qrcode.make('https://linktr.ee/atilapeixoto') # link para geração do qrcode
type(img)  # qrcode.image.pil.PilImage
img.save('atilapeixoto.png')