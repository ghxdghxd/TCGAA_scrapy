# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TcgaaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    patient_id = scrapy.Field()
    cancer_type = scrapy.Field()
    self_reported_race = scrapy.Field()
    self_reported_ethnicity = scrapy.Field()
    eigenstrat = scrapy.Field()
