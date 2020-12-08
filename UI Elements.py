import sys
import PyPDF2, traceback
from subprocess import call

try :
    src = sys.argv[1]
except :
    src = r"Alice's_Adventures_in_Wonderland_by_Lewis_Carroll.pdf"

input1 = PyPDF2.PdfFileReader(open(src, "rb"))
nPages = input1.getNumPages()
'''
#code to create thumbnail of pdf pages

loc ='D:/Games/nf/'
for i in range(nPages) :
    # generate the thumbnail
    cmd = 'convert ' + src + '[' + str(i) + ']' + 'D:/Games/nf/thumbnail.png'
    call(cmd, shell=True)
'''
cmd = '''magick convert "Alice's_Adventures_in_Wonderland_by_Lewis_Carroll.pdf" "D:/Games/thumbnail.png" '''
call(cmd, shell=True)