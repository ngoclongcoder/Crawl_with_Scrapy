import requests
import scrapy
from scrapy.http import Request
import os
import scrapy

import json


class Crawl(scrapy.Spider):
    start_urls = ['https://dav.gov.vn']
    name = "drug"
    headers = {
        "accept": "*/*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "content-type": "application/json",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"105\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"105\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-csrf-token": "x5QVBx45-eNqqBU5TThzMS85b4FJfY5Z67Pw",
        "cookie": "cf_chl_2=06d1f7a6cfeb2b1; cf_chl_prog=x15; cf_clearance=HbcESmswj3STAru.rnighD5taOb1WmtPpdiS741bssI-1663918527-0-250; _csrf=EHokb9_ak8apUmSMr0SbYM6Q; ConstructorioID_client_id=054ac361-c911-4db0-831c-a116e19561f7; ConstructorioID_session_id=1; _scid=4db1e1a2-f838-438b-8077-2c78f3b90f3d; _gcl_au=1.1.1639553116.1663918530; IR_gbd=flightclub.com; _gid=GA1.2.1343616897.1663918531; _sctr=1|1663866000000; __cf_bm=N_LTN.Xyu.tvdcRjxn_IHho8O471WLyiir2doDjn43U-1663919603-0-AeVANhX2hKdd9M2IFQ6Fw7SP2R2AiPnpU6NKRzDJzBPPsOOvJ6IjN1SIIqw18u1bVb5nPPbC93HFATe6M4BDIXw=; _gat_mpgaTracker1=1; _ga_GMJ0RMZHDX=GS1.1.1663918530.1.1.1663919641.0.0.0; _ga=GA1.1.1014569429.1663918531; IR_12612=1663919641964%7C0%7C1663919641964%7C%7C; ConstructorioID_session={\"sessionId\":1,\"lastTime\":1663919657436}; _xsrf=x5QVBx45-eNqqBU5TThzMS85b4FJfY5Z67Pw; OptanonConsent=isIABGlobal=false&datestamp=Fri+Sep+23+2022+14%3A54%3A17+GMT%2B0700+(Gi%E1%BB%9D+%C4%90%C3%B4ng+D%C6%B0%C6%A1ng)&version=6.14.0&hosts=&consentId=cb548e20-a594-46b3-88a6-bd4a7910b8b5&interactionCount=1&landingPath=https%3A%2F%2Fwww.flightclub.com%2Fcatalogsearch%2Fresult%3Fquery%3DYEEZY%2520SLIDES&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }


    def parse(self, response):
        # for page in range(1, 3):
        #     print("Page", page)
        #     link = f'https://danasilk.en.alibaba.com/productgrouplist-916210345-{page}/110_245cm.html?spm=a2700.shop_plgr.98.6'
        # link = f'https://dewangfangzhi.en.alibaba.com/search/product?SearchText=poncho'
        # yield scrapy.Request(link, headers=self.headers, callback=self.process_page)

        for page in range(1, 244):
            link = f'https://dav.gov.vn/tra-cuu-thuoc-page{page}.html'
            yield scrapy.Request(link, headers=self.headers, callback=self.saveFile)

    # def process_page(self, response):
    #     links = response.xpath(
    #         "//div[@class='icbu-product-card vertical large product-item']/a/@href").extract()
    #     for link in links:
    #         yield scrapy.Request((f'https://{link}'), callback=self.saveFile)

    def saveFile(self, response):

        titles = response.xpath("//table[@class='table table-bordered']/tbody/tr/td[4]/text()").extract()
        for i in titles:
            yield {
                "Title": i,
            }
