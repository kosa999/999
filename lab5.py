
import re

# 1. Match 'a' followed by zero or more 'b's
print("1:", re.fullmatch(r'ab*', 'abbb'))

# 2. Match 'a' followed by two to three 'b's
print("2:", re.fullmatch(r'ab{2,3}', 'abbb'))

# 3. Sequences of lowercase letters joined with an underscore
print("3:", re.findall(r'[a-z]+_[a-z]+', 'this_is a_test_example'))

# 4. One uppercase letter followed by lowercase letters
print("4:", re.findall(r'[A-Z][a-z]+', 'This Is A Test'))

# 5. 'a' followed by anything, ending in 'b'
print("5:", re.fullmatch(r'a.*b', 'axxb'))

# 6. Replace space, comma, or dot with colon
print("6:", re.sub(r'[ ,.]', ':', 'apple, banana. orange'))

# 7. Convert snake_case to camelCase
def to_camel(s):
    parts = s.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])
print("7:", to_camel('snake_case_example'))

# 8. Split string at uppercase letters
print("8:", re.findall(r'[A-Z][^A-Z]*', 'SplitAtUpperCase'))

# 9. Insert spaces between words starting with capital letters
print("9:", re.sub(r'([a-z])([A-Z])', r'\1 \2', 'InsertSpaceHere'))

# 10. Convert camelCase to snake_case
print("10:", re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', 'camelCaseToSnake').lower())
