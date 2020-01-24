import PyPDF2

pdfReader=PyPDF2.PdfFileReader('t1.pdf')

pdfWriter=PyPDF2.PdfFileWriter()

t3stream=open('t3.pdf','wb')

pdfWriter.appendPagesFromReader(pdfReader,print(pdfWriter.getNumPages()))

pdfWriter.write(t3stream)

t3stream.close()
