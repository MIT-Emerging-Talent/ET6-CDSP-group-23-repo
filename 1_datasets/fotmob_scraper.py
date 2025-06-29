"""
This module provides a data scraping script, that can access Fotmob.com's
API and take player statistics based on the desired season.
Created on: 2025/06/29
@author: Hamidullah Rajabi
"""

import csv

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def get_player_details(player_url, desired_season="2022/2023"):
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(player_url)

    wait = WebDriverWait(driver, 10)

    try:
        # Click season dropdown
        season_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[class*="SeasonText"]'))
        )
        season_button.click()

        season_option = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f'//optgroup[@label="{desired_season}"]/option')
            )
        )
        season_option.click()

        wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div[class*="DetailedStatsCSS"]')
            )
        )

        soup = BeautifulSoup(driver.page_source, "html.parser")

    finally:
        driver.quit()

    player_data = {"URL": player_url}

    # Extract Birth Date only (ignore age)
    try:
        bio_items = soup.select(
            "div.css-qpoljv-BioContainerCSS div.css-1u6v53x-PlayerBioStatCSS, div.css-1spuxeo-PlayerBioStatCSS"
        )
        for item in bio_items:
            value_div = item.find("div", class_="css-to3w1c-StatValueCSS")
            title_div = item.find("div", class_="css-10h4hmz-StatTitleCSS")
            if value_div and title_div:
                age = value_div.get_text(strip=True)
                birth_date = title_div.get_text(strip=True)
                if "year" in age.lower() and "," in birth_date:
                    player_data["Birth Date"] = birth_date
                    break
    except Exception as e:
        print("Birth date parsing error:", e)

    # Player Name and Team
    try:
        name_elem = soup.find("h1", class_=lambda c: c and "PlayerHeader__Title" in c)
        team_elem = soup.find("a", class_=lambda c: c and "PlayerHeader__TeamLink" in c)
        if name_elem:
            player_data["Name"] = name_elem.text.strip()
        if team_elem:
            player_data["Team"] = team_elem.text.strip()
    except Exception as e:
        print("Name/Team parsing error:", e)

    # Other Bio info (excluding birth date and age)
    try:
        bio_items = soup.select(
            "div.css-qpoljv-BioContainerCSS div.css-1u6v53x-PlayerBioStatCSS, div.css-1spuxeo-PlayerBioStatCSS"
        )
        for item in bio_items:
            value_div = item.find("div", class_="css-to3w1c-StatValueCSS")
            title_div = item.find("div", class_="css-10h4hmz-StatTitleCSS")
            if value_div and title_div:
                key = title_div.get_text(strip=True)
                value = value_div.get_text(strip=True)
                if key == player_data.get("Birth Date"):
                    continue  # skip if it's the birth date we've already captured
                player_data[key] = value
    except Exception as e:
        print("Bio parsing error:", e)

    # Traits
    try:
        trait_sections = soup.select("span[class*=TraitLabel]")
        for trait in trait_sections:
            name_span = trait.select_one("span[class*=TraitText]")
            percent_span = trait.select_one("span[class*=TraitPercentage]")
            if name_span and percent_span:
                trait_name = name_span.get_text(strip=True)
                trait_value = percent_span.get_text(strip=True)
                player_data[f"Trait - {trait_name}"] = trait_value
    except Exception as e:
        print("Trait parsing error:", e)

    # Season Stats
    try:
        current_group = None
        for element in soup.select("div[class*=DetailedStatsCSS] > *"):
            if (
                element.name == "h3"
                and "StatGroupTitle" in element.get("class", [""])[0]
            ):
                current_group = element.get_text(strip=True)

            if "StatItemCSS" in element.get("class", [""])[0]:
                name_elem = element.find("div", class_=lambda c: c and "StatTitle" in c)
                value_elem = element.find(
                    "div", class_=lambda c: c and "StatValue" in c
                )
                if name_elem and value_elem and current_group:
                    stat_name = name_elem.get_text(strip=True)
                    stat_value = value_elem.get_text(strip=True)
                    player_data[f"{current_group} - {stat_name}"] = stat_value
    except Exception as e:
        print("Season stats parsing error:", e)

    try:
        mp_elem = soup.find(
            "div", class_=lambda c: c and "SeasonPerformanceSubtitle" in c
        )
        if mp_elem:
            spans = mp_elem.find_all("span")
            if len(spans) == 2 and "minutes played" in spans[0].text.lower():
                minutes = spans[1].get_text(strip=True)
                player_data["Minutes Played"] = minutes
    except Exception as e:
        print("Minutes played parsing error:", e)

    return player_data


if __name__ == "__main__":
    player_urls = [
        "https://www.fotmob.com/players/901495/albert-sambi-lokonga",
        # Add all other player URLs here
    ]

    desired_season = "2021/2022"  # or any valid season available on the page

    all_data = []

    for url in player_urls:
        print(f"\nScraping: {url}")
        try:
            data = get_player_details(url, desired_season=desired_season)
            all_data.append(data)
        except Exception as e:
            print(f"❌ Failed to scrape {url}: {e}")

    if all_data:
        # Get all unique keys from all players
        keys = set()
        for player_data in all_data:
            keys.update(player_data.keys())
        keys = sorted(keys)

        # Ensure URL is first column and Birthday is early in the order
        if "URL" in keys:
            keys.remove("URL")
        if "Birthday" in keys:
            keys.remove("Birthday")
        fieldnames = ["URL", "Birthday"] + keys

        # Write CSV
        with open(
            "player_data_organized.csv", mode="w", newline="", encoding="utf-8"
        ) as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for player_data in all_data:
                writer.writerow(player_data)

        print("\n✅ CSV saved as 'player_data_organized.csv'")
    else:
        print("⚠ No valid data to write.")
