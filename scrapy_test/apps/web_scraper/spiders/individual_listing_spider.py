from urlparse import urlparse
from scrapy_test.aggregates.listing_source.models import ListingSource
from scrapy_test.apps.web_scraper.spiders.individual_item_spider import IndividualItemSpider
from scrapy_test.apps.web_scraper.spiders.listing_spider import ListingSpider

class IndividualListingSpider(IndividualItemSpider, ListingSpider):
  name = 'individual_listing_spider'

  def __init__(self, *args, **kwargs):
    url = kwargs['id']

    #get the root domain - but this is pretty naive. consider
    #https://github.com/john-kurkowski/tldextract
    domain = urlparse(url).netloc.split(".")[1]

    config = ListingSource.objects.filter(url__icontains=domain)[:1].get().scraper_config

    #hack djangospider expects our config to have an id property
    config.id = config.pk
    self.scraper = config.scraper
    self.scrape_url = url
    self.ref_object = config

    super(IndividualListingSpider, self).__init__(*args, **kwargs)