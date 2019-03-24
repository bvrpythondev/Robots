from watson_developer_cloud import TextToSpeechV1

text_to_speech = TextToSpeechV1(
    iam_apikey='QBnzuF535C-R93I8Y8jh3TDO8RFmgL5z2pCh4RmmVPe8',
    url='https://stream.watsonplatform.net/text-to-speech/api'
)

with open('hello_world.wav', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            'Hello Who I am?',
            'audio/wav',
            'en-US_AllisonVoice'
        ).get_result().content)


