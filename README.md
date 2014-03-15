#iCanViewer

Crawler my school's information by mechanize


Testing login and get my schedule in FJU(Not done yet!)

```
http://www.elearn.fju.edu.tw
```

##Python

```python
browser = mechanize.Browser()
browser.set_handle_robots(False)
```
Use mechanize to create a browser to get your page.

set_handle_robots(False)
Ingore robots.txt, if you dont do this, sometimes will get the error.

```python
results = browser.open(ican)
soup = BeautifulSoup(results.read())
results =  soup.findAll("span", {"style": "font-weight:bold;"})[0].text.split(" ")
```
open(your url here) and you will get html source.

You can use Regular Expression or like:BeautifulSoup to find the content what you want.
These will help you make the page in order and read easily.
