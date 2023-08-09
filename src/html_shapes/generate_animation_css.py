HEX_COLORS = {"Purple": "#ab9df2",
              "Blue": "#78dce8",
              "Green": "#a9dc76",
              "Red": "#ff6188",
              "Orange": "#fc9867",
              "Yellow": "#ffd866"}

TEMPLATE = """
@keyframes blink_{name}_10_60 {{
    0%  {{background-color: #2c292d;}}
    10% {{background-color:{hex};}}
    30% {{background-color:{hex};}}
    60% {{background-color: #2c292d;}}
}}

@keyframes blink_{name}_30_80 {{
    0%  {{background-color: #2c292d;}}
    30% {{background-color:{hex};}}
    50% {{background-color:{hex};}}
    80% {{background-color: #2c292d;}}
}}

@keyframes fade_to_{name} {{
    0%  {{background-color: #2c292d;}}
    100% {{background-color:{hex};}}
}}
"""


def main():

    for item in HEX_COLORS.items():
        print(TEMPLATE.format(name=item[0],
                              hex=item[1]))


if __name__ == '__main__':
    main()
