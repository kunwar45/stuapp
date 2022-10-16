import PyPDF2
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import fitz # PyMuPDF
import io
from PIL import Image
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar
from gtts import gTTS #pip install gTTS
import os

from pymongo_get_database import get_database
basicDB = get_database()
glossaryDB = basicDB["glossary"]
questionDB = basicDB["question"]

class Textbook:

    def __init__(self, textbookName, textbookFilePath):
        self.textbookName = textbookName
        self.textbookFilePath = textbookFilePath
        
        glossaryDB.insert_one(self.getGlossary(textbookFilePath))



    #Returns the entire PDF into a string
    def pdfToText(filepath):
        pdf = open(filepath,"rb")
        pdfReader = PyPDF2.PdfFileReader(pdf)

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
        """

        textfile=open("textfile.txt","w")
        textfile.write(text)
        textfile.close()
        """
        return text




    #Saves all the images of the pdf
    def picextract(self):
        pdf_file = fitz.open(self.textbook)
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
        pdf_file.close()


    #Returns a list of all bolded words in the PDF
    def getGlossary(filepath):
       
        bolded_list=[]
        for page_layout in extract_pages(filepath):
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
                                        if boldword+"*" not in bolded_list:
                                            bolded_list.append(boldword+"*")
                        except TypeError:
                            pass
        finalDict = {}
        for item in bolded_list:
            finalDict[item] = item
        return finalDict
    
    def tts(self):
        myobj = gTTS(text=self.pdfToTxt(), lang="en", slow=False)
        myobj.save("audio.mp3")
        os.system("audio.mp3")


phil = Textbook("SamplePDF.pdf")
#print (phil.textbook)
phil.tts()