
CIRCLE_FIXED_TEMPLATE = """
    height: {h}{u};
    width:  {w}{u};
    background-color: {c};
    border-radius: 50%;
    display: inline-block;
    """

SQUARE_FIXED_TEMPLATE = """
    height: {h}{u};
    width:  {w}{u};
    background-color: {c};
    display: inline-block;
    """

EMPTY_TEMPLATE = """
    height: {h}{u};
    width:  {w}{u};
    opacity: 0.0;
    display: inline-block;
    """

SHAPE_TEMPLATES = {
    "circle_fixed": CIRCLE_FIXED_TEMPLATE,
    "square_fixed": SQUARE_FIXED_TEMPLATE,
    "empty": EMPTY_TEMPLATE,
}

# CIRCLE_BLINK_TEMPLATE = """
#     height: {h}vw;
#     width:  {w}vw;
#     background-color: #2c292d;
#     border-radius: 50%;
#     display: inline-block;
#     animation-name: blink_{c}_{fd};
#     animation-duration: {du}s;
#     animation-delay: {de}s;
#     animation-iteration-count: {n};
#     /* animation-fill-mode: forwards;*/
#     """

# SQUARE_BLINK_TEMPLATE = """
#     height: {h}vw;
#     width:  {w}vw;
#     background-color: #2c292d;
#     display: inline-block;
#     animation-name: blink_{c}_{fd};
#     animation-duration: {du}s;
#     animation-delay: {de}s;
#     animation-iteration-count: {n};
#     /* animation-fill-mode: forwards;*/
#     """
