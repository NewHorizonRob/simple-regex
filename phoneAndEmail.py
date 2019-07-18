#Robert Thomas
#AIST 2120  
#Homework 3a
#6/11/19
#phoneAndEmail.py


import pyperclip, re #imports the pyperclip and re modules

# regular expression for an phone number
phoneRegex = re.compile(r'''(
(\d{3}|\(d{3}\))?    #area code (with or without parenthesees within the string)
(\s|-|\.)?           #separator (optional because of the question mark)
(\d{3})                #first 3 digits of number 
(\s|-|\.)            #seperator (not optional)
(\d{4})                #last 4 digits of number 
(\s*(ext|x|ext.)\s*(\d{2,5}))?   # extension of the number (optional because of the question mark)
)''',re.VERBOSE)


#regular expression for an email address
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+  # user name (plus symbol matches one or more of the preceeding group)
@                  #
[a-zA-Z0-9.-]+     # domain name (plus symbol matches one or more of the preceeding group)
(\.[a-zA-Z]{2,4})  #  .website name
)''', re.VERBOSE)  # verbose ignores the whitespace and comments


text = str(pyperclip.paste()) #converts whatever is pasted to the clipboard into a string and stored in variable text
matches = [] #makes a new list called matches
for groups in phoneRegex.findall(text): #for all the phone group matches in the text variable 
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        matches.append(phoneNum) # appends the phone numbers to matches
for groups in emailRegex.findall(text): #for all the email group matches in the text variable 
    matches.append(groups[0]) #appends the email addresses to matches



if len(matches) > 0: # if the length of matches is greater than 0
    pyperclip.copy('\n'.join(matches)) # join the items of matches to a string and copy them
    print('Copied to Clipboard:')
    print('\n'.join(matches)) #print the results of the matches
else:
    print('No phone numbers or email addresses found.') # will print this if the initial if statement is false