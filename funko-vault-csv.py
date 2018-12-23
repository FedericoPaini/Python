#!/usr/bin/env python
#
# this script will parse all items from the pop vault (http://funko.com/collections/pop/the-vault)
# and save to a csv file. this script will need to be updated as new vault items are added if they
# do not conform to the normal or special patterns (see: special_patterns). comment on this gist
# with an item that does not export properly and i will add a condition for it.
#
# @requires lxml.html and requests
# @author Josh Kastang (josh[dot]kastang[at]gmail[dot]com)
# @tested Python 2.7, but should work with Python 2.6 as well.
#

import re
import sys
import csv
import requests
import lxml.html
from pprint import pprint

# vaulted items list
vaulted_items = []

page_number = 1
while True:
    print ("Processing page {0}...".format(page_number))

    tree = lxml.html.parse('{0}'.format(page_number))

    # loop through all items on the page and parse the item names
    items = tree.xpath('//div[contains(@class, "product-item")]/div[@class="caption"]/p/a')
    for item in items:

        # sanatize the names, only allow ascii characters
        item_name = item.text.encode('utf-8').strip()
        item_name = re.sub(r'[^\x00-\x7F]+',' ', item_name) # non-unicode is the bane of my existance

        # attempt to split the series
        item_name = item_name.split(':', 1)
        if len(item_name) == 1:
            item_name = item_name[0].split('-', 1)

        # attempt to split the sub-series (if available) and the name of the pop
        # there are some exceptions here (and will likely be more as additional)
        # pops are vaulted because of expected hyphens or other human error when
        # the pops were added to the vault.
        special_patterns = []
        special_patterns.append('(X-Men)\s?\-\s?(.+$)')
        special_patterns.append('(Hanna\-Barbera)\s?\-\s?(.+$)')
        special_patterns.append('(Dark Knight Movie)\s?(.+$)')
        special_patterns.append('(Amazing Spider\-Man Movie 2)\s?\-\s?(.+$)')
        special_patterns.append('(Rudolph the Red-Nosed Reindeer)\s?\-\s?(.+$)')
        special_patterns.append('(Beavis and Butt-head)\s?\:\s?(.+$)')
        special_patterns.append('(Teenage Mutant Ninja Turtles)\s+(.+$)')

        # attempt to split the sub-series and pop name
        item_details = []
        match_found = False
        for sp in special_patterns:
            match = re.search(sp, item_name[1], re.IGNORECASE)
            if match:
                item_details.append(match.group(1))
                item_details.append(match.group(2))
                match_found = True

        if not match_found:
            item_details = item_name[1].split('-', 1)

        # add the series, subseries, and character to a dict that
        # is added to the vaulted_items list which will be exported
        # to a csv
        series = item_name[0]
        subseries = 'N/A'
        character = None
        if len(item_details) == 2:
            subseries, character = item_details
        else:
            character = item_details[0]

        vaulted_item = {
            'series' : series.strip(),
            'subseries' : subseries.strip(),
            'character' : character.strip()
        }

        vaulted_items.append(vaulted_item)

    # next page
    try:
        next_page_url = tree.xpath('//li[@class="arrow right"]/a/@href')[0]
        next_page_num = re.search('\d+$', next_page_url)
        if(next_page_num):
            page_number = next_page_num.group(0)
    except IndexError:
        print ("Cannot determine next page. This normally means the last page has been reached")
        break

# write the csv
print ("Writing CSV...")
with open('funko-vaulted-pops.csv', 'w') as cf:
    fields  = ['series', 'subseries', 'character']
    cw      = csv.DictWriter(cf, fieldnames = fields)
    cw.writeheader()
    for row in vaulted_items:
        cw.writerow(row)

print ("Done")