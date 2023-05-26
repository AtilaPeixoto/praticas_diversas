import openai

openai.api_key = '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'
f = 2
response = openai.Image.create(
    prompt ='',
    n=f,
    size ='1024x1024'
)

for i in range(0, f):
    image_url = response['data'][i]['url']
    print(f'url da imagem gerada: {image_url}')
   
