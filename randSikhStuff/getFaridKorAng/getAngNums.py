# importing required modules
import PyPDF2

# creating a pdf file object
pdfFileObj = open('./Fareedkot_Teeka.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

lst=[]

SGGSJIangNums=["pMnw "+ str(i+1) for i in range(1430)] 
for pdfPageInd in range(pdfReader.numPages):
    # creating a page object
    pageObj = pdfReader.getPage(pdfPageInd)
    # extracting text from page
    thePageText=pageObj.extractText()
    for ang in SGGSJIangNums:
        if ang in thePageText:
            lst.append(pdfPageInd)
            # print(ang,pdfPageInd)
            SGGSJIangNums.remove(ang)
            break
print(len(lst))

obj=open("./jsObj.js","w")
obj.write("const getTekaAng={\n")
for i in range(len(lst)):
    obj.write(f"{i+1}: {lst[i]+1},\n")
obj.write("}")

obj.close()
# closing the pdf file object
pdfFileObj.close()
