import urllib
# Get a file-like object for a site.
f = urllib.urlopen("http://call-kelly.com")
# NOTE: At the interactive Python prompt, you may be prompted for a username
# NOTE: and password here.
# Read from the object, storing the page's contents in 's'.
s = f.read()
f.close()
print(s)
