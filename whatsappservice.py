import requests
import json

def SendMessageWhatsapp(data):
    try:
        token =     "EAF3gkosTIZAQBRCH0ChZAMZCh94RHh5HZByzOUoHMM5gRYq0FMD4qWeJpSetd29cQzUsTjx4DeHp9PaPOM9VtdUVczPIspjd7nXZCHZBiyTZA6PSq2666Oh86IAwWAyXDYF6dXAxx7TZBYKVVZCzZAVjXzU73ODPGTUZCe8aMg58z4E5LMqEVYD8USUBAryWzlhTkwjFwZDZD"
        api_url = "https://graph.facebook.com/v22.0/1012501618618541/messages"
        headers = {
                        "Content-Type": "application/json",
                        "Authorization": "Bearer " + token
                    }

        response = requests.post(api_url,data=json.dumps(data),headers=headers)

        if response.status_code == 200:
            return True

        return False
    except Exception as exception:
        print(exception)
        return False