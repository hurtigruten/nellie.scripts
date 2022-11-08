import json
import contentful
import os
from urllib.request import urlopen, Request
from dotenv import load_dotenv
import csv

env_vars = load_dotenv()

CONTENTFUL_SPACE_ID = os.getenv('CONTENTFUL_SPACE_ID')
CONTENTFUL_CDN_KEY = os.getenv('CONTENTFUL_CDN_KEY_GLOBAL')
CONTENTFUL_ENVIRONMENT = os.getenv('CONTENTFUL_ENVIRONMENT')

locale = 'de-DE'

base_activity_url = 'https://www.hurtigruten.com/de-de/expeditions/zusaetzliche-angebote/katalog/'
base_cruise_url = 'https://www.hurtigruten.com/de-de/expeditions/reisen/'
base_destination_url = 'https://www.hurtigruten.com/de-de/expeditions/reiseziele/'

voyage_base_url_epi = 'https://www.hurtigruten.de/rest/b2b/voyages'
excursion_base_url_epi = 'https://www.hurtigruten.de/rest/b2b/excursions'
program_base_url_epi = 'https://www.hurtigruten.de/rest/b2b/programs'

redirected_types = ['PDP', 'Excursions', 'Pre-Post Programmes']


client = contentful.Client(
    CONTENTFUL_SPACE_ID, CONTENTFUL_CDN_KEY, 'cdn.contentful.com')
cf_voyages = client.entries({
    'content_type': 'voyage',
    'locale': locale,
    'select': 'sys.id,fields.slug,fields.bookable,fields.isPastOrCancelled,fields.destination',
    'include': 1,
    'limit': 900
}).items

cf_excursions = client.entries({
    'content_type': 'excursion',
    'locale': locale,
    'select': 'sys.id,fields.slug',
    'limit': 900
}).items

cf_programs = client.entries({
    'content_type': 'program',
    'locale': locale,
    'select': 'sys.id,fields.slug',
    'limit': 900
}).items

cf_activities = cf_excursions + cf_programs


def nellie_activity_url(id):
    for v in cf_activities:
        if (str(v.id) == str(id)):
            return base_activity_url + v.slug + '/'
    return base_activity_url


def nellie_voyage_url(id):
    for v in cf_voyages:
        if (str(v.id) == str(id)):
            if (v.fields(locale).get("bookable") and not v.fields(locale).get("isPastOrCancelled")):
                return base_cruise_url + v.slug + '/'
            return base_destination_url + v.fields(locale).get('destination')[0].fields(locale).get('slug') + '/'
    return ''


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'ZBrowser'
}

req = Request(voyage_base_url_epi, headers=headers)
res = urlopen(req).read()
epi_voyages_raw = json.loads(res.decode('utf-8'))

req = Request(excursion_base_url_epi, headers=headers)
res = urlopen(req).read()
epi_excursions_raw = json.loads(res.decode('utf-8'))

req = Request(program_base_url_epi, headers=headers)
res = urlopen(req).read()
epi_programs_raw = json.loads(res.decode('utf-8'))

epi_voyages = {}
epi_excursions = {}
epi_programs = {}

for e in epi_voyages_raw:
    epi_voyages[e["url"]] = e["id"]
for e in epi_excursions_raw:
    epi_excursions[e["url"]] = e["id"]
for e in epi_programs_raw:
    epi_programs[e["url"]] = e["id"]


with open('input.csv', 'r', encoding='UTF8', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    header = next(reader)
    header.append('Nellie URL')

    rows = []
    for row in reader:
        if (row[1] not in redirected_types):
            continue

        row_vid = epi_voyages.get(row[0])
        row_eid = epi_excursions.get(row[0])
        row_pid = epi_programs.get(row[0])

        if (row_vid):
            row.append(nellie_voyage_url(row_vid))
        elif (row_eid):
            row.append(nellie_activity_url(row_eid))
        elif (row_pid):
            row.append(nellie_activity_url(row_pid))
        else:
            row.append('  Not found in EPI overview.')
        rows.append(row)

with open('output.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)
