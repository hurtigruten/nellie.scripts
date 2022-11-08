# Classify URLs to expedition | group | coastal | nellie

This script reads in a CSV file of urls in the following format:

```
https://www.hurtigruten.de/alaska/
https://www.hurtigruten.de/app/
https://www.hurtigruten.de/de/adobe-download/
https://www.hurtigruten.de/eine-reise-finden/
https://www.hurtigruten.de/kataloge/
https://www.hurtigruten.de/short-urls/katalog-expeditionsseereisen-2021/
https://www.hurtigruten.de/heimathafen-hamburg/
```

and classifies them into an output csv like so:

```
ur, brand
https://www.hurtigruten.de/alaska/, expedition
https://www.hurtigruten.de/app/, group
https://www.hurtigruten.de/de/adobe-download/, group
https://www.hurtigruten.de/eine-reise-finden/, expedition
https://www.hurtigruten.de/kataloge/, group
https://www.hurtigruten.de/short-urls/katalog-expeditionsseereisen-2021/, group
https://www.hurtigruten.de/heimathafen-hamburg/, expedition
```

Note that this script uses the deno runtime, install using Homebrew:

```
brew install deno
```

Script is run like so:

```
 deno run --allow-read --allow-net --allow-write findExpeditionURLs.ts input.csv output.csv
```
