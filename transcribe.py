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


flacArr = ['test20171205092107','test20171205104654','test20171205105137','test20171206135253']
#flacArr = ['test20171205090904']

for fa in flacArr:
    audio    = types.RecognitionAudio(uri='gs://yonggeunoh/' + fa + '.flac')
    config   = types.RecognitionConfig(encoding=enums.RecognitionConfig.AudioEncoding.FLAC
                                     , sample_rate_hertz=44100
                                     , language_code='en-US')
    operation  = client.long_running_recognize(config, audio)
    
    print('Waiting for operation to complete...')
    
    response = operation.result()
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    f = open(fa + '.txt', 'w')
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        for alternative in result.alternatives:
            f.writelines(alternative.transcript)
            print(alternative.transcript)
    f.close()
    
