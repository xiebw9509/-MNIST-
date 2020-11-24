import numpy as np
import struct
import scipy.misc#目前scipy版本是1.1.0，如果版本过高会导致imsave无法调用，可以用pip方式更换版本
#一下路径都是绝对路径，可以自由替换
filename = 'C:/Users/Administrator/Desktop/data/train-images.idx3-ubyte'
filename1 = 'C:/Users/Administrator/Desktop/data/train-labels.idx1-ubyte'
def t10k(args):
    pass
#以二进制方式打开
binfile = open(filename,'rb')
lbinfile = open(filename1,'rb')
buf  = binfile.read()
lbuf = lbinfile.read()
index = 0
lind  = 0
magic, numImages, numRows, numColums = struct.unpack_from('>IIII',buf,index)#读取4个32 int
print (magic,' ',numImages,' ',numRows,' ',numColums  )
index += struct.calcsize('>IIII')
lmagic, numl = struct.unpack_from('>II',lbuf,lind)
print ('label')
print (lmagic,' ', numl)
lind += struct.calcsize('>II')
#输出的也是绝对路径
outputLabel='C:/Users/Administrator/Desktop/data/labels.txt'
fw=open(outputLabel,"w+")
outputImgDir='C:/Users/Administrator/Desktop/data/labels.txt'
for i in range(numl):
    im = struct.unpack_from('>784B',buf,index)
    index += struct.calcsize('>784B' )
    im = np.array(im)
    im = im.reshape(28,28)
    imgdir=outputImgDir+str(i)+'.jpg'
    scipy.misc.imsave(imgdir, im)
    tlabel=np.array((struct.unpack_from('>1B',lbuf,lind)))[0]
    fw.write(str(tlabel)+"\n")
    lind+=struct.calcsize('>1B')
fw.close()
binfile.close()
lbinfile.close()
