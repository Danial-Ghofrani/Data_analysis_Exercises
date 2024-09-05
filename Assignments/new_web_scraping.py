import scrapy
from scrapy.crawler import CrawlerProcess
import csv
import datetime
start = datetime.datetime.now()
class NewsSpider(scrapy.Spider):
    name = "news_spider"
    custom_settings = {
        'DOWNLOAD_DELAY': 5,  # 5 seconds delay between requests
        'DOWNLOAD_TIMEOUT': 30,  # 30 seconds timeout for each request
        'RETRY_TIMES': 3,  # Retry failed requests up to 3 times
        'HTTPERROR_ALLOWED_CODES': [404, 500],  # Handle specific HTTP errors
    }

    def start_requests(self):
        base_url = 'https://www.sciencedaily.com/news/plants_animals/'
        groups = [
            'biology',
            'biotechnology',
            'behavior',
            'biochemistry',
            'botany',
            'cell_biology',
            'developmental_biology',
            'epigenetics',
            'evolution',
            'genetics',
            'marine_biology',
            'mating_and_breeding',
            'molecular_biology',
            'zoology',
            'bacteria',
            'fungus',
            'microbiology',
            'prions',
            'viruses'
        ]
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        for group in groups:
            url = f"{base_url}{group}/"
            yield scrapy.Request(url=url, headers=headers, callback=self.parse_front, meta={'group': group})

    def parse_front(self, response):
        group = response.meta['group']
        news_data = []
        news_titles = response.css('div.latest-head a::text').getall()
        news_links = response.css('div.latest-head a::attr(href)').getall()
        news_summaries = response.css('div.latest-summary::text').getall()
        news_dates = response.css('div.latest-summary span::text').getall()

        # Debug prints
        print(f"Processing group: {group}")
        print(f"Titles: {news_titles}")
        print(f"Links: {news_links}")
        print(f"Summaries: {news_summaries}")
        print(f"Dates: {news_dates}")

        for title, link, summary, date in zip(news_titles, news_links, news_summaries, news_dates):
            if title and link and summary and date:
                news_data.append([group, title.strip(), response.urljoin(link), summary.strip(), date.strip()])

        with open('news_data.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Group', 'Title', 'Link', 'Summary', 'Date'])
            writer.writerows(news_data)


process = CrawlerProcess()
process.crawl(NewsSpider)
process.start()

print(f' the operation took this amount of time:{datetime.datetime.now()-start}')
