# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import io
import os

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "D:\\app\\python\\transcribe\\API Project-c5200311a916.json"
#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "https://speech.googleapis.com/v1/speech:recognize?key=AIzaSyAXHJflNnJazXtIQqq5VnhNdhn7cWXcJrY"

client = speech.SpeechClient()

with io.open("D:\\app\\python\\transcribe\\testb20171205090904.flac", 'rb') as audio_file:
    content  = audio_file.read()
    audio    = types.RecognitionAudio(content=content)
    config   = types.RecognitionConfig(encoding=enums.RecognitionConfig.AudioEncoding.FLAC
                                     , sample_rate_hertz=44100
                                     , language_code='en-US')
    response = client.recognize(config, audio)
#    response = client.long_running_recognize(config, audio)

    print('Waiting for operation to complete...')
    
    for k in response.results:
        alternatives = k.alternatives
    
        for alternative in alternatives:
            print('{}'.format(alternative.transcript))
    #        print('Confidence: {}'.format(alternative.confidence))
        
