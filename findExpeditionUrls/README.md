# Find expedition URLs

This script reads in a CSV file of format below:

```
Address,Section,Content Type,Status Code,GA Sessions,GA Goal Completions All,Clicks,Impressions,Position,Ahrefs Keywords - Exact,Ahrefs Keywords Top 3 - Exact,Ahrefs Keywords Top 10 - Exact
https://www.hurtigruten.de/alaska/,Campaigns,text/html; charset=utf-8,200,3657,7099,9,88,4,0,0,0
https://www.hurtigruten.de/app/,App / Tool / Function,text/html; charset=utf-8,200,1500,509,405,1567,7,0,0,0
https://www.hurtigruten.de/de/adobe-download/,App / Tool / Function,text/html; charset=utf-8,200,27,17,19,11817,13,2,0,1
https://www.hurtigruten.de/eine-reise-finden/,App / Tool / Function,text/html; charset=utf-8,200,43789,72839,2471,99279,4,9,5,6
https://www.hurtigruten.de/kataloge/,Catalogue,text/html; charset=utf-8,200,5951,2665,3699,38728,30,60,3,5
```

and maps the nellie cruises like so:

```
Address,Section,Content Type,Status Code,GA Sessions,GA Goal Completions All,Clicks,Impressions,Position,Ahrefs Keywords - Exact,Ahrefs Keywords Top 3 - Exact,Ahrefs Keywords Top 10 - Exact,Nellie URL
https://www.hurtigruten.de/ausfluege/,Excursions,text/html; charset=utf-8,200,24473,21237,8872,42298,17,29,5,6,  Not found in EPI overview.
https://www.hurtigruten.de/ausfluege/alaska/alert-bay-kulturelle-tanzdarbietung/,Excursions,text/html; charset=utf-8,200,5,8,0,84,25,0,0,0,https://www.hurtigruten.com/de-de/expeditions/zusaetzliche-angebote/katalog/alert-bay---kulturelle-tanzdarbietung/
https://www.hurtigruten.de/ausfluege/alaska/chignik-malerisches-chignik/,Excursions,text/html; charset=utf-8,200,5,3,2,209,9,0,0,0,https://www.hurtigruten.com/de-de/expeditions/zusaetzliche-angebote/katalog/malerisches-chignik/
https://www.hurtigruten.de/ausfluege/alaska/dutch-harbor-erkundung-der-stadt-mit-dem-hop-on-hop-off-shuttle/,Excursions,text/html; charset=utf-8,200,48,28,33,3405,10,2,1,2,https://www.hurtigruten.com/de-de/expeditions/zusaetzliche-angebote/katalog/dutch-harbor-hop-on-hop-off-shuttleservice/
```

Note that this is a python script. Dependency packages are managed via Pipfile. You will need to install pipenv in order to create the virtual environment to run this script:

```
brew install pipenv
```

Load dependecies into shell:

```
pipenv shell
```

Script is run like so:

```
python3 find-expedition-urls.py input.csv output.csv
```

Or

```
python find-expedition-urls.py input.csv output.csv
```
