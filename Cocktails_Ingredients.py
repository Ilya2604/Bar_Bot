popular_cocktails = ["1. Май Тай", "2. Маргарита", "3. Мохито", "4. Дайкири"]

class Cocktail:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def top_cocktails():
        popular_list = "\n".join(popular_cocktails)
        return f"Популярные коктейли:\n{popular_list}"

    def cocktail_recipe(name):
        recipe = cocktail_recipes.get(name)
        if recipe:
            return f"Рецепт коктейля '{name}':\n{recipe}"
        return "Извините, рецепт этого коктейля не найден. Попробуйте другой."


class Ingredient:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
