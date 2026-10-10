"""
Common utility functions for IELTS 1000 Contextual Articles.
Extracts vocabulary pairs from narrative text and formats output.
"""

import re
try:
    from src.vocab_db import lookup_vocab
except ImportError:
    from vocab_db import lookup_vocab


def extract_vocab_from_text(text):
    """
    Finds all patterns of: Turkish_word (english_word)
    Returns a deduplicated list of vocab dictionaries.
    """
    pattern = r'(\b[\wçğıöşüÇĞİÖŞÜ\-]+)\s*\(([a-zA-Z\s\-\'/]+)\)'
    matches = re.findall(pattern, text)
    seen = set()
    vocab_list = []
    
    for tr_token, en_word in matches:
        clean_en = en_word.strip()
        if clean_en.lower() in seen:
            continue
        seen.add(clean_en.lower())
        
        info = lookup_vocab(clean_en, tr_fallback=tr_token)
        vocab_list.append(info)
        
    return vocab_list

def format_markdown_article(art):
    """Formats a single article into high-quality GitHub markdown."""
    vocab_lines = "\n".join([f"> - **{v['word']}**: {v['tr']} *({v['pos']})*" for v in art['vocab']])
    return f"""### Makale {art['id']}: {art['title_tr']} | {art['title_en']} [{art['level']} - {art['category']}]

{art['text']}

> **Hedef Kelimeler (Target Vocabulary):**
{vocab_lines}
"""

def format_typst_article(art, accent_color="#2563eb"):
    """Formats a single article into Typst syntax with colored parenthetical words."""
    # Convert (word) to styled text in Typst
    text = art['text']
    
    # Escape Typst special characters: \ # $ @ < >
    for c in ['\\', '#', '$', '@', '<', '>']:
        text = text.replace(c, '\\' + c)
        
    # Replace (english_word) with bold colored text
    def repl(m):
        w = m.group(1)
        return f'#text(fill: rgb("{accent_color}"), weight: "bold")[({w})]'
    
    formatted_text = re.sub(r'\(([a-zA-Z\s\-\'/]+)\)', repl, text)
    
    vocab_items = " | ".join([f"• *{v['word']}*: {v['tr']} ({v['pos']})" for v in art['vocab']])
    
    return f'''
== Makale {art['id']}: {art['title_tr']} #text(size: 8.5pt, fill: rgb("{accent_color}"))[[{art['level']} • {art['category']}]]
#text(size: 8.5pt, fill: rgb("#64748b"), style: "italic")[{art['title_en']}]

{formatted_text}

#block(
  fill: rgb("#f8fafc"),
  inset: (x: 8pt, y: 6pt),
  radius: 3pt,
  stroke: 0.5pt + rgb("#e2e8f0"),
  width: 100%,
  [
    #text(size: 7.5pt, weight: "bold", fill: rgb("#334155"))[Hedef Kelimeler (Target Vocabulary):] \\
    #text(size: 7.5pt, fill: rgb("#475569"))[{vocab_items}]
  ]
)
#v(0.2cm)
'''
