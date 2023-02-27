import re, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

rules = [
    {
        "regex": re.compile(r"^(#{1,6})\s(.*)$"),
        "replace": lambda m: f"<h{len(m.group(1))}>{m.group(2)}</h{len(m.group(1))}>"
    },
    {
        "regex": re.compile(r"(\*\*|__)(.*?)\1"),
        "replace": lambda m: f"<strong>{m.group(2)}</strong>"
    },
    {
        "regex": re.compile(r"(\*|_)(.*?)\1"),
        "replace": lambda m: f"<em>{m.group(2)}</em>"
    },
    {
        "regex": re.compile(r"~~(.*?)~~"),
        "replace": lambda m: f"<del>{m.group(1)}</del>"
    },
    {
        "regex": re.compile(r"`(.*?)`"),
        "replace": lambda m: f"<code>{m.group(1)}</code>"
    },
    {
        "regex": re.compile(r"!\[(.*?)\]\((.*?)\)"),
        "replace": lambda m: f'<img src="{m.group(2)}" alt="{m.group(1)}">'
    },
    {
        "regex": re.compile(r"\[(.*?)\]\((.*?)\)"),
        "replace": lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>'
    },
    {
        "regex": re.compile(r"^(\d+)\.(.*)$"),
        "replace": lambda m: f"<ol><li>{m.group(2)}</li></ol>"
    },
    {
        "regex": re.compile(r"^- (.*)$"),
        "replace": lambda m: f"<ul><li>{m.group(1)}</li></ul>"
    },
    {
        "regex": re.compile(r"^((?:.|\n)*?)\n={3,}$"),
        "replace": lambda m: f"<h1>{m.group(1)}</h1>"
    },
    {
        "regex": re.compile(r"^((?:.|\n)*?)\n-{3,}$"),
        "replace": lambda m: f"<h2>{m.group(1)}</h2>"
    },
    {
        "regex": re.compile(r"^>\s(.*)$"),
        "replace": lambda m: f"<blockquote>{m.group(1)}</blockquote>"
    }
]

import re

def comment(md_line: str):
    
    pattern = r'^<!--(.+?)-->$'
    replace = r'<!--\1-->'
    flags = re.S
    return re.sub(pattern, replace, md_line, flags=flags)

def inline_code(md_line: str):
    
    pattern = r'`([^`]+)`'
    replace = r'<code>\1</code>'
    return re.sub(pattern, replace, md_line)


def block_code(md_line: str):
    """ ```python
        print("Hello World")
        ```
    """
    pattern = r'```(.+?)'
    replace = r'<pre><code>\1'
    flags = re.S
    return re.sub(pattern, replace, md_line, flags=flags)

def h1(md_line: str):
    
    pattern = r'^#\s(.+)$'
    replace = r'<h1>\1</h1>'
    flags = re.M
    return re.sub(pattern, replace, md_line, flags=flags)

def h2(md_line: str):
    
    pattern = r'^##\s(.+)$'
    replace = r'<h2>\1</h2>'
    flags = re.M
    return re.sub(pattern, replace, md_line, flags=flags)

def h3(md_line: str):
    
    pattern = r'^###\s(.+)$'
    replace = r'<h3>\1</h3>'
    flags = re.M
    return re.sub(pattern, replace, md_line, flags=flags)

def h4(md_line: str):
    
    pattern = r'^####\s(.+)$'
    replace = r'<h4>\1</h4>'
    flags = re.M
    return re.sub(pattern, replace, md_line, flags=flags)

def h5(md_line: str):
    
    pattern = r'^#####\s(.+)$'
    replace = r'<h5>\1</h5>'
    flags = re.M
    return re.sub(pattern, replace, md_line, flags=flags)

def h6(md_line: str):
    
    pattern = r'^######\s(.+)$'
    replace = r'<h6>\1</h6>'
    flags = re.M
    return re.sub(pattern, replace, md_line, flags=flags)

def headers(md_line: str):
    
    pattern = re.compile(r"^(#{1,6})\s(.*)$", re.M)
    return pattern.sub(lambda m: f"<h{len(m.group(1))}>{m.group(2)}</h{len(m.group(1))}>", md_line)
    
def bold(md_line: str):
    
    pattern = r'(\*\*|__)([^_]+)\1'
    replace = r'<strong>\2</strong>'
    return re.sub(pattern, replace, md_line)

def italic(md_line: str):
    
    pattern = r'(\*|_)([^_]+)\1'
    replace = r'<em>\2</em>'
    return re.sub(pattern, replace, md_line)

def unordered_list(md_line: str):
    
    pattern = r'^\*\s+(.+)$'
    replace = r'<ul><li>\1</li></ul>'
    flags = re.M
    return re.sub(pattern, replace, md_line, flags=flags)

def ordered_list(md_line: str):
    
    pattern = r'^\d+\.\s+(.+)$'
    replace = r'<ol><li>\1</li></ol>'
    flags = re.M
    return re.sub(pattern, replace, md_line, flags=flags)

def horizontal_rule(md_line: str):
    
    pattern = r'^[-*_]{3,}\n?$'
    replace = r'<hr />'
    flags = re.M
    return re.sub(pattern, replace, md_line, flags=flags)

def blockquote(md_line: str):
    
    pattern = r'^>\s?(.+)$'
    replace = r'<blockquote>\1</blockquote>'
    flags = re.M
    return re.sub(pattern, replace, md_line, flags=flags)

def link(md_line: str):
    
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    replace = r'<a href="\2">\1</a>'
    return re.sub(pattern, replace, md_line)

def image(md_line: str):
    
    pattern = r'!\[([^\]]+)\]\(([^)]+)\)'
    replace = r'<img src="\2" alt="\1" />'
    return re.sub(pattern, replace, md_line)

def paragraph(md_line: str):
    
    pattern = r'^([^<>\n].+)$'
    replace = r'<p>\1</p>'
    flags = re.M
    return re.sub(pattern, replace, md_line, flags=flags)

def element(md_line: str):
    
    pattern = r'^<([a-z]+)([^>]+)>(.+)</\1>$'
    replace = r'<\1\2>\3</\1>'
    return re.sub(pattern, replace, md_line)

def parse(md_line: str):
    
    for rule in RULES:
        md_line = rule(md_line)
    return md_line

def parse_file(file):
    html = ''
    with open(file, 'r') as f:
        for line in f:
            html += parse(line)
    return html

# determine les potentielles lignes qui peuvent être traitées en bloc
# exemple : les listes, les bloc de code, les tableaux, etc.
def block_lines(lines): 
    pass

def is_block_code(md_line: str):
    
    pattern = r'```(.+?)'
    flags = re.S
    return re.search(pattern, md_line, flags=flags)

RULES = [
    inline_code,
    headers,
    bold,
    italic,
    unordered_list,
    ordered_list,
    horizontal_rule,
    blockquote,
    link,
    image,
    paragraph,
    element,
]

    

if __name__ == '__main__':
    print(parse_file('test.md'))