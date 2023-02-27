import md_rules as rules

def transform(md: str):
    """Transform a mardown line to a html line"""
    for rule in rules:
        md = rule["regex"].sub(rule["replace"], md)
    