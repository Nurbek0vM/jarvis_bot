from parsel import Selector
import requests


class NewScraper:
    URL = 'https://animespirit.tv/'
    LINK_XPATH = '//div[@class="custom-poster"]/a[@href]'

    def parse_date(self):
        html = requests.get(url=self.URL).text
        tree = Selector(text=html)
        links = tree.xpath(self.LINK_XPATH).getall()
        for link in links:
            selector = Selector(text=link)
            href_value = selector.css('a::attr(href)').get()
            print(href_value)

        return links


if __name__ == '__main__':
    scraper = NewScraper()
    scraper.parse_date()