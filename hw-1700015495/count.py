#count
s=input('input a string:')
letter=0
space=0
digit=0
other=0
for c in s:
    if c.isalpha():
        letter+=1
    elif c.isspace():
        space+=1
    elif c.isdigit():
        digit+=1
    else:
        other+=1
print('There are {0} letters,{1} spaces, {2} digits and {3} other characters \
in your string.'.format(letter,space,digit,other))