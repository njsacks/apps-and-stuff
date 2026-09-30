import urllib.request
import xml.etree.ElementTree as ET
import json
from datetime import datetime

# Feeds to aggregate
FEEDS = [
    {"name": "The Hacker News", "url": "https://feeds.feedburner.com/TheHackersNews"},
    {"name": "CISA Alerts", "url": "https://www.cisa.gov/cybersecurity-advisories/all.xml"}
]

articles = []

for feed in FEEDS:
    try:
        req = urllib.request.Request(feed["url"], headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            xml_data = response.read()
            root = ET.fromstring(xml_data)
            
            # Parse standard RSS items
            for item in root.findall('.//item')[:5]:  # Get top 5 per feed
                title = item.find('title').text if item.find('title') is not None else 'No title'
                link = item.find('link').text if item.find('link') is not None else '#'
                pub_date = item.find('pubDate').text if item.find('pubDate') is not None else ''

                articles.append({
                    'title': title,
                    'link': link,
                    'source': feed['name'],
                    'pubDate': pub_date
                })
    except Exception as e:
        print(f"Error fetching {feed['name']}: {e}")

# Save results to articles.json
with open('articles.json', 'w', encoding='utf-8') as f:
    json.dump(articles, f, indent=2)

print(f"Saved {len(articles)} articles.")
    json.dump(articles, f, indent=2)


