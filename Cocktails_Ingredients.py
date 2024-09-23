import csv
import json
from abc import ABC, abstractmethod

#popular_cocktails = ["1. Май Тай", "2. Маргарита", "3. Мохито", "4. Дайкири"]


class iRepository(ABC):
    @abstractmethod
    def load_date(self):
        pass

    @abstractmethod
    def find_by_name(self, name: str):
        pass

    @abstractmethod
    def find_by_tags(self, tags: []):
        pass

class Cocktail:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def top_cocktails():
        popular_list = "\n".join(popular_cocktails)
        return f"Популярные коктейли:\n{popular_list}"

    def cocktail_recipe(self, name):
        recipe = cocktail_recipes.get(name)
        if recipe:
            return f"Рецепт коктейля '{name}':\n{recipe}"
        return "Извините, рецепт этого коктейля не найден. Попробуйте другой."


class Ingredient:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


class DishService(iRepository):
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = self.load_date()

# Метод для работы с файлом JSON
    def load_date(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def find_by_name(self, name: str):
        data = self.load_date()
        for item in data["data"]:
            if item["name"] == name:
                return item["description"]
        return "Коктейль не найден"

    def find_by_tags(self, tags: str):
        data = self.load_date()
        results = []
        for item in data["data"]:
            if set(tags).intersection(item.get("tags", [])):
                results.append(item["name"])
        if results:
            return results
        else:
            return "Коктейль не найден"


class CsvRepository(iRepository):
    def __int__(self, file_path: str):
        self.file_path = file_path
        self.data = self.load_date()

    def load_date(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            data = csv.DictReader(file)
        return data

    def find_by_name(self, name: str):
        data = self.load_date()
        for item in data["data"]:
            if item["name"] == name:
                return item["description"]
        return "Коктейль не найден"

    def find_by_tags(self, tags: str):
        data = self.load_date()
        results = []
        for item in data["data"]:
            if set(tags).intersection(item.get("tags", [])):
                results.append(item["name"])
        if results:
            return results
        else:
            return "Коктейль не найден"


#service = DishService(data='dishes.json')


# Проверка работоспособности
if __name__ == "__main__":
    # Работа с JSON
    #json_repo = DishService("dishes.json")
    #user_find_by_name = input("")
    #print(json_repo.find_by_name(user_find_by_name))
    #user_find_by_tags = input("")
    #tags = [tag.strip() for tag in user_find_by_tags.split(',')]
    #print(json_repo.find_by_tags(tags))

    # Работа с CSV
    csv_repo = CsvRepository("dishes.csv")
    user_find_by_name = input("")
    print(csv_repo.find_by_name(user_find_by_name))
    user_find_by_tags = input("")
    tags = [tag.strip() for tag in user_find_by_tags.split(',')]
    print(csv_repo.find_by_tags(tags))
