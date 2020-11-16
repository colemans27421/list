"""
    This is the file you edit.

    You *do not need to create a new file*. Just edit this file to achieve what is needed.

    Use the function provided to solve this puzzle.

    DO NOT EDIT THE EXISTING CODE. You do not need to change the function definition line or the if statement lines.
"""

def is_palindrome(phrase: str) -> bool:
    '''
        Add your code between this comment and the if statement. "normalized" and "reversed" are variabled you should end up with.
    '''


 normalized = phrase.lower().strip().replace(" ", "")
    reversed = normalized[::-1]
    return normalized == reversed


    # DO NOT TOUCH. ADD CODE ONLY ABOVE THIS.
    if(normalized == reversed):
        return True
    else:
        return False
