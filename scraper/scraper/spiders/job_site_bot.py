import scrapy


class JobSiteBotSpider(scrapy.Spider):
    name = 'job-site-bot'
    allowed_domains = ['sarkariresult.com']
    start_urls = ['https://www.sarkariresult.com/']

    def parse(self, response):
        for href in response.css("div a::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        text = response.css("div table:nth-child(1) tr:nth-child(1) td:nth-child(1)::text").extract()
        if len(text) > 0 and "Name of Post:" in text[0]:
            item = {}
            item["title"] = response.css("table table:nth-child(1) h1::text").extract_first()
            item['short_description'] = response.css(
                "table table:nth-child(1) tr:nth-child(4)>td:nth-child(2)::text").extract_first()

            imortant_dates = response.css(
                "table table:nth-child(3) tr:nth-child(2) td:nth-child(1)>ul li>b::text").extract()
            if len(imortant_dates) > 0:
                item['start_date_to_apply'] = imortant_dates[0]
            if len(imortant_dates) > 1:
                item['end_date_to_apply'] = imortant_dates[1]

            fees = response.css(
                "table table:nth-child(3) tr:nth-child(2) td:nth-child(2)>ul li>b::text").extract()
            if len(fees) > 2:
                item['general_application_fees'] = fees[0]
                item['sc_st_application_fees'] = fees[1]
                item['ph_application_fees'] = fees[2]

            age_limit = response.css(
                "table table:nth-child(3) tr:nth-child(3"
                ") b::text").extract()
            if len(age_limit) > 3:
                item['minimum_age'] = age_limit[2]
                item['maximum_age'] = age_limit[3]
                item['age_relaxation'] = "As per government rule"

            eligibility_and_exam_heading = response.css("table table:nth-child(3) tr:nth-child(5) td")
            i = 1
            for el in eligibility_and_exam_heading:
                if el.css('b::text').extract_first() == "Eligibility":
                    break
                i = i + 1

            eligibility_and_exam_row = response.css(
                "table table:nth-child(3) tr:nth-child(6) td:nth-child(" + str(i) + " ) ul li::text").extract()

            eligibility_and_exam = ''
            for elg in eligibility_and_exam_row:
                eligibility_and_exam = eligibility_and_exam + str(elg)

            item['eligibility'] = eligibility_and_exam

            item['is_goverment_job'] = True
            # item['unique_url_id'] = item["title"].replace(' ', "-").replace(",", "")
            # item.save()
            yield item
