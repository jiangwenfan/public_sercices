import Parser from "@postlight/parser";
import fs from "fs";

class ParserHtmlContent {
  // 发送请求获取图片的字节数据
  async getImageData(url) {
    // 1.获取图片字节数据
  }

  // 格式化处理为标准格式内容
  formatResult(result) {
    // 1.获取 lead_image_url 的图片内容
    // 1.1 增加 lead_image_content 字段，存储图片字节数据
    // 1.2 移动 lead_image_url 到 backup 字段
  }

  // 从url获取html内容
  async fromUrl(url) {
    Parser.parse(url, { contentType: "html" }).then((result) => {
      // [test]保存到本地html文件
      const { content } = result;
      fs.writeFileSync("test_data/content.html", content);
    });
  }

  // 从html内容获取正文
  // 仍然提供 URL 参数，以便识别 Web 站点并使用其自定义解析器（如果有），尽管它不会用于获取内容。
  async fromHtmlContent(url, htmlContent) {
    Parser.parse(url, {
      html: htmlContent,
    }).then((result) => {
      console.log(result);
    });
  }
}

/*
lead_image_content: 封面图片链接，字节数据[base64编码]
title: 文字标题
date_published: 发布日期
excerpt: 摘要
content_text: 正文内容文本
content_array: 正文中所有图片字节内容数据[base64编码]


backup:{
  lead_image_url: 封面图片链接
  content: 正文html内容，包含图片img标签
}
meta:{
  author: 作者
  url: 原始url
  domain: 域名
  word_count: 字数
}
*/
