# html_for_markdown

## 1 前言

因为每次复制网页为Markdown时，图片需要重新命名归档，标题的级别需要更改，故写了个脚本帮忙修改



## 2 环境

>运行：
>
>`prompt> python3 main.py`

windows 10

python 3.9.12 64-bit

```python
uri-template             1.2.0
urllib3                  2.0.2
```



## 3 参数

1. 将网页上的内容复制到`test.md`中，即参数`source_file`
2. 设置`pic_num`，该参数用于命名图片，比如图片依次命名为`56_net.png`、`57_net.png`等等，这里的`56`就是起始命名
3. 设置`name_mid`，比如图片名为`56_net.png`，这里的`net`即为`name_mid`
4. 设置路径`head_path`，首先需要确保是**相对路径**（<font size=5 color=gree>注：必须是相对路径</font>），其次必须确保该文件夹存在（即下例中的`roadmap`文件夹是存在的），最后还要确保首尾是`/`，即写成`./roadmap`或`roadmap/`是不行的，必须写成`./roadmap/`（本人就是想要兼容之前的格式）
5. 设置`diff_level`，这个是设置标题的级别差的。例如：从网页上拷贝过来的是一级标题，但是到markdown归档时，我想要他是4级标题，网页上的二级标题，我想要它是5级标题，以此类推，则应该设置`diff_level`为`3`（即4-1=3）
6. 设置`sharp_header`，这个是设置级别头的，上个参数`diff_level`已经设置了级别为3，所以这里应该设置为三级，如：`5.1.1`或`1.2.3`等

```bash
#main.py

...
...

if __name__ == "__main__":
    source_file = 'test.md'
    pic_num = 56
    name_mid = 'net'
    head_path = './roadmap/'
    diff_level = 3
    sharp_header = '5.1.1'
    Markdown_detect(source_file, pic_num, name_mid, head_path, diff_level, sharp_header)
```

