def convert(text):
    # Chain your .replace() calls here to swap :) and :(
    return text.replace(":)", "🙂").replace(":(", "🙁")


def main():
    # 1. Prompt user with input()
    # 2. Call convert()
    # 3. Print result
    ...
    print(convert(input()))


main()