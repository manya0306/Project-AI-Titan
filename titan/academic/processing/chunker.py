import re

def chunk_text(text, max_chars=800):

    sentences = re.split(r'(?<=[.!?])\s+', text)

    chunks = []
    current = ""

    for s in sentences:

        if len(current) + len(s) < max_chars:
            current += s + " "
        else:
            chunks.append(current.strip())
            current = s + " "

    if current:
        chunks.append(current.strip())

    return chunks