import requests

API_KEY = "c875c2c90c77edb31d4b66c70dbcf470"
def get_data(place,forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"

    response = requests.get(url)
    data = response.json()

    filtered_data = data["list"]
    nr_values = forecast_days * 8      # 1 day = 24/3 = 8  3hs entries
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__ == "__main__":
     print(get_data(place="Rio de Janeiro", forecast_days=3, kind="Temperature"))
