def count_vowels(s):
    vowels = "aeiouAEIO"
    return sum(1 for char in s if char in vowels)
print(count_vowels("hello"))