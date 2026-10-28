def first_and_last(s: str) -> str:
    """
    Return a new string made of the first character of `s`
    followed by the last character of `s`.

    - If `s` is empty, return "".
    - If `s` has exactly one character, return that character twice.

    Example: first_and_last("python") -> "pn"
    """
    if len(s)==0:
        return ""

    return s[0]+s[-1]
        
    
    pass


def reverse_string(s: str) -> str:
    """
    Return a new string containing the characters of `s` in
    reverse order. Use a slice with a negative step.

    Example: reverse_string("python") -> "nohtyp"
    """
    return s[::-1]
    pass



def every_kth_from(s: str, start: int, k: int) -> str:
    """
    Return characters at positions start, start + k,
    start + 2k, and so on.
    """
    if start < -len(s) or start >= len(s):
        return ""

    if start < 0:
        start = len(s) + start

    return s[start::k]
