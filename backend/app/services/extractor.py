import re


def extract_fields(text: str):
    return {
        "brand": text.split("\n")[0],
        "abv": re.findall(r"(\d+\.?\d*)%", text),
    }
