import acodec
import atest
try:
    import bad_codec_name_test
    print "Failed test for whether incorrect codec name causes error #6"
except SyntaxError:
    print "Passed test for whether incorrect codec name causes error #6"

