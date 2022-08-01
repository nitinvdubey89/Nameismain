import re

s = r"\d{4}"

string2 = "192.168.1.4"
#####################
print("#####################example1")
print(string2.split('.'))

#\d will match any digit from 0 to 9 in a target string \d{4} means consecutive 4 digits

#EOL While Scanning String Literal Error appears when your python code ends
# before ending the string quotes. In simpler terms, your string quotes are missing in the code either by human mistake or
# incorrect syntax mistake.

string1 = '''The Euro STOXX """ 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February.'''
print(len(string1))
print(type(string1))
t = re.compile(s)  ## turns the r"\d{4}" into a regular expression object that we can work with
print(type(t))
result30 = re.findall(r"\b", string1)
print("This is output for \b",result30)



result = re.findall(t, string1)
print(result)
print(type(result))

string3 = '''The Euro STOXX 600 index, """"  #### ,,,,, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998.\n The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February.'''
result23  = re.findall(r"\W{1,}", string3)
print("this is for slash W", result23)



result28 = re.findall(r"\b\w{1,}\b", string3)
print("THIS IS THE RESULT FOR slash b before and after a slash w word",result28)

#re.search(pattern , string, flags) for no we will not discuss flags
new_result = re.search(r"\d{3}" , string1)
print(new_result)  # what is span, search method will always match and return only the first occurence of pattern string inside the target string
# span=(15, 18) 15 is the index at which 6 is located and 18 is where the first character starts
print(type(new_result))
print(string1[15:18])

result1 = re.match(r"\w{4}", string1)
#\w represents any alphanumeric value or character, upper case or lower case as well as digits 0-9
#\w does not match whitespaces
print(type(result1))
print(result1)

result2 = re.fullmatch(r".{285}", string1) ##  i want to match a string of 285 characters except the new line character
print(type(result2))
print(result2)

result3 = re.fullmatch(r"\w{285}", string1)
print(type(result3))
print(result3)

result4 = re.findall(r"\d{3}", string1)
print(type(result4))
print(result4)

result5 = string1.split(" ")
print(result5)

result6 = re.split(r"\s", string1)
print(result6)


result7 = re.split(r"\s{3}", string1) # it means 3 consequtive white spaces
print(result7)


#result8  = re.sub(pattern, repl, string , count, flags) # substitute
# by default count is 0 , flags is also optional
# replacing one or more occurences of a certain pattern in the target string with another string
# replace all the words that are made of upper case with the word index also all upper case
#
result8 = re.sub(r"[A-Z]{2,}", "INDEX", string1, 2 ) #atleast{2,} 2 times , # setting count is 2 means INDEX will not replace capital words more than 2 times
#[A-Z] is a character class and [a-z]
print(type(result8))

result9 = re.subn(r"[A-Z]{2,}", "INDEX", string1, 2)
print(result9) # returns the number of replacements done if count not mentioned and if count is mentioned then returns count
print("new")

result10 = re.search(r".+\s(.+ex).+(\d\d\s.+).", string1) # \d\d is same as \d{2}
print(result10.group(2))
print(result10.group(1))
print("wait")
print(result10.group(0))
print("try")
print(result10.groups()) # group indexing always starts at 1

# . represents any character except new line
# + represents means that the preceding pattern is repeating one or more times
# s matches the space character before the word index

result11 = re.findall(r".+\s(.+ex).+(\d\d\s.+).", string1) # \d\d is same as \d{2}
print(result11)
#print(result11.group(1))

#Note the difference between parameters and arguments: Function parameters are the names listed in the function's definition. Function arguments are the real values passed to the function. Parameters are initialized to the values of the arguments supplied
#Class Attribute: Class Attributes are unique to each class. Each instance of the class will have this attribute.
#Instance Attribute: Instance Attributes are unique to each instance, (an instance is another name for an object). Every object/instance has its own attribute and can be changed without affecting other instances.
#https://www.geeksforgeeks.org/difference-between-attributes-and-properties-in-python/#:~:text=Attributes%20are%20described%20by%20data,are%20special%20kind%20of%20attributes.

# start method returns the index at which that grups starts inside the larget target string
#
print("strart, end and span ")
print(result10.start(1))
print(result10.start(2))
print(string1.index("index"))
print(string1.index("19 February"))
print(result10.end(1))
print(result10.end(2))
print(string1[21:26])
print(string1[275:286])
print(result10.span(1))
print(result10.span(2))

s = 'nitindubey'
print(s[4:6])

#list= [1,1,1,2,2,2,2,3,3,3,3]
#for i in list:
#    print(list.index(i)) # index only matches the first element

result12 = re.findall(r"the", string1) # case sensitive matching
print(result12)

result13 = re.findall(r"the", string1 , re.I) # case sensitive matching , I is the ignore
print(result13)


