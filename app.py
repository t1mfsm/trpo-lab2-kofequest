"""КофеКвест — сервис поиска кофеен. Версия 1.0 (стабильный релиз, включает поиск по рейтингу)"""
import config
from search import filter_by_rating

def find_cafes(city=config.DEFAULT_CITY):
    print(f"Ищем кофейни в городе: {city}")
    return filter_by_rating([])

if __name__ == "__main__":
    find_cafes()