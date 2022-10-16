import PyPDF2
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import fitz # PyMuPDF
import io
from PIL import Image

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
    textfile=open("textfile.txt","w")
    textfile.write(text)
    textfile.close()




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
    bold_arr=[]

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

                                    boldarr
                                                    
                    except TypeError:
                        pass
    return bolded_dictionary

def extract_images(filename):
    pdf_file = fitz.open(filename)
    for page_index in range(len(pdf_file)):
    # get the page itself
        page = pdf_file[page_index]
        image_list = page.get_images()
        # printing number of images found in this page
        if image_list:
            print(f"[+] Found a total of {len(image_list)} images in page {page_index}")
        else:
            print("[!] No images found on page", page_index)
        for image_index, img in enumerate(page.get_images(), start=1):
            # get the XREF of the image
            xref = img[0]
            # extract the image bytes
            base_image = pdf_file.extract_image(xref)
            image_bytes = base_image["image"]
            # get the image extension
            image_ext = base_image["ext"]
            # load it to PIL
            image = Image.open(io.BytesIO(image_bytes))
            # save it to local disk
            image.save(open(f"image{page_index+1}_{image_index}.{image_ext}", "wb"))
    return image_index



