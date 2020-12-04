# -MINST-
提取训练集的60000张图片（jpg）
一.数据集名称为（以下4个）：
train-images-idx3-ubyte: training set images
train-labels-idx1-ubyte: training set labels
t10k-images-idx3-ubyte:  test set images
t10k-labels-idx1-ubyte:  test set labels 
使用前需要解压，放在同一个文件夹内
数据集地址：http://yann.lecun.com/exdb/mnist/

二.代码中scipy库的版本为1.1.0，如果版本过高可以使用（pip install scipy==1.1.0）更换。如果有权限问题在install后面加一个--user可以解决。
三.images（图片）文件夹是提取后的70张格式为jpg的图片，一共60000张，上传不方便，只供参考。
四.labels.txt文件是对应图片的分类标签。
