"""
1. Write a function to check if a string is a palindrome. The function should ignore all spaces and punctuation
like “.”, “!”, “?”. Example sentence with punctuation: "Madam, in Eden, I'm Adam."
"""
def is_palindrome(example_sentence):
    avoid_char = ['.','!','?',' ',"'",',']
    clean_text_arr = [char for char  in example_sentence if char not in avoid_char]
    clean_text = ''.join(clean_text_arr).lower()
    if clean_text == clean_text[::-1]:
        return True
    return False

if __name__ == "__main__":
    example_sentence = "Madam, in Eden, I'm Adam"
    result = is_palindrome(example_sentence)
    if result:
        print(f"\"{example_sentence}\" is palindrome")
    else:
        print(f"\"{example_sentence}\" is not palindrome")

    