"""КофеКвест — сервис поиска кофеен. Версия 0.2 (ветка search-feature)"""
from search import filter_by_rating

def find_cafes(city):
    print(f"Ищем кофейни в городе: {city}")
    return filter_by_rating([])

if __name__ == "__main__":
    find_cafes("Москва")