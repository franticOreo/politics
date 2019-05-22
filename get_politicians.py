import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = "politicians"
    start_urls = [
        'https://www.aph.gov.au/Senators_and_Members/Parliamentarian_Search_Results?q=&mem=1&par=-1&gen=0&ps=0'
    ]


    # get all the links for xml documents
    def parse(self, response):
        # loop over the amount of politicans on page and get there names and respective parties
        count = 0
        for politician in response.xpath('//a[contains(@href, "/Senators_and_Members/Parliamentarian?")]/text()').getall():
            with open('politicians_and_parties', 'a') as f:
                f.write(json.dumps({
                'name': politician,
                'party': response.xpath('//dt[contains(text(), "Party")]/following-sibling::dd[1]/text()').getall()[count]
                }))
            count += 1

        next_page = response.xpath('//a[contains(@title, "Next page")]/@href').get()

        if next_page is not None:
            print('going to next page...')
            yield response.follow(next_page, callback=self.parse)







    # def get_xml(self, response):
    #     with open('hansard-xml', 'a') as f:
    #         f.write(str(response.xpath('/hansard').getall()))
