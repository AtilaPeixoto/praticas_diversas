import requests
api_key = ''
endpoint = 'https://api.openai.com/v1/engines/davince/completions'

# definir o text de entrada e as configuraçoes do modelo
prompt = 'test'
model = 'text-davinci-001'

#corpo de solicitação

data = {
    'prompt': prompt,
    'model': model,
    'max_tokens': 100
}

# enva a solicitação a api
response = requests.post(endpoint, json=data, headers={
    'content-type': 'application/json',
    'authorization': f'bearer {api_key}'
    })

print(response.json())