# extension notations
# managing and referencing groups can be difficult
# having pattern of 20 or 30 different groups
# testing .,^,$,*,+,?,*?,+?,??,\,[],character-classes,{},|,\A and \Z,\b and \B,\d and \D,\s and \S,\w and \W


string1 = '''The Euro STOXX  600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February.'''


import re


result2 = re.search(r".+\s(.+ex).+(\d\d\s.+).", string1)
print(result2)
print(dir(result2.group()))  # when you call it like a function i.e.() it should the output of the sting otherwise it return the object address
print(result2.groups())
print(result2.group(1,2)) # this returns a tuple , # groups method cannot be appllied with findall


result1 = re.search(r".+\s(.+ex).+(\d\d\s.+).", string1)
print(result1)

result1 = re.findall(r".+\s(.+ex).+(\d\d\s.+).", string1)
print(result1)


result1 = re.match(r".+\s(.+ex).+(\d\d\s.+).", string1)
print(result1)

result1 = re.fullmatch(r".+\s(.+ex).+(\d\d\s.+).", string1)
print(result1)

result1 = re.split(r".+\s(.+ex).+(\d\d\s.+).", string1)
print(result1)

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
########################################################################################

#(? this symbol represents extension notation
# if want to match a specific group inside the target string  and we are not willing to retrieve the content later using the group or
# groups method ,this is called a non-capturing group i.e. the group is matched but wont be sued to retrieve anything
# when having large number of groups in regex pattern you might want to define even more groups in the pattern while skipping
# ignroing some of the existing groups without deleteing them. The non-capturing group will not be retrieved when using the group or groups method
# however they will  still be there to reactovate at a later time
# the syntax for non-capturing group adds to the general syntax of extension notations by inserting a colon after ?
# this way we can distinguish between regular capturing groups and non-capturing groups
#

#resultextension = re.search(r".+(\b.+ex\b).+(\b[A-Z]{4}\b).+(\d\d\s.+)\.", string1)
resultextension = re.fullmatch(r"(\b.+ex\b)", string1)
print(resultextension)

###############################################################################################