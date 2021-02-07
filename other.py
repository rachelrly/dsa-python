def is_string_palindrome(str):
    for i in range(len(str)):
        if str[i] != str[-i-1]:
           print(f'{str}: false')
           return
    
    print(f'{str}: true')

is_string_palindrome('dad')
is_string_palindrome('a man a plan a canal panama') #currently failing
is_string_palindrome('1001')
is_string_palindrome('tauhida')