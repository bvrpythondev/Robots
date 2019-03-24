import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, KeywordsOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-11-16',
    iam_apikey='OIjKPBv1Cs8FajYDS10QUqhMKldef8stxrI4lfeHp86g',
    url='https://gateway.watsonplatform.net/natural-language-understanding/api'
)



response = natural_language_understanding.analyze(
    text="Michael Joseph Jackson foi um cantor, compositor, dançarino, produtor, empresário, arranjador vocal, filantropo, pacifista e ativista estadunidense.Segundo a revista Rolling Stone, faturou em vida cerca de sete bilhões de dólares, tornando-se o artista mais rico da história.Um ano após sua morte ainda faturou cerca de um bilhão de dólares.Começou a cantar e a dançar aos cinco anos de idade, iniciando-se na carreira profissional aos onze anos como vocalista do grupo Jackson 5",
    features=Features(keywords=KeywordsOptions(sentiment=False,emotion=False,limit=3))).get_result()

#print(response['keywords'][0]['text'])
print(response)

result = {}


for e in response['keywords']:
    text = e['text']
    relevance = e['relevance']
    result[text] = result.get(text,0) + relevance
print(result)



