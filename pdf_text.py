# import fitz

# pdf_file = "Tanvi_Rupareliya's __Resume (2).pdf"
# pdf_document = fitz.open(pdf_file)

# text = ""
# for page in pdf_document:
#     text += page.get_text()

# print(text)
# pdf_document.close()

# from pdfminer. import extract_pages
# from pdfminer.layout import LTTextContainer, LTChar, LTFigure

# def extract_text_with_formatting(pdf_path):
#     extracted_text = ""

#     for page_layout in extract_pages(pdf_path):
#         for element in page_layout:
#             if isinstance(element, LTTextContainer):
#                 for text_line in element:
#                     for character in text_line:
#                         if isinstance(character, LTChar):
#                             extracted_text += character.get_text()
#                     if not isinstance(text_line.next, (LTTextContainer, LTFigure)):
#                         extracted_text += "\n"

#     return extracted_text

# text = extract_text_with_formatting("/home/dhruv/Desktop/pdftotext/Hiral's Resume (1).pdf")
# print(text)