import requests


headers: dict[str, str] = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/86.0.4240.111 Safari/537.36'
        }

class GeoLocation():
    def __init__(self, ip: str) -> None:
        self.ip = ip

    def get_location(self):
        ip_address = self.ip
        response = requests.get(f'https://ipapi.co/{ip_address}/json/', headers=headers).json()
        location_data = {
            "ip": ip_address,
            "city": response.get("city"),
            "region": response.get("region"),
            "country": response.get("country_name")
        }
        return location_data

