from PIL import ImageFont, Image, ImageDraw
from glob import glob
import argparse
from fontTools.ttLib.ttFont import TTFont
import os

parse = argparse.ArgumentParser(description="将ttf字体文件转为图片")
parse.add_argument('-f', required=True,help="输入文字位置")
parse.add_argument('-o', help="输出目录,默认为当前目录下imgs", default="imgs")
parse.add_argument('-s', required=True,type=int, help="输出图片的像素大小", default=512)

args = parse.parse_args()

def picNorm(path,out):
    img_path = glob(os.path.join(path,"*.png"))
    for idx,img in enumerate(img_path):
        im_back = Image.new("RGB",(args.s,args.s),(255, 255, 255))
        name = os.path.join(out,"%d.png"%(idx))
        im = Image.open(img)
        im.thumbnail((args.s,args.s))
        ori_w,ori_h = im.size
        if ori_w != args.s or ori_h != args.s:
            box = (0,0,ori_w,ori_h)
            reg = im.crop(box)
            im_back.paste(reg,((args.s - ori_w) // 2, (args.s - ori_h) // 2))
            im_back.save(name,'png')
        else:
            im.save(name,'png')

if __name__ == '__main__':
    for root,dirs,files in os.walk(args.f):
        for dir in dirs:
            print(dir)
            out = os.path.join(args.o,args.f,dir)
            os.makedirs(out, exist_ok=True)
            picNorm(args.f+"\\"+dir,out)