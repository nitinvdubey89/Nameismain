import re

# testing .,^,$,*,+,?,*?,+?,??,\,[],character-classes,{},|,\A and \Z,\b and \B,\d and \D,\s and \S,\w and \W

string1 = '''The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off Thy value of STOXX 600 shares since its all-time peak on 19 February.'''
string2 = '''The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998.\n The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February .'''

#re_test_Z = re.findall(r"[A-Z]+? ", string1)
#print(re_test_Z)

re_test_Z = re.findall(r"\w{2,}\W$", string1) # last word excluding the period at the end of each sentence

print(re_test_Z)
print(len(re_test_Z))
print(type(re_test_Z))

result25 = re.findall(r"\D{8,}", string1) # 8 or more repition of preceding expression and retruns in a list
print(result25)

#\b always matches the empty string or boundary between alphanumeric character and non alphanumberic characer
#\B always matches the empty string or boundary between two alphanumeric character  or TWO non alphanumeric char


result31 = re.findall(r"\B", string1)
print(result31)

