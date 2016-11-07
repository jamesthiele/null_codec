# acodec.py
import encodings, codecs

# Our StreamReader
class aStreamReader(codecs.StreamReader):
    def __init__(self, codec_name = "null_codec"):
        self.codec_name = codec_name
        codecs.register(self.search_function)  # register our new codec search function

    def outputFromInput(input):
        return input
        
    def readline(self, size=None, keepends=True):
        inputSrc  = self.stream.read().decode("utf8")
        outputSrc = outputFromInput(inputSrc)
        return outputSrc

    def search_function(s):
        if s!= self.codec_name: 
            return None

        u8 = encodings.search_function("utf8")
        return codecs.CodecInfo( name = self.codec_name, 
                                 encode = u8.encode,
                                 decode = u8.decode,
                                 incrementalencoder = u8.incrementalencoder,
                                 incrementaldecoder = u8.incrementaldecoder,
                                 streamreader = self,        # null_codec StreamReader
                                 ## streamreader = theStreamReader,        # null_codec StreamReader
                                 ## streamreader = aStreamReader,        # null_codec StreamReader
                                 streamwriter = u8.streamwriter)

theStreamReader = aStreamReader()

## codecs.register(theStreamReader.search_function)  # register our new codec search function
## codecs.register(aStreamReader.search_function)  # register our new codec search function
# End of acodec.py
