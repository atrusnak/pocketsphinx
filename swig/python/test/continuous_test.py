#!/usr/bin/python

from os import environ, path

from pocketsphinx import *
from sphinxbase import *

MODELDIR = "model/"
DATADIR = "swig/python/test/data/"

config = Decoder.default_config()
config.set_string('-hmm', MODELDIR + 'en-us/en-us')
config.set_string('-lm', MODELDIR + 'en-us/en-us.lm.bin')
config.set_string('-dict', MODELDIR + 'en-us/cmudict-en-us.dict')
config.set_string('-logfn', 'nul')
decoder = Decoder(config)

stream = open(DATADIR + 'test2.wav', 'rb')
#stream = open('10001-90210-01803.wav', 'rb')

in_speech_bf = False
decoder.start_utt()
while True:
    buf = stream.read(1024)
    if buf:
        decoder.process_raw(buf, False, False)
        if decoder.get_in_speech() != in_speech_bf:
            in_speech_bf = decoder.get_in_speech()
            if not in_speech_bf:
                decoder.end_utt()
                print ('Result:', decoder.hyp().hypstr)
                decoder.start_utt()
    else:
        break
decoder.end_utt()

