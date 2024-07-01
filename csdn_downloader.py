import re
import parsel
import tomd
import requests
import sys

def spider_csdn(title_url):
    if not title_url:
        print("错误：请输入网址")
        return
    head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52"
    }
    html=requests.get(url=title_url,headers=head).text
    page=parsel.Selector(html)
    # 创建解释器
    title=page.css(".title-article::text").get()
    if not title:
        print("错误：未找到文章标题")
        return
    res = re.compile("[^\u4e00-\u9fa5^a-z^A-Z^0-9]")
    restr = ''
    title = res.sub(restr, title)
    content=page.css("article").get()
    if not content:
        print("错误：未找到文章内容")
        return
    content=re.sub("<a.*?a>","",content)
    content = re.sub("<br>", "", content)
    texts=tomd.Tomd(content).markdown
    # 转换为markdown 文件
    with open(title+".md",mode="w",encoding="utf-8") as f:
        f.write("# " + title + "\n")
        f.write(texts)
    print(f"文章已保存为 {title}.md")

if __name__ == '__main__':
    while True:
        title_url = input("请输入需要获取文章的CSDN链接（或输入 'exit' 退出）：")
        if title_url.lower() == 'exit':
            break
        spider_csdn(title_url)