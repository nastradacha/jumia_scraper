from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
#import undetected_chromedriver as uc
import pandas as pd
from time import sleep
# from fake_useragent import UserAgent
import random
import logging


# Setup logging
logging.basicConfig(filename='logs/scraper.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')





# List of user agents
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/89.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.48",
]



def jumia_recommended(raw_scraped_data):
    logging.info("Starting Jumia scraping process.")
    # Setup Chrome options
    # ua = UserAgent()
    # user_agent = ua.random
    # user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    user_agent = random.choice(user_agents)
    options = Options()
    options.add_argument("--enable-javascript")
    options.add_argument(f"user-agent={user_agent}")
    options.add_argument("--headless")  # Uncomment to run headless
    #options.add_argument("window-size=1920,1080")
    options.add_argument("window-size=3440,1440")
    
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome(options=options)

    try:
        url_recommended = "https://www.jumia.com.ng/catalog/?q=airtags"
        driver.get(url_recommended)

        # Initialize data collection list
        data = []
        x = 0
        sleep(10)
        driver.save_screenshot('screenshot.png')
        # Loop through pages
        while x < 4:
        # while True:
            # Ensure products are loaded
            WebDriverWait(driver, 60).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'article.prd._fb.col.c-prd'))
            )

            # Fetch product elements
            products = driver.find_elements(By.CSS_SELECTOR, 'article.prd._fb.col.c-prd')
            for product in products:
                print("getting product data")
                name = product.find_element(By.CSS_SELECTOR, '.name').text
                price = product.find_element(By.CSS_SELECTOR, '.prc').text
                old_price = (product.find_element(By.CSS_SELECTOR, '.old').text 
                             if product.find_elements(By.CSS_SELECTOR, '.old') else 'No old price')
                rating = (product.find_element(By.CSS_SELECTOR, '.stars._s').text 
                          if product.find_elements(By.CSS_SELECTOR, '.stars._s') else 'No rating')
                product_image = product.find_element(By.CSS_SELECTOR,'div.img-c > img').get_attribute('src')
                data.append([name, price, old_price, rating, product_image])

            logging.info(f"Scraped {len(products)} products from Jumia.")
            # Scroll and click the next page button
            try:
                next_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.pg[aria-label="Next Page"]'))
                )
                # Scroll into view
                driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
                sleep(2)  # Allow time for scrolling
                driver.execute_script("arguments[0].click();", next_button)  # JavaScript click
                print("Next button clicked")
                print(x)
                x +=1
                # sleep(10)  # Wait for the page to load
                
            except Exception as e:
                print(f"Failed to click next button: {e}")
                break

        # Convert data to DataFrame and save as CSV
        df = pd.DataFrame(data, columns=['Name', 'Price', 'Old Price', 'Rating', 'Product Image'])
        df.to_csv(raw_scraped_data, index=False, encoding='utf-8')

    except Exception as e:
        logging.error(f"Error occurred during scraping: {e}")

    finally:
        logging.info("Scraping process completed. Closing the driver.")
        driver.quit()

# jumia_recommended()