# -*- coding: utf-8 -*-
import scrapy
from TCGAA.items import TcgaaItem



class TcgaaSpiderSpider(scrapy.Spider):
    #爬虫的名字
    name = 'tcgaa_spider'
    #允许的域名
    allowed_domains = ['52.25.87.215']

    cancer_list = ['BRCA', 'COAD', 'ESCA', "GBM", "KIRC", "LIHC", "LUAD", "OV", "PRAD", "STAD", "THCA", "UCEC", 
        'ACC', "BLCA", "CESC", "CHOL", "DLBC", "HNSC", "KICH", "KIRP", "LAML", "LGG","LUSC", "MESO", "PAAD",
        "PCPG", "READ", "SARC", "SKCM","TGCT","THYM","UCS","UVM"]

    #入口url
    start_urls = ['http://52.25.87.215/TCGAA/cancertype.php?cancertype=' + str(x) for x in cancer_list]

    def parse(self, response):
        # table_list = response.xpath('//div[@id="Content Box Content"]/div[6]/section/table[2]/tbody/tr')
        table_list = response.xpath(
            '//div[@id="Content Box Content"]//tr[@style="background-color: #D7DDDD; color: black; text-align: center; text-decoration: none; font-weight: bold; "]/parent::*/tr')
        # print(table_list)
        for t_item in table_list[1::2]:
            table_item = TcgaaItem()
            table_item['patient_id'] = t_item.xpath(".//td[1]//text()").extract_first()
            table_item['cancer_type'] = t_item.xpath(".//td[2]//text()").extract_first()
            table_item['self_reported_race'] = t_item.xpath(".//td[3]//text()").extract_first()
            table_item['self_reported_ethnicity'] = t_item.xpath(".//td[4]//text()").extract_first()
            table_item['eigenstrat'] = t_item.xpath(".//td[5]//text()").extract_first()
            # print(table_item)
            yield table_item

        next_links = response.xpath("//section//table[3]//td[2]//a/@href").extract()

        if len(next_links) == 2:
            next_link = next_links[0]
            if next_link.endswith("=1"):
                next_link = False
        else:
            next_link = next_links[2]

        if next_link:
            yield scrapy.Request("http://52.25.87.215/TCGAA/" + next_link, callback = self.parse)
