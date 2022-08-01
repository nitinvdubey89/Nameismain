# string has to be encoded into bytes
# encoding scheme like MP3 or WAVP
# PICTUE IN PNG
# mp, ascii etc are examples of encoding scheme
# an encoding scheme is a format to store videa, audio impages text and so on as sequence of bytes
# string is a sequence of characters that are abstract character and cannot be directly stored in a computer therefore they are stored as object bytes
# bytes objects are immutable sequence of small integers in the range of 0 and 255 , printed as utf-8 characters
# ascii is only a subset of utf-8 consisting only 158 characters
#

s1 = 'abc'
b1 = s1.encode('utf-8') # default encoding scheme is utf-8 therefore its not mandatory to use it

print(type(b1))
## object type of bytes
print(b1)  # b'abc' # b means bytes ## reason its printed as b'abc because the built-in print function is used to print strings therefore it managed a string representation
print(b1[0]) # 97  ## 97 is ascii code for a , b is 98 and till z sequenctially
print(b1[1]) # 98

# ascii can only represent 128 characters , these are the latin letters including english alphabets , the digits  and most used symbols

s2  = 'ハイキング' # this is japenese and not ascii but utf-8

b2 = s2.encode()
print(b2) # b'\xe3\x83\x8f\xe3\x82\xa4\xe3\x82\xad\xe3\x83\xb3\xe3\x82\xb0'
print(b2[0]) #227
# now the print function could not get  a string representation like before and it printed a sequence of bytes in base 16
#

s3 = b2.decode()
print(s3 , s3 == s2) ## it returned true