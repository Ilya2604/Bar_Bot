import json

popular_cocktails = ["1. Май Тай", "2. Маргарита", "3. Мохито", "4. Дайкири"]


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


class DishService:
    def __init__(self, name=None, tags=None):
        self.name = name
        self.tags = tags

    def find_by_name(self):
        user_find_by_name = input("")
        with open("dishes.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        for item in data["data"]:
            if item["name"] == user_find_by_name:
                return item["description"]
        return "Коктейль не найден"

    def find_by_tags(self):
        user_find_by_tags = input("")
        tags = [tag.strip() for tag in user_find_by_tags.split(',')]
        with open("dishes.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        results = []
        for item in data["data"]:
            if set(tags).intersection(item.get("tags", [])):
                results.append(item["name"])
        if results:
            return results
        else:
            return "Коктейль не найден"




service = DishService()
#print(service.find_by_name())
#print(service.find_by_tags())

