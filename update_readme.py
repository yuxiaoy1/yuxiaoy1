# -*- coding: utf-8 -*-
"""
    :author: yuxiaoy
    :url: https://github.com/Yuxiaoy1
    :copyright: © 2020 yuxiaoy <1032897296@qq.com>
    :license: MIT, see LICENSE for more details.
"""

import requests
import sys

bing_base_url = "https://cn.bing.com/"

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
             (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Connection': 'close'
}


def fetch_img():
    """
    return image url, image copyright and copyright link.
    """
    res = requests.get(bing_base_url +
                       "HPImageArchive.aspx?format=js&idx=0&n=1",
                       headers=headers)
    res.encoding = "utf-8"
    res_data = res.json().get('images')[0]

    img_url = bing_base_url + res_data.get('url')
    img_copyright = res_data.get('copyright')
    img_copyright_link = res_data.get('copyrightlink')
    return img_url, img_copyright, img_copyright_link


img_url, img_copyright, img_copyright_link = fetch_img()

new_read_me = f"""
![{img_copyright}]({img_url})

*[{img_copyright}]({img_copyright_link})*
"""


def update_readme():
    """
    update readme file with latest image.
    """
    with open("README.md", "rb") as f:
        cur_read_me = f.read().decode("utf-8")
        if img_copyright in cur_read_me:
            print("POTD is just the same with yesterday, have a nice day :)")
            sys.exit()

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_read_me)


update_readme()
