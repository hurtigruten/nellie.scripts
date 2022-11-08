import { readCSV, writeCSV } from "https://deno.land/x/csv/mod.ts";
import { DOMParser } from "https://deno.land/x/deno_dom/deno-dom-wasm.ts";

if (typeof Deno.args[0] === "string" && typeof Deno.args[1] === "string") {
  const f = await Deno.open(Deno.args[0]);

  const rows = [["url", "brand"]];

  for await (const row of readCSV(f)) {
    for await (const cell of row) {
      const textResponse = await fetch(cell);
      const textData = await textResponse.text();
      const document: any = new DOMParser().parseFromString(
        textData,
        "text/html"
      );

      const bodyClassList = document.querySelector("body").classList;
      let brand = "undefined";
      if (bodyClassList?.contains("theme-expedition")) {
        brand = "expedition";
      } else if (bodyClassList?.contains("theme-group")) {
        brand = "group";
      } else if (bodyClassList?.contains("theme-coastal")) {
        brand = "coastal";
      } else {
        if (textData.includes("nellie")) {
          brand = "nellie";
        }
      }

      rows.push([cell, brand]);
    }
  }
  const outfile = await Deno.open(Deno.args[1], {
    write: true,
    create: true,
    truncate: true,
  });
  await writeCSV(outfile, rows);
  outfile.close();
  f.close();
} else {
  console.log("ERROR: Please provide a file path");
}
