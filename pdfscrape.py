import PyPDF2
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


import pdfplumber
pdfFile= open("Meditations_Cottingham.pdf","rb")
def pdftotxt(filename):


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




from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar

def findboldedwords(filename):
    bolded_dictionary={}
    bolded_list=[]
    for page_layout in extract_pages(filename):
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                for text_line in element:
                    try:
                        for character in text_line:
                            if isinstance(character, LTChar):
                                if 'Bold' in character.fontname:
                                    weird_array =(str(text_line).strip().split("'"))
                                    boldword =weird_array[1]
                                    boldword= boldword[0:len(boldword)-3]

                                    if boldword not in bolded_list:
                                        bolded_list.append(boldword)
                                        pagey = str(page_layout)
                                        first = pagey.find("(")
                                        second = pagey.find(")")
                                        pagenumber= pagey[first + 1:second]
                                        bolded_dictionary[pagenumber]=boldword

                    except TypeError:
                        pass
    return bolded_list

#This function doesn't work properly (don't call)
#Should return a dictionary with the page number of bolded words
def boldedinpages(filename):
    bolded_dictionary={}
    prevbold=""
    boldedstring=""
    count=0
    for page_layout in extract_pages(filename):
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                for text_line in element:
                    try:
                        for character in text_line:
                            if isinstance(character, LTChar):
                                if 'Bold' in character.fontname:
                                    weird_array =(str(text_line).strip().split("'"))
                                    boldword =weird_array[1]
                                    boldword= boldword[0:len(boldword)-3]
                                    pagey = str(page_layout)
                                    first = pagey.find("(")
                                    second = pagey.find(")")
                                    pagenumber= pagey[first + 1:second]
                                    
                                    
                                    if boldword not in bolded_dictionary and count<10:
                                        bolded_dictionary[pagenumber]=boldword

                                        boldedstring = boldedstring +boldword
                                        
                                        print(boldedstring)
                                  
                                    
                                        
                    except TypeError:
                        pass
    return bolded_dictionary







textfile.write(text)