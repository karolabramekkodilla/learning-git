def check_if_word_is_palindrom(word = "word_to_check"):
    i = 0 
    j = len(word) - 1  
    is_palindrome = True  

    while i < j:
        if word[i] != word[j]:  
            is_palindrome = False
            break
        i += 1
        j -= 1

    return is_palindrome

print(check_if_word_is_palindrom(word="kajak"))
print(check_if_word_is_palindrom(word="yo"))