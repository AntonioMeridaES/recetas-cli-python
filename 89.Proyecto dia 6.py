from pathlib import Path
from os import system


# ============================ # CATEGORY  METHODS # ============================

def get_categories():
    """Return a list of category folder names inside the Recetas directory."""
    base_path = Path(Path.home(), "Recetas")
    #dynamic list of folders
    categories = [c.name for c in base_path.iterdir() if c.is_dir()]
    return categories


def select_category():
    """Display categories and allow the user to choose one."""
    categories = get_categories()
    option = ""  # Starts empty
    while not option.isdigit() or not (0 <= int(option) <= len(categories)):
        print("Indíquenos una de estas opciones:")
        print("\n0 - Volver atrás")
        for i, cat in enumerate(categories, start=1):
            print(f"{i} - {cat}")
        option = input("Elige una categoría: ")
        if not option.isdigit() or not (0 <= int(option) <= len(categories)):
            system("cls")  # Clear windows
            print("\nOpción inválida. Intente de nuevo.")
    option = int(option)
    if option == 0:
        return None
    return option


# ============================ # RECIPE METHODS# ============================

def get_recipes(category_name: str):
    """Return a list of recipe files inside a given category."""
    base_path = Path(Path.home(), "Recetas")
    category_path = base_path / category_name
    recipe = [f.name for f in category_path.iterdir() if f.is_file()]
    return recipe


def select_recipe(category_name: str):
    """Display recipes inside a category and allow the user to choose one."""
    recipes = get_recipes(category_name)
    if not recipes:
        print("No hay recetas disponibles...")
        system("cls")
        return None
    option = ""
    while not option.isdigit() or not (0 <= int(option) <= len(recipes)):
        print(f"\nRecetas en la categoría: {category_name}")
        print("0 - Volver atrás")
        for i, rec in enumerate(recipes, start=1):
            print(f"{i} - {rec}")
        option = input("Elige una receta: ")
        if not option.isdigit() or not (0 <= int(option) <= len(recipes)):
            system("cls")  # Clear windows
            print("\nOpción inválida. Intente de nuevo.")
    option = int(option)
    if option == 0:
        return None
    return recipes[option - 1]


def open_recipe(category_name: str, recipe_name: str):
    """Open and display the content of a selected recipe."""
    base_path = Path(Path.home(), "Recetas")
    recipe_path = base_path / category_name / recipe_name
    with open(recipe_path, "r", encoding="utf-8") as recipe_file:
        system("cls")
        print(f"=== {recipe_name} ===\n")
        print(recipe_file.read())
        print("\n=== Fin de la receta ===\n")
    input("Pulse Enter para volver...")

def create_recipe(category_name: str, recipe_name: str):
    '''Create a new recipe inside a given category.'''
    base_path = Path(Path.home(), "Recetas")
    recipe_path = base_path / category_name
    with open(recipe_path, "w", encoding="utf-8") as recipe_file:
        system("cls")
        print(f"=== {recipe_name} ===\n")


# ============================ # OTHER METHODS# ============================

def choose_category():
    """Return the name of the selected category."""
    cat_index = select_category()
    if cat_index == None:
        return None
    categories = get_categories()
    category_name = categories[cat_index - 1]
    return category_name


# ============================ # MAIN PROGRAM  # ============================

while True:
    system("cls")  # Clear windows
    print("Elige una opción:\n"
          "1-Leer receta.\n"
          "2-Crear receta.\n"
          "3-Crear categoría.\n"
          "4-Eliminar receta.\n"
          "5-Eliminar categoría.\n"
          "6-Salir.\n"
          )
    num_option = input("Usted ha seleccionado ")
    # Check number bad option
    if not num_option.isdigit() or not (1 <= int(num_option) <= 6):
        system("cls")  # Clear windows
        print("La opcion seleccionada no es valida, debera de ser un numero entre 1 y 6, vuelva a intentarlo.\n")
        continue
    # Become  INT
    num_option = int(num_option)

    match num_option:
        # OPEN RECIPE
        case 1:
            category_name = choose_category()
            if category_name is None:
                print("No se ha seleccionado ninguna categoría.")
                input("Pulse Enter para volver al menú...")
                continue
            recipe_name = select_recipe(category_name)
            if recipe_name is None:
                print("No se ha seleccionado ninguna receta.")
                input("Pulse Enter para volver...")
                continue
            open_recipe(category_name, recipe_name)
        case 2:
            ##NEW RECIPE
            category_name = choose_category()
            if category_name is None:
                print("No se ha seleccionado ninguna categoría.")
                input("Pulse Enter para volver al menú...")
                continue
            recipe_name = select_recipe(category_name)
        case 3:
            select_category()
        case 4:
            select_category()
        case 5:
            select_category()
    # Opcion 6 salimos del programa.
    if num_option == 6:
        print("Saliendo del programa...")
        break
