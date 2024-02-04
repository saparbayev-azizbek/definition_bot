import requests

def diction(word):
    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'

    response = requests.get(url)
    res = response.json()
    if type(res) == dict:
        return False
    else:
        output = {}
        meanings = res[0]['meanings'][0]['definitions']
        size = len(meanings)
        definitions1 = []
        for i in range(0, size):
            definitions1.append(f"👉 {meanings[i]['definition']}")
        output["definitions"] = '\n'.join(definitions1)
        return output
