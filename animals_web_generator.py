import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def print_animal_info(animals_data):
    """ Prints selected information for each animal in the list """
    for animal in animals_data:
        if "name" in animal:
            print(f"Name: {animal['name']}")
        if "characteristics" in animal and "diet" in animal["characteristics"]:
            print(f"Diet: {animal['characteristics']['diet']}")
        if "locations" in animal and animal["locations"]:
            print(f"Location: {animal['locations'][0]}")
        if "characteristics" in animal and "type" in animal["characteristics"]:
            print(f"Type: {animal['characteristics']['type']}")
        print("." * 3)


def main():
    animals_data = load_data("animals_data.json")
    print_animal_info(animals_data)


if __name__ == "__main__":
    main()
