"""Модуль поиска и фильтрации кофеен."""

def filter_by_rating(cafes, min_rating=4.0):
    return [c for c in cafes if c["rating"] >= min_rating]