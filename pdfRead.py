import PyPDF2

path = 'C:/Users/1310615/Documents/theartofbrassplaying/'
pdfFile = 'The_Art_of_Brass_Playing_by_Philip_Farkas_OCR.pdf'

# create a pdf file object
pdfFileObj = open(path+pdfFile, 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

with open(path+"TextFile.txt", "w",encoding="UTF-8") as text_file:
    for i in range(pdfReader.numPages):
        pdfText = pdfReader.getPage(i).extractText()
        print( pdfText, file=text_file)



# closing the pdf file object
pdfFileObj.close()



