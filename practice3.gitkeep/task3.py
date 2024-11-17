import requests

def get_information(url):
    response = requests.get(url)
    print ("Status code:", response.status_code)
    print("Headers:", response.headers)
    print("URL:", response.url)
    print("History:", response.history)
    print("Encoding:", response.encoding)
    print("Reason:", response.reason)
    print("Cookies:",response.cookies)
    print("Elapsed:", response.elapsed)
    print("Request:", response.request)
    print("Content:", response.content)

url_to_check="https://www.python.org/"
get_information(url_to_check)