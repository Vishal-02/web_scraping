from explore.items import cover
from scrapy import Spider

class CoverSpider(Spider):
    name = "pyimagesearch-cover-spider"
    start_urls = ["https://time.com/section/us/"]

    def parse(self, response):
        # get the urls of all the images
        image_urls = response.xpath("//div[contains(@class, 'component image-new')]/div//img/@src").extract()

        # get all the titles for the corresponding images
        divs_for_titles = response.xpath("//div[contains(@class, 'taxonomy-tout')]").getall()
        titles = []
        
        for title in divs_for_titles:
            text = title.xpath(".//div[contains(@class, 'text')]/h2/text()").extract()
            titles.append(text)

        titles = [title.split("\n")[1].strip() for title in titles]

        # store in your data structure
        for i in range(len(image_urls)):
            yield cover(title=titles[i], file_urls=image_urls[i])

