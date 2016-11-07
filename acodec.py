import encodings, codecs

# Our StreamReader
class aStreamReader(codecs.StreamReader):
    def __init__(self, codec_name = "null_codec"):
        self.codec_name    = codec_name
        self.output_source = None
        codecs.register(self.search_function)  # register our new codec search function

    def outputFromInput(input):
        return input
        
    def readline(self, size=None, keepends=True):
        if output_src == None:
            input_source  = self.stream.read().decode("utf8")
            output_source = StringIO(outputFromInput(input_source))
        return output_source.readline(size)

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
                                 streamwriter = u8.streamwriter)

theStreamReader = aStreamReader()

