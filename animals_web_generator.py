import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def generate_animal_string(animals_data):
    """ Prints selected information for each animal in the list """
    output = ""
    for animal in animals_data:
        if "name" in animal:
            output += f"Name: {animal['name']}\n"
        if "characteristics" in animal and "diet" in animal["characteristics"]:
            output += f"Diet: {animal['characteristics']['diet']}\n"
        if "locations" in animal and animal["locations"]:
            output += f"Location: {animal['locations'][0]}\n"
        if "characteristics" in animal and "type" in animal["characteristics"]:
            output += f"Type: {animal['characteristics']['type']}\n"
        output += "\n"
    return output


def load_template(file_path):
    with open(file_path, "r") as file:
        return file.read()


def inject_animals_into_template(template, animals_string):
    return template.replace("__REPLACE_ANIMALS_INFO__", animals_string)


def save_html(output_string, filename="animals.html"):
    with open(filename, "w") as file:
        file.write(output_string)


def main():
    animals_data = load_data("animals_data.json")
    animals_string = generate_animal_string(animals_data)
    template = load_template("animals_template.html")
    final_html = inject_animals_into_template(template, animals_string)
    save_html(final_html)


if __name__ == "__main__":
    main()
