#!/usr/bin/python

import sys, os
from pocketsphinx import *
from sphinxbase import *


modeldir = "model/"
datadir = "swig/python/test/data/"

# Create a decoder with certain model
config = Decoder.default_config()
config.set_string('-hmm', modeldir + 'en-us/en-us')
config.set_string('-dict', modeldir + 'en-us/cmudict-en-us.dict')
config.set_string('-keyphrase', 'h seven')
config.set_string('-logfn', 'nul')
config.set_boolean('-remove_silence', False)
config.set_boolean('-remove_noise', False)
config.set_float('-kws_threshold', 1)


# Open file to read the data
stream = open(datadir + "test2.wav", "rb")

# Alternatively you can read from microphone
# import pyaudio
# 
# p = pyaudio.PyAudio()
# stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
# stream.start_stream()

# Process audio chunk by chunk. On keyphrase detected perform action and restart search
decoder = Decoder(config)
decoder.start_utt()
count = 0
while True:
    buf = stream.read(1024)
    if buf:
         decoder.process_raw(buf, False, False)
    else:
         break
    if decoder.hyp() != None:
        print ([(seg.word, seg.prob, seg.start_frame, seg.end_frame, int(seg.start_frame/6000), (seg.start_frame/6000 - int(seg.start_frame/6000))*60) for seg in decoder.seg()])
        print ("Detected keyphrase, restarting search")
        count += 1
        decoder.end_utt()
        decoder.start_utt()

print(count)