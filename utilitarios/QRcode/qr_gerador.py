import qrcode

img = qrcode.make('51985036999') # link para geração do qrcode
type(img)  # qrcode.image.pil.PilImage
img.save('atilapeixotonumero.png')

