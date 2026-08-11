from pdf_parser import extract_text_from_pdf

text = extract_text_from_pdf("data/test_resume.pdf")
print(text)