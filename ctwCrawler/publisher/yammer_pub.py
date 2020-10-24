import requests
from requests.structures import CaseInsensitiveDict

class Publisher:
    url = "https://www.yammer.com/criticaltechworks.com/#/threads/inGroup?type=in_group&feedId=43795390464&view=all"

    # Confirm headers and body
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = "Basic YWJla2o6czxnZA=="
    headers["Content-Type"] = "application/json"

    def createEntry(self, url):
        data = "{" + url + "}"

    def readUrls(self):
        file1 = open('NewsResult.txt', 'r')
        return file1.readlines()


if __name__ == "__main__":
    pub = Publisher()

    count = 1
    urls = pub.readUrls()
    for url in urls:
        print("Line{}: {}".format(count, url.strip()))
        count += 1

        resp = requests.post(pub.url, headers=pub.headers, data=pub.createEntry(url=url))
        print(resp.status_code)