"""КофеКвест — сервис поиска кофеен. Версия 1.0 (стабильный релиз)"""
import config

def find_cafes(city=config.DEFAULT_CITY):
    print(f"Ищем кофейни в городе: {city}")
    return []

if __name__ == "__main__":
    find_cafes()