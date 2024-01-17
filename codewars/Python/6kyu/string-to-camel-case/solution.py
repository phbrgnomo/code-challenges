

def to_camel_case(text):
    chars = ["_", "-"]

    for _ in chars:
        i = text.find(_)

        # nc = text[i + 1 : i + 2]
        # text = text[:i] + '' + text[i +1:]
        text = text[:i + 1] + text[i + 1 : i + 2].upper() + text[i + 2:]
        print(text)

    text = text.replace('_', '')
    text.replace('-', '')
    
    return text

print(to_camel_case("the_stealth_warrior"))