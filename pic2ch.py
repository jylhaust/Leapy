#encoding:utf-8
from PIL import Image
import argparse
#-------------------------------------------------------
ascchar='''@#$%&?*aeoc=<{[(/l|!-_:;,."'^~` '''
count = len(ascchar)
def get_char(Imagefile):
    Imagefile=Imagefile.convert("L")#转灰度
    asd=''
    for h in range(Imagefile.size[1]):
        for w in range(Imagefile.size[0]):
            grayImg=Imagefile.getpixel((w,h))
            asd+=ascchar[int(grayImg/(256/(count)))]
        asd+='\r\n'
    return asd

if __name__== '__main__':

  Imagefile = Image.open("dola.png")
  Imagefile = Imagefile.resize((int(Imagefile.size[0]*0.8),int(Imagefile.size[1])))
  print u'Info:',Imagefile.size[0],' ',Imagefile.size[1],' ',count

  with open('tmp.txt','w')  as f:
      f.write(get_char(Imagefile))
#  tmp=open('tmp1.txt','w')
#  tmp.write(get_char(Imagefile))
#  tmp.close()