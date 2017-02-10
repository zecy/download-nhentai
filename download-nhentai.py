#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import re
import os
import string
import shutil
import subprocess

def main():

    title = input('粘贴标题：')
    url   = input('粘贴连接：')
    count = input('输入页数：')

    if(re.search("nhentai", url)):
        pat     = re.compile(r"https://t.nhentai.net/galleries/(\d+)/\d+t.(jpg|png)")
        comicId = re.search(pat, url).group(1) 
        imgType = re.search(pat, url).group(2) 
        linkPre = "https://i.nhentai.net/galleries/"
        links   = []
        for i in range(int(count)):
            filename = str(i+1).rjust(len(str(count)), '0') + '.' + imgType
            link = linkPre + comicId + '/' + str(i + 1) + '.' + imgType + '\n out=' + filename + '\n'
            links.append(link)
    else:
        print('傻逼，网址不对！')
        return

    try:
        os.mkdir(title)
        os.chdir(title)
    except:
        shutil.rmtree(title)
        os.mkdir(title)
        os.chdir(title)

    f = open("list.txt", "w", encoding="utf-8")
    f.writelines(links)
    f.close()

    stdout = subprocess.call("aria2c --dir=. --input-file=list.txt --enable-rpc=false", shell=True)

    if(stdout == 0):
        os.remove("list.txt")
        print("共 " + count + " 页下载完成：" + title)
        os.chdir("cd " + title)
    else:
        print("FUCK！出错了！")
    

if __name__ == '__main__':
    main()
