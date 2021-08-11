import PyPDF2,os

pdfFileObj=open('BERT- Pre-training of Deep Bidirectional Transformers for Language Understanding.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(pdfFileObj)


with open('BERT- Pre-training of Deep Bidirectional Transformers for Language Understanding.txt','w') as f:
    for page_num in range (pdfReader.numPages):
        print('Page:{0}'.format(page_num))
        pageobj=pdfReader.getPage(page_num)

        try:
            txt=pageobj.extractText()
            print('',center(100,'-'))
        except:
            pass
        else:
            f.write("Page{0}\n".format(page_num+1))
            f.write(''.center(100,'-'))
            f.write(txt)
    f.close()
                    
# The txt file does not show text, and i don't know why. 

