import re
# re.match, re.search. re.compile, re.fullmatch, re.split, re.sub, reb.subn, group and groups, start, end and span
# optional flags , attribute error

from pprint import pprint


string1 = '''The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February!!!...'''
result2 =  re.search(r".+(\b.+ex).+(\b[A-Z]{4}\b).+(\d\d\s.+)\.", string1)
# \. matches the actual . and not metacharacter .
print("this is the result of a capturing group",result2.groups())


# lets make non-capturing group , adding ?:

result2 =  re.search(r".+(?:\b.+ex).+(\b[A-Z]{4}\b).+(\d\d\s.+)\.", string1)
# \. matches the actual . and not metacharacter .
print("this is the result of a capturing group",result2.groups())

string3 ="___ ___"
############## SEARCH #########################################

#  search method scans through the entire target string and looks for patterns  that we specify as the first argument
#
result = re.search(r"\d{3}", string1)
print("this is \d{3}",result.group())
# we had 3 such occurences, the result returned by the string is a match object
# the search method will only match the first occurence of the pattern
# and if no match is found then it will return None.

result = re.findall(r"(?<=,\s)\b\w+\b", string1)
print(result)


###################### MATCH ###################################################

######MATCH METHOD MATCHES ONLY AT THE BEGINING OF THE STRING , if no match is found then returns none#################
#result = re.match(r"\w{4}", string1)
#print(result.group())
#    print(result.group())
#AttributeError: 'NoneType' object has no attribute 'group' # here the code will exit with code 1


result = re.match(r"\w{3}", string1)
print("this is \w",result.group())

###################### FULL  MATCH ######################


#### returns the result  only if the pattern matches the entire target string.#########

result1 = re.fullmatch(r".{280}", string1, re.M) # . matches any character except /n
result2 = re.fullmatch(r".{280,}", string1, re.M)
# this means that we want to match a string with 286 characters
print(len(string1))
print("this is sthe result of exact match {280} which is nothng",result1)
print("this is sthe result of exact match {280,} which is ",result2)
#print(result1.group())


######### FIND ALL #########################################

## most frequntly used method , unlike other methods, findall searches for and returns all matches found inside the target sting
# target string is scanned left to right and the matches are returned in the order they are found as alist of strings
# result will be an empty list

resultnew = re.findall(r"\d{3}", string1)
print("this is the result of 3 digit numbers" , resultnew)


####### SPLIT ################################

result2 = string1.split(" ")
print("splitting the string using split function of re module", result2)

# re.split method
result2  = re.split(r"\s", string1)
print(result2)

## difference is that with regex split, we can specify pattern , with default split function we can only
# provide a single char,
# with regex split, we can use a pattern to split a string by comma or dot
## words that start with captial letter, way more flexible
# what if no pattern is found
# if pattern is not found then the string is not split

result2  = re.split(r"\s{3}", string1) # here the three consecutive white spaces are not there and is the only element
print( len(result2) ,"here we are matching 3 consequtive whitespaces",result2)

######### re.sub module ###

## the sub method is used for replacing one or more occurences of a certiain pattern in a target string with another string
# replacing all upper case words with with word INDEX

#result2 = re.sub(pattern, repl, string, count, flags)
result2 = re.sub(r"[A-Z]{2,}","INDEX", string1) # if we dont mention count then it will replace all occurences
print(result2)
print(type(result2))


result2 = re.sub(r"[A-Z]{2,}","INDEX", string1, 2) # if we mention the count then it replaces only the count occurences
print(result2)
print(type(result2))

########### RE.SUBN module

# subn retuns a tuple consisting of the new version of the target string after all the replacesments havve been made
# as the first elemnet and the number of replacements it made as the second element of the tuple

result2 = re.subn(r"[A-Z]{2,}","INDEX", string1)
print(result2)
print(type(result2))

####### OPTIONAL FLAGS ############################################
## can be used with match, search, findall, split and others
# each method we may or maynot specify these flags ,
# top 3 most frequenctly used flags are re.I , re.S and re.X

# re.I is used for ignore i.e. case insensitve matching

result2 = re.findall(r"the", string1, re.I)
print("the search is case insensitive for the word the,",result2)

# re.S is a dotall, . represent any character except the \n and .S makes this exception disappear i.e including \n

string2 = "hello\npython"

result2 = re.search(r".+", string2)
print(result2.group())

result2 = re.search(r".+", string2, re.S)
print(result2.group())

# re.X flag which stands for verbose
# verbose flag enables us to use better spacing, indentation and have a clean format for longer
# and more complex patterns in between
# comments inside the pattern using the hash sign
# parathensis of match, search, findall functions

result2 = re.search(r".+\s(.+ex).+(\d\d\s.+).", string1)
print(result2.groups())


result2 = re.search(r""".+\s # Begining of the string)
                       (.+ex)# Searching for index
                        .+ # Middle of the string   
                        (\d\d\s.+). # Date at the end""", string1, re.X)         # the last
