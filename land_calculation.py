# THis program calculates acres off of inputted square feet

ACRES = 43560


def main():
    feet = int(input('Please enter the square footage: '))
    total = feet / ACRES

    print(f'{total: .2f}')


if __name__ == '__main__':
    main()
