# acodec.py
import encodings, codecs, re, sys

# Our StreamReader
class aStreamReader(codecs.StreamReader):
    outputSrc = None
    codecName = "acodec"

    def outputFromInput(input):
        return input
        
    def readline(self, size=None, keepends=True):
        if outputSrc == None:
            inputSrc  = self.stream.read().decode("utf8")
            outputSrc = StringIO(outputFromInput(inputSrc))
        return outputSrc.readline()

    def search_function(s):
        if s != codecName: 
            return None

        u8 = encodings.search_function("utf8")
        return codecs.CodecInfo( name = codecName, 
                                 encode = u8.encode,
                                 decode = u8.decode,
                                 incrementalencoder = u8.incrementalencoder,
                                 incrementaldecoder = u8.incrementaldecoder,
                                 streamreader = aStreamReader,        # acodec StreamReader
                                 streamwriter = u8.streamwriter)

codecs.register(aStreamReader.search_function)  # register our new codec search function
# End of acodec.py
