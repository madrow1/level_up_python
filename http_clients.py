# This has to be installed with pip install requests
import requests

# request can be used to query APIs with common request formats, such as GET and POST
response = requests.get(
    "http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json")

# This converts the API request to a json file, and assigns it to the variable
last_twenty_years = response.json()[1][:20]

# This then loops over that and divides the value by 10000000
for year in last_twenty_years:
    display_width = year["value"] // 10_000_000
    print(f'{year["date"]}: {year["value"]}', "=" * display_width)