string2 = "Hello\nPython"
result14 = re.search(r".+", string2, re.S) #. does not catch the new line character .S will match the entire string
print(result14)


result15 = re.search(r""".+\s #Begining of the string )
                        (.+STO) # searching for index 
                        .+ #Middle of string 
                        (\d\d\s.+).  #Date at the end""",string1, re.X)
print(result15.groups())
# re.X is  verbose flag

##################### METACHARACTERS #####################

#. the dot()
# a . represents any character except the new line character i.e. \n , letters upper of lowet, digits , symbos, puncutaliton, commands nad colons and white spaces

result16 = re.search(r"(.+)", string1 )
print(result16.groups(1))

# ^ matches a pattern only at the begining of a line

result17 = re.search(r"^\w{3}", string1 )
#\w matches word characters meaning letters, lower and upper , numbers and _ character
print(result17)  # this is matching the first three char
print(type(result17.groups())) ## if you have multiline thwn we can use the flahg , re.M

# $ is the last string of aline
result18 = re.findall(r"\s(\w{2,})\W$", string3, re.M ) # mathciong the last word in a line excluding the space between words and the period
# \s represents the whitespace and matches a whitespace
#\w{2,} represents a word with atleast 2 characters
#\W$  matches any non alphanumerical  oppposite of \w
print(result18)

# * : 0 or more repitions of the preceding expression , that expression is the last \d over here , number with 2 digits or possibly 3 digits i.e. 3 is possible
# or not possible . no upper limit in repition

result19 = re.findall(r"\d\d*", string3 , re.M)
print(result19)

result20= re.findall(r"E.* ", string3 , re.M) # it will match a whitespace appears, . metacharacter also considers whitespace hence it does not stop at first whitespace
print(result20)

result21 = re.findall(r"E\w*", string3, re.M)
print(result21)

#\w matches any alphanumeric or word charac
#Lower-case and upper case letters
#Digits 0-9
#Underscore



result22 = re.findall(r"\s(\w{3,5})\s", string3)
print(result22)

#\W matches any non-alphanumeric
#1)Whitepsaces

result23  = re.findall(r"\W", string3)
print(result23)


result24 = re.findall(r"\s", string3)
print(result24)

result25 = re.findall(r"\S{8,}", string3) # 8 or more repition of preceding expression and retruns in a list
print(result25)

result26= re.findall(r"(\d)[a-z]", string3)
print(result26)

result27 = re.findall(r"\W\D \W", string3) # all non digit in our
print(result27)

result28 = re.findall(r"\b\w{10,}\b", string1)
print(result28)

result29 = re.findall(r"\bEuro\b", string1)
print(result29)


#\b always matches the empty string or boundary between alphanumeric character and non alphanumberic characer
#\B always matches the empty string or boundary between two alphanumeric character  or TWO non alphanumeric char

result31 = re.findall(r"\B", string1)
print(result31)

#Alphanumeric: alphanumeric characters are
# those comprised of the combined set of the 26 alphabetic characters, A to Z, and the 10 Arabic numerals,
# 0 to 9.


result32 = re.findall(r"\Bcross", string1)
print(result32)


result33 = re.findall(r"cross\B", string1)
print(result33)


result34 = re.findall(r"\Bcross\B", string1)
print(result34)

result35 = re.findall(r"\A([A-Z].*?)\s", string3, re.M)
print(result35)

result36 = re.findall(r"^([A-Z].*?)\s", string3, re.M)
print(result36)

result37 = re.findall(r"\d\d\d?", string3, re.M) # last digit to be repeated 0 ir 1 tine
print(result37)

result38 = re.findall(r"E.?u", string1) # result is ['Eu', 'Eu'] basically
print(result38)

result39 = re.findall(r"E.? ", string1) # result is ['E, '] basically white space.
print(result39)

result40 = re.findall(r"E\W", string1) # result is ['E, '] \w does not match whitespaces
print(result40)

result41 = re.findall(r"E\w", string1) # result is ['E, '] \w does not match whitespaces
print(result41)

### greedy and non greedy behaviour

result42 = re.findall(r"\d\d\d*", string1) # result is ['E, '] \w does not match whitespaces
print(result42)

result41 = re.findall(r"\d\d\d*?", string1) # result is ['E, '] \w does not match whitespaces
print(result41)


result43 = re.findall(r"\d\d\d+", string1) # result is ['E, '] \w does not match whitespaces
print(result43)

result44 = re.findall(r"\d\d\d+?", string1) # result is ['E, '] \w does not match whitespaces
print(result44)


result45 = re.findall(r"\d\d\d??", string1) # result is ['E, '] \w does not match whitespaces
print(result45)

#####
#Examples:Metacharacters - Greedy vs. non-greedy ( *?, +?, ?? ) - Notebook

