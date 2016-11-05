# acodec.py
import encodings, codecs

# Our StreamReader
class aStreamReader(codecs.StreamReader):
    codec_name = "null_codec"
    def outputFromInput(input):
        return input
        
    def readline(self, size=None, keepends=True):
        inputSrc  = self.stream.read().decode("utf8")
        outputSrc = outputFromInput(inputSrc)
        return outputSrc

def search_function(s):
    if s!= codec_name: 
        return None

    u8 = encodings.search_function("utf8")
    return codecs.CodecInfo( name = codec_name, 
                             encode = u8.encode,
                             decode = u8.decode,
                             incrementalencoder = u8.incrementalencoder,
                             incrementaldecoder = u8.incrementaldecoder,
                             streamreader = aStreamReader,        # null_codec StreamReader
                             streamwriter = u8.streamwriter)

codecs.register(search_function)  # register our new codec search function
# End of acodec.py
