# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "D:\\app\\python\\transcribe\\API Project-c5200311a916.json"

client = speech.SpeechClient()

audio    = types.RecognitionAudio(uri='gs://yonggeunoh/testa20171205090904.flac')
config   = types.RecognitionConfig(encoding=enums.RecognitionConfig.AudioEncoding.FLAC
                                 , sample_rate_hertz=44100
                                 , language_code='en-US')
operation  = client.long_running_recognize(config, audio)

print('Waiting for operation to complete...')

response = operation.result(timeout=90)
# Each result is for a consecutive portion of the audio. Iterate through
# them to get the transcripts for the entire audio file.
for result in response.results:
    # The first alternative is the most likely one for this portion.
    print('{}'.format(result.alternatives[0].transcript))
