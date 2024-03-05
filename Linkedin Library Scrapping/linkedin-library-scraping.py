import argparse
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

def scrape_linkedin(driver_path, username, password, output_path):
    driver = webdriver.Chrome(service=Service(driver_path))
    url = "https://www.linkedin.com"
    driver.get(url)
    
    driver.find_element(By.XPATH, '/html/body/main/section[1]/div/div/form/div[1]/div[1]/div/div/input').send_keys(username)
    driver.find_element(By.XPATH, '/html/body/main/section[1]/div/div/form/div[1]/div[2]/div/div/input').send_keys(password)
    driver.find_element(By.XPATH,'/html/body/main/section[1]/div/div/form/div[2]/button').click()
    
    driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div/div[2]/div/div/div/div/div[1]/a[2]/span').click()
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    linkedin_library = soup.find_all("li", {"class": "reusable-search__result-container"}) 
    
    output = []
    for saved_item in linkedin_library:
        saved_item_output = {}
        author = saved_item.find('span', attrs={'aria-hidden': 'true'}).text 
        profile_pic_link = saved_item.findAll('img')[0]['src'] 
        saved_item_output = ({'author': author,
                      'profile_pic_link': profile_pic_link}) 
        potential_paragraphs = saved_item.findAll('p')  
        for p in potential_paragraphs:
            if not p.get('class') or 't-black--light' not in p.get('class'):
                content_post = p.get_text(separator="\n", strip=True)
                saved_item_output['post_content'] = content_post
        if len(saved_item.findAll('img')) > 1:
            optional_post_pic_link = saved_item.findAll('img')[1]['src']
            saved_item_output['optional_post_pic_link'] = optional_post_pic_link
        output.append(saved_item_output)
    
    output_df = pd.DataFrame(output)
    output_df.to_csv(output_path, index=False)

def main():
    parser = argparse.ArgumentParser(description="Scrape LinkedIn saved items")
    parser.add_argument("--driver_path", required=True, help="Path to chromedriver executable")
    parser.add_argument("--username", required=True, help="LinkedIn username")
    parser.add_argument("--password", required=True, help="LinkedIn password")
    parser.add_argument("--output_path", required=True, help="Output CSV file path")
    args = parser.parse_args()

    scrape_linkedin(args.driver_path, args.username, args.password, args.output_path)

if __name__ == "__main__":
    main()
