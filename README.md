# PicNormalization

### 本脚本用于将不规则图片用白色填充为正方形图片

使用方法：

将脚本放置于存储有图片文件夹的一级目录下，运行

```
python picNormalize.py -f [输入目录名] -o [输出目录名] -s [输出文件大小]
```

脚本会将输入目录二级文件夹中图片输出到输出目录名下对应的文件夹

例如：

```
python picNormalize.py -f ./competotion -o ./img -s 128
```

