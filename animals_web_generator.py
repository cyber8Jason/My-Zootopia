import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def generate_animal_string(animals_data):
    """ Prints selected information for each animal in the list """
    output = ""
    for animal in animals_data:
        animal_name = animal['name'].replace("’", "'")
        output += "<li class='cards__item'>\n"
        if "name" in animal:
            output += f"\t<div class='card__title'>{animal_name}</div>\n"
        output += "\t\t<p class='card__text'>\n"
        if "characteristics" in animal and "diet" in animal["characteristics"]:
            output += f"\t\t\t<strong>Diet:</strong> {animal['characteristics']['diet']}<br/>\n"
        if "locations" in animal and animal["locations"]:
            output += f"\t\t\t<strong>Location:</strong> {animal['locations'][0]}<br/>\n"
        if "characteristics" in animal and "type" in animal["characteristics"]:
            output += f"\t\t\t<strong>Type:</strong> {animal['characteristics']['type']}<br/>\n"
        output += "\t\t</p>\n"
        output += "</li>\n"
    return output


def load_template(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def inject_animals_into_template(template, animals_string):
    return template.replace("__REPLACE_ANIMALS_INFO__", animals_string)


def save_html(output_string, filename="animals.html"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(output_string)


def main():
    animals_data = load_data("animals_data.json")
    animals_string = generate_animal_string(animals_data)
    template = load_template("animals_template.html")
    final_html = inject_animals_into_template(template, animals_string)
    save_html(final_html)


if __name__ == "__main__":
    main()
