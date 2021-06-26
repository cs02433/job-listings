from django.core.management.base import BaseCommand
from scraper.scraper.spiders.job_site_bot import JobSiteBotSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class Command(BaseCommand):
    help = "Release the spiders"

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())

        process.crawl(JobSiteBotSpider)
        process.start()
