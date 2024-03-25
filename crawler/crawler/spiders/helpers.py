from bs4 import BeautifulSoup
import hashlib
from datetime import datetime


def set_body(response, body_type):
    if body_type == 'news_and_dat_report':
        soup = BeautifulSoup(response.xpath("//div[contains(@class, 'content-column')]").get(), 'html.parser')
    elif body_type == 'job_offer':
        soup = BeautifulSoup(response.xpath("//div[contains(@class, 'jobDisplay')]").get(), 'html.parser')
    else:
        soup = BeautifulSoup(response.xpath("//div[contains(@class, 'main-content')]").get(), 'html.parser')
    text = soup.get_text(separator=' ', strip=True)
    return text


def set_site_html(response):
    # soup = BeautifulSoup(response.xpath('//html').get(), 'html.parser')
    # for trash in soup(['script', 'style', 'svg', 'img']):
    #     trash.decompose()
    # return str(soup)
    return response.text


def hash_body(body):
    hasher = hashlib.new('sha256')
    hasher.update(body.encode('utf-8'))
    return hasher.hexdigest()


def parse_to_db_datetime(value):
    datetime_format = "%a %b %d %H:%M:%S UTC %Y"
    parsed_date = datetime.strptime(value, datetime_format).date()
    return parsed_date
