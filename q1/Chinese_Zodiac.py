import sys

ZODIAC_SIGNS = [
    "Rat (鼠 / Shǔ)",
    "Ox (牛 / Niú)",
    "Tiger (虎 / Hǔ)",
    "Rabbit (兔 / Tù)",
    "Dragon (龙 / Lóng)",
    "Snake (蛇 / Shé)",
    "Horse (马 / Mǎ)",
    "Goat (羊 / Yáng)",
    "Monkey (猴 / Hóu)",
    "Rooster (鸡 / Jī)",
    "Dog (狗 / Gǒu)",
    "Pig (猪 / Zhū)"
]

def main ():
# Ask for the birth year and make sure it's a valid integer

    try: 
        birth_year = int(input("Enter your birth year: "))
    except ValueError:

# Non-numeric input: show an error and exit the program
        print("Invalid input. Please enter a valid numerical year.")
        sys.exit()

    index = (birth_year - 1900) % 12
    zodiac_sign = ZODIAC_SIGNS[index]

#Display the result
    print(f"Your Chinese zodiac sign is: {zodiac_sign}")

if __name__ == "__main__":
        main()
