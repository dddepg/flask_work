from docxtpl import DocxTemplate

doc = DocxTemplate("static/my_word_template.docx")
context = { 'living' : ''}
doc.render(context)
doc.save("resultDocx/generated_doc.docx")