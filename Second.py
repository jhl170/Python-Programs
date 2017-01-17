# This will extract links

# page will be content of a web page
start_link = page.find("<a href=")

# start from start_link, look for "
start_quote = page.find('"', start_link)
# This will find one after the first "
end_quote = page.find('"', start_quote+1)
url = page[start_quote+1 : end_quote]

# value of the rest of the page
page = page[end_quote:]
