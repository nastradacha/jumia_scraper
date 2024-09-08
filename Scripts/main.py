from scraper import jumia_recommended
from clean_data import clean_data
import pandas as pd

raw_scraped_data = 'data/raw/jumia_products.csv'
cleaned_data = 'data/processed/jumia_products_cleaned.csv'


def main():
    # Run the scraper
    print("Scraping data from Jumia...")
    jumia_recommended(raw_scraped_data)
    
    # Load the scraped CSV and clean the data
    print("Cleaning the scraped data...")
    df = pd.read_csv(raw_scraped_data)  # Adjust the path as needed
    cleaned_df = clean_data(df)
    
    # Save the cleaned data
    cleaned_df.to_csv(cleaned_data, index=False)
    print("Data cleaning complete! Cleaned data saved.")

if __name__ == "__main__":
    main()