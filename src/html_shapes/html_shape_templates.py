
CIRCLE_BLINK_TEMPLATE = """
    height: {h}vw;
    width:  {w}vw;
    background-color: #2c292d;
    border-radius: 50%;
    display: inline-block;
    animation-name: blink_{c}_{fd};
    animation-duration: {du}s;
    animation-delay: {de}s;
    animation-iteration-count: {n};
    /* animation-fill-mode: forwards;*/
    """

SQUARE_BLINK_TEMPLATE = """
    height: {h}vw;
    width:  {w}vw;
    background-color: #2c292d;
    display: inline-block;
    animation-name: blink_{c}_{fd};
    animation-duration: {du}s;
    animation-delay: {de}s;
    animation-iteration-count: {n};
    /* animation-fill-mode: forwards;*/
    """

CIRCLE_FIXED_TEMPLATE = """
    height: {h}vw;
    width:  {w}vw;
    background-color: #78dce8;
    border-radius: 50%;
    display: inline-block;
    """

SQUARE_FIXED_TEMPLATE = """
    height: {h}vw;
    width:  {w}vw;
    background-color: #78dce8;
    display: inline-block;
    """


BLANK_TEMPLATE = """
    height: {h}vw;
    width:  {w}vw;
    background-color: #2c292d;
    display: inline-block;
    """

SHAPE_TEMPLATES = {
    "circle_blink": CIRCLE_BLINK_TEMPLATE,
    "square_blink": SQUARE_BLINK_TEMPLATE,
    "circle_fixed": CIRCLE_FIXED_TEMPLATE,
    "square_fixed": SQUARE_FIXED_TEMPLATE,
    "blank": BLANK_TEMPLATE
}
