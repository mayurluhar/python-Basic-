import requests as rq
import  json

def get_data(url):
    try:
        return rq.get(url).text

    except Exception as e:
        print("unable to load url")

def load_data(data):
    if not data is None:
        j = json.loads(data)
        fname = j["results"][0]["name"]["first"]
        lname = j["results"][0]["name"]["last"]
        phone = j["results"][0]["registered"]["phone"]
        email = j["results"][0]["email"]
        return fname,lname,phone,email

def main():
    url = "https://randomuser.me/api"
    value = load_data(get_data(url))
    if not value is None:
        print("Full name:", value[0] + " " + value[1])
        print("Phone No:", value[2])
        print("email:", value[3])

if __name__ == '__main__':
    main()
