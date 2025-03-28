import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("Missing API_KEY. Please find it in .env file")

BASE_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_animal_data(animal_name):
    """Fetch animal data from the API."""
    url = f"{BASE_URL}?name={animal_name}"
    headers = {"X-Api-Key": API_KEY}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        if not data:
            return {"error": "No results found for this animal."}

        return data  # API returns a list of animals
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch data: {e}"}


def generate_animal_html(animal):
    """Generate HTML snippet for a single animal."""
    return f"""
        <li class='cards__item'>
            <div class='card__title'>{animal.get('name', 'Unknown')}</div>
            <div class='card__text'>
                <strong>Diet:</strong> {animal.get('characteristics', {}).get('diet', 'Unknown')}<br>
                <strong>Location:</strong> {', '.join(animal.get('locations', ['Unknown']))}<br>
                <strong>Type:</strong> {animal.get('characteristics', {}).get('type', 'Unknown')}<br>
            </div>
        </li>
    """


def update_animals_html(input_html, output_html, animal_data):
    """Update the HTML file with new animal data."""
    try:
        with open(input_html, "r", encoding="utf-8") as file:
            html_content = file.read()
    except FileNotFoundError:
        print(f"Error: {input_html} not found.")
        return

    start_marker = "<ul class=\"cards\">"
    end_marker = "</ul>"
    start_index = html_content.find(start_marker) + len(start_marker)
    end_index = html_content.find(end_marker, start_index)

    if start_index == -1 or end_index == -1:
        print("Error: HTML markers not found.")
        return

    # Generate HTML for each animal in the list
    animal_html_list = "\n".join(generate_animal_html(animal) for animal in animal_data)

    # Inject new content into HTML
    new_html_content = html_content[:start_index] + "\n" + animal_html_list + "\n" + html_content[end_index:]

    # Write to a temporary file first
    temp_output = output_html + ".tmp"
    with open(temp_output, "w", encoding="utf-8") as file:
        file.write(new_html_content)

    # Replace the original file
    os.replace(temp_output, output_html)

    print("Updated animals.html successfully!")


def main():
    """Main function to fetch animal data and update HTML."""
    animal_name = input("Enter the name of an animal: ").strip().lower()
    animal_data = fetch_animal_data(animal_name)

    if "error" in animal_data:
        print(animal_data["error"])
        return

    # Ensure we process a list of animals
    if isinstance(animal_data, dict):  # Sometimes API may return a single object
        animal_data = [animal_data]

    update_animals_html("animals.html", "animals.html", animal_data)


if __name__ == "__main__":
    main()
