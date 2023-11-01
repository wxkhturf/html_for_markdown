import re
import os
import shutil
import urllib.request


def Pic_rename(line, pic_name, head_path):
    img_url = re.findall("\(.*\)", line)[0][1:-1]
    file_suffix = os.path.splitext(img_url)[1]
    new_path = head_path + pic_name + file_suffix
    tmp = '![' + pic_name + ']' + '(' + new_path + ')'
    new_line = re.sub("!\[.*\]\(.*\)", tmp, line)
    #print(new_name)
    #print(img_url)
    return (new_line, img_url)

def Save_img(img_url, source_file, file_path):
    #https://blog.csdn.net/weixin_45798684/article/details/105497137
    #获得图片后缀
    file_suffix = os.path.splitext(img_url)[1]
    #拼接图片名（包含路径）
    #filename = '{}{}{}{}'.format(file_path,os.sep,source_file,file_suffix)
    filename = '{}{}{}{}'.format(file_path, '/', source_file, file_suffix)
    #下载图片，并保存到文件夹中
    urllib.request.urlretrieve(img_url,filename=filename)

def Sharp_process(line, diff_level, level, sharp_header):
    old_level         = level
    old_sharp_header  = sharp_header

    header_flag       = re.match("^\s*#+ +", line)
    str_sharp         = header_flag[0]
    str_sharp_core    = re.sub(" ", "", str_sharp)
    level             = diff_level + len(str_sharp_core)

    if(old_level == level):
        tmp          = str( int(old_sharp_header[-1]) + 1)
        sharp_header = old_sharp_header[:-1] + tmp
    elif(old_level > level):
        tmp          = 2*(level - old_level)
        sharp_header = old_sharp_header[:tmp-1]
        last_str     = str(int(old_sharp_header[tmp-1]) + 1)
        sharp_header = sharp_header + last_str
    elif(old_level < level):
        sharp_header = old_sharp_header + '.1'


    new_sharp         = '#'*level + ' ' + sharp_header + ' '
    new_line          = re.sub(str_sharp, new_sharp, line)
    return (new_line, level, sharp_header)


def Markdown_detect(source_file, pic_num, name_mid, head_path, diff_level, sharp_header):
    with open(source_file, 'r', encoding='utf-8') as sf:
        target_file = "new_" + source_file
        with open(target_file, 'w', encoding='utf-8') as tf:
            diff_level   = diff_level
            level        = diff_level
            sharp_header = sharp_header
            for line in sf.readlines():
                #line = line.strip('\n')  #去掉列表中每一个元素的换行符
                pic_name   = str(pic_num) + '_' + name_mid
                img_flag   = re.match(".*!\[.*\]\(.*\).*", line)
                sharp_flag = re.match("^\s*#+ ", line)
                if(img_flag != None):
                    (new_line, img_url) = Pic_rename(line, pic_name, head_path)
                    Save_img(img_url, pic_name, head_path)
                    tf.write(new_line)
                    pic_num += 1
                elif(sharp_flag != None):
                    (new_line, level, sharp_header) = Sharp_process(line, diff_level, level, sharp_header)
                    tf.write(new_line)
                else:
                    tf.write(line)
            tf.close()
        sf.close()


if __name__ == "__main__":
    source_file = 'test.md'
    pic_num = 56
    name_mid = 'net'
    head_path = './roadmap/'
    diff_level = 3
    sharp_header = '5.1.1'
    if (os.path.exists(head_path)):
        shutil.rmtree(head_path)
    os.mkdir(head_path)
    Markdown_detect(source_file, pic_num, name_mid, head_path, diff_level, sharp_header)
