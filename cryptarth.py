import itertools
def get_value(word, substitution):
    s = 0
    factor = 1
    for letter in reversed(word):
        s += factor * substitution[letter]
        factor *= 10
    return s
def solve2(equation):
    left, right = equation.replace(' ', '').split('=')
    left = left.split('+')
    letters = set(right)
    for word in left:
        for letter in word:
            letters.add(letter)
    letters = list(letters)

    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))

        if sum(get_value(word, sol) for word in left) == get_value(right, sol):
            print(' + '.join(str(get_value(word, sol)) for word in left) + " = {} (WORD : DIGIT {})".format(get_value(right, sol), sol))

a = str(input("ENTER THE FIRST WORD : "))
b = str(input("ENTER THE SECOND WORD : "))
c = str(input("ENTER THE THIRD WORD : "))
solve2(a + '+' + b + '=' + c)