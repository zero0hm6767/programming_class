import urllib.request
import re

url = "https://web.stanford.edu/~jurafsky/NLPCourseraSlides.html"
html = urllib.request.urlopen(url)
html_contents = str(html.read().decode("utf-8"))
url_list = re.findall(r"http.+\.pdf", html_contents)
f_n = 1

for url in url_list:
    file_name = "".join(url)
    full_url = file_name
    print(full_url)
    frame, header = urllib.request.urlretrieve(full_url, "./pdf/" + str(f_n) + ".pdf")
    f_n += 1
    print("Downloaded: " + str(f_n - 1) + ".pdf")
