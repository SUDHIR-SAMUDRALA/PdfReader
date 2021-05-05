import PyPDF2

pdfFileObj = open("TwinkleComplete", "rb")

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

mytext = ""

for pageNum in range(pdfReader.numPages):
	pageObj = pdfReader.getPage(pageNum)

	mytext += pageObj.extractText()

pdfFileObj.close()

print(mytext)
