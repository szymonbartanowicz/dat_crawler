#!/bin/bash
cd crawler
#scrapy crawl dat -o ../data/dat.jsonl
scrapy crawl career_dat -o ../data/career_dat.jsonl
#TODO
#scrapy crawl barometer_dat -o barometer_dat.jsonl
#scrapy crawl top100_dat -o top100_dat.jsonl
