import PyPDF2

file=open('kurs-d.pdf','rb')
PdfReader=PyPDF2.PdfFileReader(file)
page1=PdfReader.getPage(0)
print(PdfReader.numPages)

pdfData=page1.extractText()
print(pdfData)


