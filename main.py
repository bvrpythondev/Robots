'''

The MIT License

Copyright (c) 2010-2019 Google, Inc. https://www.python.org/

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

Author: Bernardo Vieira Rocha
Github: https://github.com/bvrgamerpvp
'''
import re
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, KeywordsOptions
from time import sleep
from sentence_splitter import  split_text_into_sentences
import  wikipedia
from google_images_download import google_images_download
import feedparser


natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-11-16',
    iam_apikey='YOUR-APYKEY',
    url='URL-KEY'
)

content = {}
googletrend = ""
counter = 0


def main():
    global content

    def askAndReturnSearchTerm():
        global googletrend,counter

        inputask = str(input("Escreva G para sugestões do google or pressione I para  seu propio input: ")).upper()

        if inputask == "G":
            for trend in searchGoogleTrendTopics():
                result = str(counter) + ": " + str(trend)
                print(result)
                counter += 1
            sleep(2)

            ask = int(input("\nEscolha uma opção: "))
            print("Voce escolheu {}".format(searchGoogleTrendTopics()[ask]))

            term = searchGoogleTrendTopics()[ask]

            return term

        else:
            userinput = str(input("OK.... Escreva a wikipedia search term : "))
            return userinput

    def askAndReturnPrefix():
        prefixes =('''-[0] Quem é\n-[1] O que é\n-[2] A história de\n''')
        selectprefixesIndex = int(input(prefixes))

        if selectprefixesIndex == 0:
            return "Quem é"
        elif selectprefixesIndex == 1:
            return  "O que é"
        elif selectprefixesIndex == 2:
            return "A história de"
        else:
            print("\033[0;31mThe input is incorrect please try again!")
            exit()
            return 'Error'

    content['SearchTerm'] = askAndReturnSearchTerm()
    content['prefix'] = askAndReturnPrefix()
    #content['OriginalText'] = wikipedia()
    content['WatsonTextLimitted'] = []
    print(content)



def wikipediaText():
    wikipedia.set_lang('pt')
    summary = wikipedia.summary(content["SearchTerm"], sentences=7)
    summary = re.sub(r"\([^)]*\)", "", summary)
    summary.replace("\n","")
    print(summary)
    return summary

def breaksetences(text):
    content['sentences'] = split_text_into_sentences(
        text=text,
        language="pt",
    )
    return content['sentences']

def images():
    response = google_images_download.googleimagesdownload()
    arguments = {"keywords": content['SearchTerm'], "limit": 7,
                     "print_urls": True}
    paths = response.download(arguments)
    print(paths)


def searchGoogleTrendTopics(geo = 'BR',period = 'daily'):
    # Return a array with with google's trend topics titles
    searchUrl = 'https://trends.google.com/trends/trendingsearches/'+period+'/rss?geo='+geo
    feed = feedparser.parse(searchUrl)
    googleTrendsTitles = [feed.entries[i].title for i in range(len(feed.entries))]
    return googleTrendsTitles
def tags():

    result = {}
    watsoninput = ''
    for i in range(0,3):
        count = 0
        content['WatsonTextLimitted'].append(content['sentences'][count])
        count += 1


    for e in content['WatsonTextLimitted']:
        watsoninput += str(e)
    response = natural_language_understanding.analyze(
        text=watsoninput,
        features=Features(keywords=KeywordsOptions(sentiment=False, emotion=False, limit=3))).get_result()

    for e in response['keywords']:
        text = e['text']
        relevance = e['relevance']
        result[text] = result.get(text, 0) + relevance
        content['WatsonTextKey'] = text

    content['tags'] = result
    return content['tags']





main()
breaksetences(wikipediaText())
tags()
images()





