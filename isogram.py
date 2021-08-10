def is_isogram(string):
    string_list = {}
    for letter in string:
        string_list[letter] = string.count(letter)
    for x in (string_list):
        if string_list[x]==2 in string_list.values():
            return f"{string} is not an isogram"
        else:
            return f"{string} is an isogram"
