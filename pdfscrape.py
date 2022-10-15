import PyPDF2
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

pdfFile= open("Meditations_Cottingham.pdf","rb")

pdfReader = PyPDF2.PdfFileReader(pdfFile)

num_pages = pdfReader.numPages

count = 0
text=""

while count<num_pages:
    page = pdfReader.getPage(count)
    count +=1
    text += page.extractText()


#This if statement exists to check if the above library returned words. It's done because PyPDF2 cannot read scanned files.
if text != "":
   text = text

#If the above returns as False, we run the OCR library textract to #convert scanned/image based PDF files into text.
else:
   text = textract.process(fileurl, method='tesseract', language='eng')   



pdfFile.close()

textfile = open("textfile.txt",'w')
print(text)

textfile.write(text)