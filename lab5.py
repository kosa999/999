import re

# 1. Match 'a' followed by zero or more 'b's. А и несколько и более б
x1 = re.fullmatch(r'ab*', 'abbb')
print("1 экс:", x1)

# 2. Match 'a' followed by two to three 'b's. А и 2 или 3 б.
x2 = re.fullmatch(r'ab{2,3}', 'abbbbbb')  # слишком много b, так что не будет компилиться
print("2 экс:", x2)

# 3. Sequences of lowercase letters joined with an underscore. Апперы и после андеры.
x3 = re.findall(r'[a-z]+_[a-z]+', 'this_is a_test_example')
print("3 экс:", x3)

# 4. One uppercase letter followed by lowercase letters
x4 = re.findall(r'[A-Z][a-z]+', 'Genius kbtu Test')
print("4 экс:", x4)

# 5. 'a' followed by anything, ending in 'b'
x5 = re.fullmatch(r'a.*b', 'axdfsdfsfdsxb')
print("5 экс:", x5)

# 6. Replace space, comma, or dot with colon
x6 = re.sub(r'[ ,.]', ':', 'sobaka, dog. Hund')
print("6 экс:", x6)

# 7. Convert snake_case to camelCase
def to_camel(s):
    parts = s.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])
x7 = to_camel('snake_case_example')
print("7 экс:", x7)

# 8. Split string at uppercase letters
x8 = re.findall(r'[A-Z][^A-Z]*', 'SplitAtUpperLetters')
print("8 экс:", x8)

# 9. Insert spaces between words starting with capital letters
x9 = re.sub(r'([a-z])([A-Z])', r'\1 \2', 'MySpaceBarIsBroken')
print("9 экс:", x9)

# 10. Convert camelCase to snake_case
x10 = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', 'camelCaseToSnake').lower()
print("10 экс:", x10)
