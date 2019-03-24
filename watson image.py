import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='-sTCyL1lZ0iT_6rX8JjvrWzk28NiMFiBepMr5vHxt-eJ')

url = 'https://watson-developer-cloud.github.io/doc-tutorial-downloads/visual-recognition/fruitbowl.jpg'
classifier_ids = ["food"]

classes_result = visual_recognition.classify(url=url, classifier_ids=classifier_ids).get_result()
print(json.dumps(classes_result, indent=2))