# . means that its exclused out of the group
print(result2.groups())


###### GROUP AND GROUPS###########################
# more often than not , having target string much larger than few words, we are going
# to be interested in several distinct pattern
# we might me interested in finding matches for a word
# match index and 19th feb  ==> this is multuple pattern match i.e. index and 19th feb seperately

result2 = re.search(r".+\s(.+ex).+(\d\d\s.+)", string1)
# we can also use \d{2} # if i dont inlcude last  \d\d\s.+). then
# we get the entire dot in the end i.e. ... rather than ..
print(result2.groups())
print(result2.group(1,2))

# in order to define and isoloate the two pattens we plan to match , we need two things
# 1st we need to enclose each of the two patterns in parantehesis
# 2nd we need to consider the larger context in which these groups reside
# we care about the location of each of these groups in the entire target string
# so we need to define context or borders for each group
# \s is for space
# . is for any type char excpet \n
# + means precen.+\s() means that we have a bunch of chars and a space
# # if none of the groups match then the result is ending pattern repeates 1 or more times
# so tire string

################ EXTENSION NOTATION AND NON-CAPTURING GROUPS    #####################################

#MANAGING and referencing grousp with 20 or 30 groups is difficutl
#(? extension notation syntax
#the characters that follow that ? define the group or role
# when we want to match a group bit not willing to capture output i.e. NON-CAPTURING GROUPS
#
result2 =  re.search(r".+(\b.+ex).+(\b[A-Z]{4}\b).+(\d\d\s.+)\.", string1)
# \. matches the actual . and not metacharacter .
print("this is the result of a capturing group",result2.groups())


# lets make non-capturing group , adding ?:

result2 =  re.search(r".+(?:\b.+ex).+(\b[A-Z]{4}\b).+(\d\d\s.+)\.", string1)
# \. matches the actual . and not metacharacter .
print("this is the result of a capturing group",result2.groups())

############################## NAMED GROUP ######################################
## Named groups and  group dict
# using named grourps, we can refer to groups by name rather than their numbers, especially when having complex pattern
# naming a group is by (?P<name>

result2 =  re.search(r".+(?P<wordex>\b.+ex).+(?P<uppercase>\b[A-Z]{4}\b).+(?P<date>\d\d\s.+)\.", string1)
print(result2.group("wordex", "uppercase", "date"))           # always use double quotes

############## GROUP DICT ########################## ######################

# group dict will return all values using a key value pair in a dictionary, key is the name of the group and value is the string
#
print(result2.groupdict())


############ POSITIVE LOOKAHEAD ASSERTIONS ###################################

# THERE ARE 4 TYPES OF ASSERTION AND PROVIDES FLEXIBILITY IN PATTERN MATCHING
# 1) LOOKAHEAD  postive/negative
# 2) LOOKBEHIND  positive/negative
# (?= ...) this is the pattern   , assertion matches only the pattern matching the ...

result2 = re.findall(r"[A-Z]{5}\s(?=[0-9]{3})", string1)
print(result2)
# (?=[0-9]{3}) basically specifies a condition for the match to be performed  i.e.      [A-Z]{5}\s this is the real match
# additional condition is that this will match [A-Z]{5}\s if this is present after the match(?=[0-9]{3})
# result is that we get STOXX but we did not print the number 

# NOW WE WANT TO MATCH THE EURO but not EUROPE

result2 = re.findall(r"\s.+(Euro)(?=[a-z]+)", string1)
print(result2)

## NEGATIVE LOOKAHEAD ASSERTION

## RETURNS a match if an only if the pattern inside parathesis does not follow the pattern before the parantehsis
#(?! this is th symbol

result2 = re.findall(r"\d(?![5-9]|\D)", string1) # \ D any non digit character i.e space, letter etc
print(result2)


result2 = re.findall(r"\b\w+\b(?!\s)", string1) # \ D any non digit character i.e space, letter etc
print(result2)

print("new")
result3 = re.findall(r"\w+", string3) # \ D any non digit character i.e space, letter etc, \w does not consider spaces
print(result3)



######### POSITIVE LOOKBEHIND ASSERTION ##################

#(?<=...) returns a match if the pattern following the paranthesis is preceeded by the pattern specified inside the paranthesis

result4  = re.findall(r"(?<=\s)\d{1,}", string1)
print("space before the digit",result4)


result4  = re.findall(r"(?<=,\s)\b\w+\b", string1)
print(result4)


########### NEGATIVE LOOKBEHIND ASSERTION #############

# in this case match is returned if the pattern following the paranthesis is not precended  by the pattern inside the paranthesis
# general syntax is the following
# (?<!...)

result = re.findall(r"(?<!\s)\d{1,}", string1)
print("digits not preceeded  by space",result)

######## every occurence of letter x, regardless of it being lower case or upper case that is not preceeded nor followed by x
# we need to use two negative assertions i.e negative look behind and negative lookahead

result = re.findall(r"(?<!x)x(?!x)", string1, re.I)
print(result)