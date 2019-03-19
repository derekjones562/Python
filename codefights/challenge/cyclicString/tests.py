from cyclicString import cyclicString

test_strings = {
"cabca": 3,
"aba": 2,
"ccccccccccc": 1,
"bcaba": 5,
"abacabaabacab": 7,
"aab": 3,
"abaaba": 3,
"zazazaza": 2,
"abbaab": 4,
"jjeiiloejjeii": 8,
}

for string, value in test_strings.items():
    length_of_cycle = cyclicString(string)
    if value != length_of_cycle:
        assert()
    print(".", end='')