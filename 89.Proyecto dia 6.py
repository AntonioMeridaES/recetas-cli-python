from linecache import clearcache
from os import system
from pathlib import Path
from xml.dom.minidom import ProcessingInstruction


# ============================ # CATEGORY  METHODS # ============================

def get_categories():
    """Return a list of category folder names inside the Recetas directory."""
    base_path = Path(Path.home(), "Recetas")
    # dynamic list of folders
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

def choose_category():
    """Return the name of the selected category."""
    cat_index = select_category()
    if cat_index == None:
        return None
    categories = get_categories()
    category_name = categories[cat_index - 1]
    return category_name

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

def recipe_exist(category_name: str, recipe_name: str):
    """Return True if the recipe exists, False otherwise."""
    recipes = get_recipes(category_name)
    for recipe in recipes:
        if recipe.lower() == f"{recipe_name}.txt".lower():
            return True
    return False

def create_recipe(category_name: str, recipe_name: str):
    '''Create a new recipe inside a given category.'''
    base_path = Path(Path.home(), "Recetas")
    recipe_path = base_path / category_name / f"{recipe_name}.txt"
    system("cls")
    print(f"=== Creando receta: {recipe_name} ===\n")
    print("Escribe la receta. Cuando termines, escribe 'FIN' y pulsa Enter.\n")
    with open(recipe_path, "w", encoding="utf-8") as recipe_file:
        while True:
            line = input("")
            if line.upper() == "FIN":
                break
            recipe_file.write(line + "\n")
    system("cls")
    print("\nReceta guardada correctamente.")
    input("Pulse Enter para volver al menú...")
# ============================ # OTHER METHODS# ============================


# ============================ # MAIN PROGRAM  # ============================

while True:
    # CLEAR WINDOWS
    system("cls")
    #WELCOME
    base_path = Path(Path.home(), "Recetas")
    print("=== Bienvenido Usuario===")
    print(f"La ruta de carpetas es {base_path}")
    # ALL RECIPES
    print(f"El total de recetas es de {len(list(base_path.rglob("*.txt")))}")
    #RECIPES BY CATEGORY
    print("\nRecetas disponibles por categoria:")
    for category in get_categories():
        category_path= base_path / category
        count = len(list(category_path.glob("*.txt")))
        print(f"{category}: {count}")
    #MAIN MENU
    print("\nElige una opción:\n"
          "1-Leer receta.\n"
          "2-Crear receta.\n"
          "3-Crear categoría.\n"
          "4-Eliminar receta.\n"
          "5-Eliminar categoría.\n"
          "6-Salir.\n"
          )
    num_option = input("Usted ha seleccionado ")
    # CHECK NUMBER BAD OPTION
    if not num_option.isdigit() or not (1 <= int(num_option) <= 6):
        system("cls")  # Clear windows
        print("La opcion seleccionada no es valida, debera de ser un numero entre 1 y 6, vuelva a intentarlo.\n")
        continue
    # BECOME num_option to INT
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
        ##NEW RECIPE
        case 2:
            category_name = choose_category()
            if category_name is None:
                print("No se ha seleccionado ninguna categoría.")
                input("Pulse Enter para volver al menú...")
                continue
            new_recipe_name = input("Ingrese el nombre del receta: ")
            if recipe_exist(category_name, new_recipe_name):
                print("El receta ya existe!")
                input("Pulse Enter para volver...")
                continue
            create_recipe(category_name, new_recipe_name)
            continue
        case 3:
            select_category()
        case 4:
            select_category()
        case 5:
            select_category()
        # OPTION 6 EXIT PROGRAM
        case 6:
            print("Saliendo del programa...")
            break