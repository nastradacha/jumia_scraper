
# Jumia Scraper Project

![Jumia Scraper](https://img.shields.io/badge/Web-Scraping-blue.svg?style=flat-square) ![Python](https://img.shields.io/badge/Made%20with-Python-brightgreen.svg?style=flat-square) ![GitHub](https://img.shields.io/github/license/nastradacha/jumia_scraper?style=flat-square)

Welcome to the **Jumia Scraper** project! This tool scrapes product data from [Jumia](https://www.jumia.com.ng/), Nigeria’s largest online shopping platform. The project gathers information on products, cleans the data, and provides insights on the highest, middle, and lowest-rated products in various categories.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- 🛍️ **Scrapes product data from Jumia**
- 🏷️ **Categorizes products based on ratings**: Highest, middle, and lowest.
- 📄 **Data Cleaning**: Removes duplicates and irrelevant data.
- 🔍 **Extensible**: Can be easily extended to scrape more fields or categories.
- 📊 **Prepares data for easy analysis** using tools like Pandas and NumPy.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/jumia_scraper.git
   ```
2. Change to the project directory:
   ```bash
   cd jumia_scraper
   ```
3. Create a virtual environment and activate it:
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows use: env\Scripts\activate
   ```
4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. **Run the Scraper**:
   You can run the scraper by executing the `main.py` file:
   ```bash
   python main.py
   ```

2. **Data Cleaning**:
   After scraping, clean the data by running the following:
   ```bash
   python clean_data.py
   ```

3. **Testing**:
   Run the unit tests to ensure the scraper works as expected:
   ```bash
   python -m unittest unit_test_scraper.py
   ```

---

## File Structure

```bash
jumia_scraper/
│
├── scraper.py           # Contains the web scraping logic
├── clean_data.py        # Script for cleaning and transforming the scraped data
├── main.py              # Main entry point for running the scraper
├── unit_test_scraper.py # Unit tests for validating the scraper
├── requirements.txt     # List of dependencies needed to run the project
└── README.md            # Project documentation (You are here!)
```

---

## Technologies Used

- **Python**: Core language used to build the project.
- **Selenium**: Used for web scraping.
- **Pandas**: For cleaning and analyzing the scraped data.
- **BeautifulSoup**: For parsing HTML and extracting data.

---

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Feel free to fork this project and submit pull requests with improvements or bug fixes!

1. Fork the project
2. Create your feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a pull request

---

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

### Acknowledgements

- **Jumia**: For providing such a rich platform to scrape product data.
- **Selenium and BeautifulSoup**: For making web scraping easy.
- **Pandas**: For providing powerful data analysis capabilities.