#>>> import re
#>>> result = re.findall(r"\d\d\d*", string)
#>>> result
#['600', '11', '48', '1998', '600', '19']
##>>> result = re.findall(r"\d\d\d*?", string)
#>>> result
#['60', '11', '48', '19', '98', '60', '19']
#>>> result = re.findall(r"\d\d\d+", string)
#>>> result
#['600', '1998', '600']
#>>> result = re.findall(r"\d\d\d+?", string)
#>>> result
#['600', '199', '600']
#>>> result = re.findall(r"\d\d\d?", string)
#>>> result
#['600', '11', '48', '199', '600', '19']
#>>> result = re.findall(r"\d\d\d??", string)
#>>> result
#['60', '11', '48', '19', '98', '60', '19']

###### sqaure brackets
# the square brackets are very useful in pattern matching  as they represent sets of characters and character classes
# search for all occurences of w,x, k or q inside the strinng anf have the returne d

result45 = re.findall(r"[wxkq]", string3, re.M)
print(result45)
lenx = len([x for x in result45 if "x" in x])
lenw = len([x for x in result45 if "w" in x])
lenk = len([x for x in result45 if "k" in x])
lenq = len([x for x in result45 if "q" in x])
print(f'{lenx}, {lenw}, {lenq}, {lenk}')


result46 = re.findall(r"[a-d]", string3)
print(result46)

result47 = re.findall(r"[S-W]", string3)
print(result47)

result48= re.findall(r"[1-5]", string3)
print(result48)

result49= re.findall(r"[a-f][c-w]", string3)
print(result49)

result50= re.findall(r"[0-5][7-9]", string3)
print(result50)

result51= re.findall(r"[0-9][a-z]", string3)
print(result51)

result52= re.findall(r"[^X]", string3) # except captial X print all  , negation is done by [^..}
print(result52)

print("X" in result52)

## special char *.? loose power inside sqaure bracket

result53 = re.findall(r"[(.+?)]", string3) # we are searchin for (.+?) in the string , special char loose power
print(result53)



####### character classes ###########

result54 = re.findall(r"[0-9]", string3)
print(result54)

result55 = re.findall(r"[a-zA-Z]", string3)
print(result55)

result56 = re.findall(r"[^0-9]", string3)
print(result56)

result57 = re.findall(r"[ \n\t\r\f\v]", string3) # al white spaces
print(result57)

print(len(result57))
print(string3.count(" "))

result58 = re.findall(r"[^ \n\t\r\f\v]", string3) # no white space
print(result58)

result59 = re.findall(r"[a-zA-Z0-9_]", string3) # all alphanumeric numbers
print(result59)

result60 = re.findall(r"[^a-zA-Z0-9_]", string3) # all alphanumeric numbers
print(result60)



####### CURLY BRACES {}
## lets say we want all 4 letter word in target string

result61 = re.findall(r"\b\w{4}\b", string3)
print(result61)

result61 = re.findall(r"\b\w{3,5}\b", string3)
print(result61)

result61 = re.findall(r"\b\w{3,}\b", string3)
print(result61)

number = "12121322328432731823719237916412638972"

result62 = re.search(r"\d{3,6}?", number) #<re.Match object; span=(0, 3), match='121'
print(result62)

result63= re.search(r"\d{3,6}", number) #<re.Match object; span=(0, 3), match='121213'
print(result63)

result64 = re.search(r"\d{3}|\d{4}|\b[A-Z]{4}\b", string3) # search only matches the first character and the rest are ignored
print(result64)

result65 = re.search(r"\d{8}|\d{4}|\b[A-Z]{4}\b", string3) # search only matches the first character and the rest are ignored
print(result65)

result66 = re.findall(r"\d.", string1)
print(result66)

result67 = re.findall(r"\.", string1)
print(result67)
# . matches any character except the new line

result68 = re.findall(r".", string1)
print(result68)


## + sequence

result69 = re.findall(r"\d\d\d+", string1)
print(result69)


result69 = re.findall(r"\W+", string1)
print(result69)
print(len(result69))
print(len(string1)) # string length is 288

result71 = re.findall(r"E.* ", string1)
# the space represents right border for the pattern match
#* is greedy

strinng = "1211111111111121111111111111111111"
result71 = re.findall(r"1*", strinng)
print(len(result71))
print(len(strinng))
print(result71)


#\A will always match staart of the string  regardless of multiline or not but ^ will match every line first string


result72 = re.findall(r"([A-Z].*?)\s", string3, re.M)
print(result72)

result73 = re.findall(r"([A-Z].*?)", string1, re.M)
print(result73)

result74 = re.findall(r"\W$", string3, re.M) # ['.', '.']
print(result74)

result74 = re.findall(r"\W\Z", string3, re.M) # ['.']
print(result74)