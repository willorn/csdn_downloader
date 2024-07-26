# CSDN文章下载器

这是一个简单的Python脚本，用于下载CSDN博客文章并将其转换为Markdown格式。

## 功能

- 从CSDN文章URL爬取内容
- 提取文章标题和正文
- 将HTML内容转换为Markdown格式
- 保存文章为Markdown文件

## 依赖

本脚本依赖以下Python库：

- re
- parsel
- tomd
- requests

您可以使用以下命令安装依赖：

```
pip install parsel tomd requests
```

## 使用方法

1. 运行脚本：

```
python csdn_downloader.py
```

2. 在提示时输入CSDN文章的URL。

3. 脚本将下载文章并保存为Markdown文件，文件名为文章标题。

4. 重复步骤2-3下载更多文章，或输入'exit'退出程序。

## 注意事项

- 请确保您有权下载和使用所爬取的内容。
- 过度频繁的请求可能会导致您的IP被CSDN封禁。请合理使用本工具。
- 本脚本仅用于学习和个人使用，请勿用于商业目的。

## 贡献

欢迎提交问题和拉取请求。对于重大更改，请先开issue讨论您想要改变的内容。

## 许可

[MIT](https://choosealicense.com/licenses/mit/)
