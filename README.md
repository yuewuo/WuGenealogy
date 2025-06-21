# WuGenealogy 吴氏支谱
genealogy of Wu's family

## 简介

本项目展示以肆凡公为一世祖的吴氏支谱，为方便族人查询关系，可以使用网页内人名搜索功能快速定位到个人。

## 访问地址

项目将在以下两个地址永久有效：

- https://genealogy.wuyue98.cn （网页主体）
- https://github.com/yuewuo/WuGenealogy （代码仓库）

对于微信分享，可以使用如下图片：

<a href="https://genealogy.wuyue98.cn"><img style="width: 50%;" src="./qrcode.png"/></a>

## 可持续性

为了使族谱得以更新和传承，此项目托管在GitHub平台，过往更改均可在commit中查询，对于需要更新的内容（比如添加人员，修改错名，修改错误关系等），可以通过 Issues 功能提交，或者可以邮件联系维护人员。

## 维护人员

吴越（yue.wu@yale.edu）

## 维护指南

在 `./previous` 文件夹内下载最新的excel表格，修改后保存为新的文件，然后导出为csv格式（UTF-8编码），保存在本项目根目录的 `data.csv` 文件（覆盖旧文件）。

运行 `python3 ./parse_data.py` 解析csv文件（`./data.csv`）生成树型数据 `./data.json`。

打开 `./data.json` ，复制所有内容，打开 `./index.html` ，找到 `origin_data` 变量，并替换其后的JSON数据。

本地打开 `./index.html` ，检查更改是否生效，是否有明显问题。

