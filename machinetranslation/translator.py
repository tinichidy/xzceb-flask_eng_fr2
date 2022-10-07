import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version ='2018-05-01'
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=version, authenticator = authenticator)


def englishToFrench(englishText):
    frenchText = language_translator.translate(englishText, model_id = 'en-fr').get_result()
    return frenchText['translations'][0]['translation']
print(englishToFrench(input("Please Input English Text: ")))


def frenchToEnglish(frenchText):
    englishText = language_translator.translate(frenchText, model_id = 'fr-en').get_result()
    return englishText['translations'][0]['translation']
print(frenchToEnglish(input("Please Input French Text: ")))
