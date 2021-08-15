import scrapy
from scrapy.http import HtmlResponse
from vacancyparcer.items import VacancyparcerItem


class HhruSpider(scrapy.Spider):
    name = 'hhru'
    allowed_domains = ['hh.ru']
    start_urls = ['https://hh.ru/search/vacancy?clusters=true&ored_clusters=true&enable_snippets=true&salary='
                  '&st=searchVacancy&text=python']

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[@data-qa='pager-next']/@href").extract_first()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        links = response.xpath("//a[@data-qa='vacancy-serp__vacancy-title']/@href").extract()
        for link in links:
            yield response.follow(link, callback=self.vacancy_parse)

    def vacancy_parse(self, response: HtmlResponse):
        vac_name = response.xpath("//h1/text()").extract_first()
        salary_min = response.xpath("//p[@class='vacancy-salary']/span/text()").extract_first()
        salary_max = response.xpath("//p[@class='vacancy-salary']/span/text()").extract_first()
        salary_curr = response.xpath("//p[@class='vacancy-salary']/span/text()").extract_first()
        vac_url = response.url
        vac_cite = 'https://hh.ru/'
        yield VacancyparcerItem(name=vac_name, salary_min=salary_min, salary_max=salary_max,
                                salary_curr=salary_curr, cite=vac_cite, url=vac_url)
