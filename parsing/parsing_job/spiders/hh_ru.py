import scrapy
from scrapy.http import HtmlResponse
from parsing_job.items import ParsingJobItem


class HhRuSpider(scrapy.Spider):

    name = 'hh_ru'
    allowed_domains = ['hh.ru']
    start_urls = [
        'https://tomsk.hh.ru/search/vacancy?no_magic=true&L_save_area=true&text=web&excluded_text=&area=90&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=20'
    ]

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[@data-qa='pager-next']/@href").get()

        if next_page:
            yield response.follow(next_page, callback=self.parse)

        urls_vacancies = response.xpath("//div[@class='serp-item']//a[@data-qa='serp-item__title']/@href").getall()
        for url_vacancy in urls_vacancies:
            yield response.follow(url_vacancy, callback=self.vacancy_parse)

    def clean_salary(self, salary):
        min_salary = None
        max_salary = None
        currency_salary = None
        salary_note = None
        for i in range(len(salary) - 1):
            if salary[i] == 'от ':
                min_salary = int(salary[i + 1].replace('\xa0', ''))
            elif salary[i] == ' до ' or salary[i] == 'до ':
                max_salary = int(salary[i + 1].replace('\xa0', ''))
            elif salary[i] == '–':
                min_salary = int(salary[i - 1].replace('\xa0', ''))
                max_salary = int(salary[i + 1].replace('\xa0', ''))
        if len(salary) > 4:
            currency_salary = salary[-3]
            salary_note = salary[-1]

        return min_salary, max_salary, currency_salary, salary_note

    def vacancy_parse(self, response: HtmlResponse):
        vacancy_name = response.css("h1::text").get()
        vacancy_salary = response.xpath("//div[@data-qa='vacancy-salary']//text()").getall()
        vacancy_url = response.url
        min_salary, max_salary, currency_salary, salary_note = self.clean_salary(vacancy_salary)

        yield ParsingJobItem(
            name=vacancy_name,
            min_salary=min_salary,
            max_salary=max_salary,
            currency_salary=currency_salary,
            salary_note=salary_note,
            url=vacancy_url
        )
