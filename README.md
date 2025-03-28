# Animal Data Fetcher

This project fetches detailed information about animals using the API provided by [API Ninjas](https://api-ninjas.com). The script allows users to input the name of an animal, fetches the animal's data, and updates an HTML file with this data.

## Features

- Fetch animal information like diet, type, and location.
- Dynamically updates an HTML file with the retrieved data.
- Handles API request errors and missing data gracefully.

## Installation

### Prerequisites

Make sure you have Python 3.6+ installed on your machine. You'll also need to install the required dependencies from `requirements.txt`.

### Steps

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/animal-data-fetcher.git
    cd animal-data-fetcher
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory of the project and add your API key:

    ```
    API_KEY=your_api_key_here
    ```

    You can get the API key from [API Ninjas](https://api-ninjas.com).

## Usage

1. Make sure the `.env` file is in place with your API key.
2. Run the script using the command:

    ```bash
    python main.py
    ```

3. Enter the name of an animal when prompted.

4. The script will fetch data about the animal and update `animals.html` with the new information.

## File Structure

