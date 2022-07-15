import re

# TODO: Create phone regex.
dateRegex = re.compile(r'''(
    (0[1-9]|1[0-9]|2[0-9]|3[01])    # day
    /                           # sep
    (0[1-9]|1[012])             # month
    /                           # sep
    ([1-2][0-9]{3})             # year
    )''', re.VERBOSE)

text = "dates like 31/02/2020 or 31/04/2021. 01/12/1001 00/12/1001"

result = dateRegex.findall(text)
print('result: ', result)
