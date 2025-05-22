#!/usr/bin/env python3
from datetime import datetime
from lunardate import LunarDate

def get_chinese_lunar_date():
    today = datetime.today()
    lunar = LunarDate.fromSolarDate(today.year, today.month, today.day)

    chinese_zodiacs = [
        "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake",
        "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"
    ]
    heavenly_stems = ['Jia', 'Yi', 'Bing', 'Ding', 'Wu', 'Ji', 'Geng', 'Xin', 'Ren', 'Gui']
    earthly_branches = ['Zi', 'Chou', 'Yin', 'Mao', 'Chen', 'Si', 'Wu', 'Wei', 'Shen', 'You', 'Xu', 'Hai']

    base_year = 1984  # Jia Zi (first of 60)
    offset = (lunar.year - base_year) % 60
    stem = heavenly_stems[offset % 10]
    branch = earthly_branches[offset % 12]
    zodiac = chinese_zodiacs[offset % 12]

    return f"{stem}-{branch} {zodiac}, {lunar.month}, {lunar.day}"

if __name__ == "__main__":
    print(get_chinese_lunar_date())

