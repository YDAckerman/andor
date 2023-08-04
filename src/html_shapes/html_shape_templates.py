
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

BLANK_TEMPLATE = """
    min-height: {h}vw;
    min-width:  {w}vw;
    background-color: #2c292d;
    display: inline-block;
    """

SHAPE_TEMPLATES = {
    "circle": CIRCLE_BLINK_TEMPLATE,
    "square": SQUARE_BLINK_TEMPLATE,
    "blank": BLANK_TEMPLATE
}
