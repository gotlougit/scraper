# scraper
A basic web scraper built completely in Python

## Setup and Installation

First, get these files with git:

```bash
git clone https://github.com/gotlougit/scraper.git
```

Then run the setup.py file contained in this repository:

```bash
python3 setup.py install
```

## Usage

Scraper is designed to be used to get information about the webpage through the tags and attributes present.
The functions present are designed to get the webpage, get the HTML tags out of the webpage and then searching 
for a variety of tags with a specific attribute, and then getting the value of that attribute.

Get a webpage with the getPage() function, like this:
```python
import scraper
page = scraper.getPage("www.github.com")
```

Get a list of tags using getTags(), for example:
```python
tags = scraper.getTags(page)
```

Find the values of attributes of specific tags using the getTagAttributes() function.
```python
attributes = scraper.getTagAttributes(tags,'a','title') #searches for the title attribute in the <a> tag
```
