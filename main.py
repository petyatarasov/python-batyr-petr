DIVIDER = "."

def get_filename(filename):
    parts = filename.split(DIVIDER)
    return parts[0]

if __name__ == "__main__":
    filename = "hello.jpg"
    result = get_filename(filename)
    print(result)