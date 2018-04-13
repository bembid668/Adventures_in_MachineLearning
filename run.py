import os
import json
from os.path import join, dirname
from dotenv import load_dotenv
from watson_developer_cloud import SpeechToTextV1 as STT
from watson_developer_cloud import NaturalLanguageUnderstandingV1 as NLU
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features
from speech_sentiment_python.recorder import Recorder

recorder = Recorder("speech.wav")
recorder.record_to_file()

def transcribe_audio(path_to_audio_file) :
    username = os.environ.get("SPEECH_TO_TEXT_USERNAME")
    password = os.environ.get("SPEECH_TO_TEXT_PASSWORD")
    speech_to_text = STT(username=username, password=password)

    with open(join(dirname(_file_), path_to_audio_file), 'rb') as audio_file:
        return speech_to_text.recognize(audio_file, content_type='audio/wav')

def get_text_sentiment(text):
    nlu_username = os.environ.get("NLU_USERNAME")
    nlu_password = os.environ.get("NLU_PASSWORD")
    nlu = NLU(username=nlu_username, password=nlu_password)

    result = nlu.analyze(text=text)

    if result['docSentiment']['type'] == 'neutral' :
        return 'neutral', 0
    return result['docSentiment']['type'], result['docSentiment']['score']


def main():
    recorder = Recorder("speech.wav")

    print("So How are you doing today?\n")
    recorder.record_to_file()

    print("Transcribing audio....\n")
    result = transcribe_audio('speech.wav')

    text = result['results'][0]['alternatives'][0]['transcript']
    print("Text: " + text + "\n")

    sentiment, score = get_text_sentiment(text)
    print(sentiment, score)

if __name__ == '__main__':
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    try:
        main()
    except:
        print("IOError detected, restarting...")
        main()
