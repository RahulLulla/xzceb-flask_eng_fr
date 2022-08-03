'''
Author: Rahul Lulla
Code: For English to French and French to English translation
'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Language Translator Instance
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def englishToFrench(englishText):
    '''
    Translate from English to French
    '''
    if englishText == '' or englishText is None:
        return ''
    translation = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()
    return translation["translations"][0]["translation"]

def frenchToEnglish(frenchText):
    ''' Translate from French to English '''
    if frenchText == '' or frenchText is None:
        return ''
    translation = language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result()
    return translation["translations"][0]["translation"]

#print(englishToFrench('Hello'))