from docx import Document
from docx.enum.style import WD_STYLE_TYPE

doc=Document('new.docx')
p=doc.add_paragraph()

'''for style in doc.styles:
    if style.type==WD_STYLE_TYPE.TABLE:
        print(style.name)
'''
