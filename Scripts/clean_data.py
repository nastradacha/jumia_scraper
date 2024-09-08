import pandas as pd
import re

# Load the CSV file
# file_path = 'jumia_products.csv'



import logging

# Setup logging
logging.basicConfig(filename='logs/data_cleaning.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def clean_data(df):
    logging.info("Starting data cleaning process.")
    try:
        # Renaming columns
        df.rename(columns={'Price (with symbol)': 'Price'}, inplace=True)
        
        # Log and handle rows with invalid or missing data
        invalid_data = df[df['Price'].isna()]
        logging.info(f'Removing rows with missing prices: {invalid_data.index.tolist()}')
        df = df.dropna(subset=['Price'])

        # Handle price ranges by splitting into two columns
        if df['Price'].str.contains('-').any():
            df[['price_lower', 'price_upper']] = df['Price'].str.split('-', expand=True)
            #df[['price_lower', 'price_upper']] = df[['price_lower', 'price_upper']].apply(pd.to_numeric, errors='coerce')
            logging.info(f'Split price ranges into lower and upper bounds for rows: {df.index[df["Price"].str.contains("-")].tolist()}')
        logging.info(f"Data cleaning completed. Processed {len(df)} rows.")
    except Exception as e:
        logging.error(f"Error during data cleaning: {e}")
    return df

# # Example usage
# data = pd.read_csv(file_path)
# cleaned_data = clean_data(data)
# cleaned_data.to_csv('cleaned_data.csv', index=False)












# df = pd.read_csv(file_path)

# # Function to clean price fields (removing unwanted characters but keeping the Naira symbol)
# def clean_price(price):
#     # If it's a price range, split and take the first price
#     if '-' in price:
#         price = price.split('-')[0].strip()
    
#     # Match and preserve the Naira symbol along with digits
#     match = re.search(r'(₦\s?\d+[,.]?\d*)', price)  # Adjusted to handle commas and decimal points
#     return match.group(0) if match else None

# # Function to extract numeric value from price
# def extract_numeric(price):
#     # Remove the Naira symbol and convert the remaining text to a float
#     if price:
#         return re.sub(r'[₦,\s]', '', price)  # Remove Naira symbol, commas, and spaces
#     return None

# # Apply the cleaning function to both Price and Old Price columns
# df['Price (with symbol)'] = df['Price'].apply(clean_price)
# df['Old Price (with symbol)'] = df['Old Price'].apply(clean_price)

# # Apply the numeric extraction function to create separate numeric columns
# df['Price'] = df['Price (with symbol)'].apply(extract_numeric).astype(float)
# df['Old Price'] = df['Old Price (with symbol)'].apply(extract_numeric).astype(float)

# # Replace 'No rating' and 'No image' with NaN for easier handling
# df['Rating'] = df['Rating'].replace('No rating', None)
# df['Product Image'] = df['Product Image'].replace('No image', None)

# # Drop rows where both price and old price are missing (optional)
# df_cleaned = df.dropna(subset=['Price', 'Old Price'], how='all')

# # Save the cleaned DataFrame to a new CSV
# cleaned_file_path = 'jumia_products_cleaned.csv'
# df_cleaned.to_csv(cleaned_file_path, index=False, encoding='utf-8')

# # Display the cleaned DataFrame
# print(df_cleaned.head())

