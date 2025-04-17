import json


def load_data(file_path):
    """ loads a JSON file """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def serialize_animal(animal):
    """
    generates an HTML list item with selected information about one animal
    :param animal: dictionary containing animal data
    :return: HTML string for one animal card
    """
    output = ""
    output += "<li class='cards__item'>\n"
    if "name" in animal:
        animal_name = animal['name'].replace("’", "'")
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
    """ loads the content of the template file and returns it as a string """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def insert_animals_into_template(template, animals_string):
    """ finds the placeholder __REPLACE_ANIMALS_INFO__ in the template and replaces it with the animal data string """
    return template.replace("__REPLACE_ANIMALS_INFO__", animals_string)


def save_html(output_string, filename="animals.html"):
    """ saves the final HTML content into a file with the filename animals.html """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(output_string)


def main():
    """
    generates an HTML file with animal info by
    loading JSON data, formatting it, and inserting it into a template
    """
    animals_data = load_data("animals_data.json")
    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)
    template = load_template("animals_template.html")
    final_html = insert_animals_into_template(template, output)
    save_html(final_html)


if __name__ == "__main__":
    main()
