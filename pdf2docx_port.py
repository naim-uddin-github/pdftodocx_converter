# Importing the Converter() class
from pdf2docx import Converter

pdf = 'NAIM UDDIN_Resume.pdf'
docx = 'NAIM UDDIN_Resume.docx'

try:
    # Converting pdf to docx
    cv_obj = Converter(pdf)
    cv_obj.convert(docx)
    cv_obj.close()
except:
    # if try don't works
    print("Convertion Failed")
else:
    # if try works fine
    print("Convertion Done")