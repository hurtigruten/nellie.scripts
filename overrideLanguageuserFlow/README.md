# Override language values in Azure AD B2C | User flows

## Sign up and sign in

The default values in the contries dropdown in the Azure provided sign up / sign in pages is the country name, but the Azure Function calling PG on sign up expcts values that are two digit ISO codes.

This becomes more necessary as we support different locales as PG should not need to handle different translated country names.

This script converts the given values in the default sign up page config json, to their ISO equivalents. Given the relevant json file as an argument it converts this:

```
"LocalizedCollections": [
    { "ElementType": "ClaimType",
    "ElementId": "country",
    "TargetCollection": "Restriction",
    "Override": false,
    "Items": [
    { "Name": "Afghanistan", "Value": "Afghanistan" },
    { "Name": "Åland Islands", "Value": "Åland Islands" },
    { "Name": "Albania", "Value": "Albania" },
    { "Name": "Algeria", "Value": "Algeria" },
    { "Name": "American Samoa", "Value": "American Samoa" }, etc...
```

to this:

```
"LocalizedCollections": [
    { "ElementType": "ClaimType",
    "ElementId": "country",
    "TargetCollection": "Restriction",
    "Override": true,
    "Items": [
        { "Name": "Afghanistan", "Value": "AF" },
        { "Name": "Åland Islands", "Value": "AX" },
        { "Name": "Albania", "Value": "AL" },
        { "Name": "Algeria", "Value": "DZ" },
        { "Name": "American Samoa", "Value": "AS" }, etc...
```

Note also that the `Override` key is set to `true`.

The updated json file should be uploaded to Azure AD B2C as an override for the given locale.

The script should be run like so:

```
npm i

node overrideLanguageUserFlow.js ./default_config_from_azure.json en

node overrideLanguageUserFlow.js <path of downloaded default json config> <supported language>
```

Note that this script relies on [node-i18n-iso-countries](https://github.com/michaelwittig/node-i18n-iso-countries) and a supported country list can be found here.
