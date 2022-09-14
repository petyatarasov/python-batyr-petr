DIVIDER = "."

def get_filename(filename):
    parts = filename.split(DIVIDER)
    return parts[0]

if __name__ == "__main__":
    filename = "hello.jpg"
    result = get_filename(filename)
    print(result)

name = 'Shaya'
print('hi, ' + name.upper() + '!')  # hi, SHAYA!

text = 'Never forget what you are, for surely the world will not'

# BEGIN (write your solution here)
print(f"Index Of N: {text.find('N')}\nIndex Of ,: {text.find(',')}")
# END

text = 'When \t\n you play a \t\n game of thrones you win or you die.'

# BEGIN (write your solution here)
print(len(text[5:15].strip()))
# END
