import fitz


def extract_text_from_pdf(pdf_path):

    document = fitz.open(pdf_path)

    full_text = ""

    for page in document:

        text = page.get_text()

        full_text += text + "\n"

    return full_text