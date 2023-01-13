import requests

API_KEY = "c875c2c90c77edb31d4b66c70dbcf470"
def get_data(place,forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    filtered_data = data["list"]
    nr_values = forecast_days * 8      # 1 day = 24/3 = 8  3hs entries
    filtered_data = filtered_data[:nr_values]
#    print(filtered_data[0]['dt_txt'])   # print date and hour for the first element
    dates = [dic["dt_txt"] for dic in filtered_data]
#   print(dates)

    if kind == "Temperature":
#       filtered_data = [float("{:.2f}".format(dic["main"]['temp'])) for dic in filtered_data]  - transforma em float com 2 casas dec
        filtered_data = [dic["main"]['temp']-273.15 for dic in filtered_data]  # from Kelvin to celsius
    if kind == "Sky":
        filtered_data = [dic["weather"][0]['main'] for dic in filtered_data]

    return dates, filtered_data

if __name__ == "__main__":
     print(get_data(place="Rio de Janeiro", forecast_days=3, kind="Temperature"))
