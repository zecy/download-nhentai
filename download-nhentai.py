#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import re
import os
import string
import shutil
import pyperclip

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
            link = linkPre + comicId + '/' + str(i + 1) + '.' + imgType
            links.append(link)
        links_out = '\n'.join(links)
        pyperclip.copy(links_out)
        print('复制了 ' + count + ' 条网址到剪贴板')
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

if __name__ == '__main__':
    main()
