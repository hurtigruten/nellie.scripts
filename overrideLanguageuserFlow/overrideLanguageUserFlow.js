const fs = require("fs");
const countries = require("i18n-iso-countries");
const stringSimilarity = require("string-similarity");
const enISOData = require("./enISOData");

const jsonFilePath = process.argv[2];
const language = process.argv[3];

const rawData = fs.readFileSync(jsonFilePath);
const jsonData = JSON.parse(rawData);

const to2CodeISO = jsonData.LocalizedCollections[0].Items.map(
  ({ Name, Value }) => {
    const bestMatch = stringSimilarity.findBestMatch(
      Name,
      enISOData.map(({ Name }) => Name)
    ).bestMatch;

    return {
      Name,
      Value:
        countries.getAlpha2Code(Name, language) ||
        (bestMatch.rating > 0.6
          ? enISOData.find(({ Name }) => Name === bestMatch.target)?.Value
          : "MANUAL UPDATE") ||
        "MANUAL UPDATE",
    };
  }
);

jsonData.LocalizedCollections[0].Items = to2CodeISO;
jsonData.LocalizedCollections[0].Override = true;

fs.writeFile(jsonFilePath, JSON.stringify(jsonData), (err) => {
  if (err) return console.log(err);
  console.log(jsonData);
  console.log("writing to " + jsonFilePath);
});
