# -*- coding: utf-8 -*-
# coding=utf-8
from scrapy import cmdline


def main(name):
    if name:
        cmdline.execute(name.split())


if __name__ == '__main__':
    print('begin main1')
    name = "scrapy crawl drug -O data/drug.csv"

    main(name)
    print('exit')
