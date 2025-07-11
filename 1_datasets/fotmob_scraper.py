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


def get_player_details(player_url, desired_season):
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(options=chrome_options)

    # First navigate to the domain to set cookies
    driver.get("https://www.fotmob.com")

    # Add all the cookies
    cookies = [
        {
            "domain": ".fotmob.com",
            "name": "_ga",
            "value": "GA1.1.904699775.1752246312",
            "path": "/",
        },
        {
            "domain": ".fotmob.com",
            "name": "_ga_G0V1WDW9B2",
            "value": "GS2.1.s1752246311$o1$g0$t17522463" "22$j60$l0$h1604236803",
            "path": "/",
        },
        {
            "domain": ".fotmob.com",
            "name": "_hjSession_2585474",
            "value": (
                "eyJpZCI6IjU5ZDFiMmIxLTUxMWUtNDBjMi1"
                "iNjBjLTkyZDFlYmFiYTYyYSIsImMiOjE3"
                "NTIyNDYzMTE5NDksInMiOjAsInIiOjAsIn"
                "NiIjowLCJzciI6MCwic2UiOjAsImZzIjox"
                "LCJzcCI6MX0="
            ),
            "path": "/",
            "secure": True,
        },
        {
            "domain": ".fotmob.com",
            "name": "_hjSessionUser_2585474",
            "value": (
                "eyJpZCI6ImE0ZmJiMTA2LTIyOTEtNTIyMi1h"
                "MzdmLTI1YTQ2ZWVjNzFhYSIsImNyZWF0ZWQiOjE"
                "3NTIyNDYzMTE5NDgsImV4aXN0aW5nIjpmYWxzZX0="
            ),
            "path": "/",
            "secure": True,
        },
        {
            "domain": ".fotmob.com",
            "name": "FCCDCF",
            "value":(
                "%5Bnull%2Cnull%2Cnull%2C%5B%22CQUY0gAQUY0gAEsAC"
                "BENBzFoAP_gAEPgABpwLItD_C7dbWFDyL53absEeIhHx"
                "_hjasQwAAbBA2AFTBqQsJQWwmE4NAyCtCACGAAAKmTBIQ"
                "IkCAAAAUAAIIAVIADMAAyQIBAIICBAiAEBAEBIAEACCoA"
                "gUQCIgIJEFEQAmAwEQJKAWFCAiAAAAEChKAAAABAYAYKI"
                "AAEAZAAAEQIAUCgAEQIAiAjAAAEIABAIAAgAAAQAIBEAB"
                "AgAABAQQAgBAAADgoQGABAOMBABIcgEAgACCyLQfwu3W1"
                "hR8i4V2G7BDiIV8f4A2rEMAAGwQNgBUwakLCEFtJhMiRI"
                "gjAgABgAACJkQSAAKAAIAABAAQCAFSAAzAAMECAQCCBgQ"
                "IAhAUBAQABAAgqAIFEAiYCCRBREAIkMBECSgFhQgAgAIC"
                "BAoSgAAAAQGAGCAAABAGAAAAAiANAAAhACAIgIwAAAAAA"
                "QCBAIAAAEACARAAQIAAAQMEAAAQAAA4KEBgAACjAQACDI"
                "AAIAAgAA.cAAAD_wAAAA%22%2C%222~61.70.89.93.108."
                "122.149.184.192.196.228.230.236.259.311.313.314."
                "318.323.358.385.415.442.445.469.486.494.495.540."
                "550.574.576.723.864.981.1029.1031.1033.1046.1047."
                "1048.1051.1067.1092.1095.1097.1126.1166.1205.1276."
                "1301.1329.1342.1365.1415.1449.1512.1514.1516.1558."
                "1570.1577.1598.1616.1626.1651.1677.1716.1720.1725."
                "1735.1753.1765.1782.1870.1878.1889.1917.1942.1958."
                "1960.1967.1969.1985.1987.2010.2068.2069.2072.2074."
                "2107.2137.2213.2219.2223.2224.2253.2299.2312.2316."
                "2328.2331.2343.2373.2387.2411.2415.2416.2440.2501."
                "2506.2510.2526.2531.2535.2567.2568.2571.2572.2575."
                "2577.2624.2642.2657.2677.2686.2767.2778.2822.2869."
                "2874.2878.2887.2898.2908.2920.2929.2963.2973.3005."
                "3023.3100.3126.3130.3135.3155.3163.3173.3182.3219."
                "3234.3235.3244.3253.3290.3299.3309.3324.3330.3331."
                "3731.4131.6931.8931.9731.13731.14332.15731.27831."
                "45931~dv.%22%2C%22A4040322-DF8E-4997-8247-8D7159"
                "43DAE7%22%5D%5D"
            ),
            "path": "/",
        },
        {
            "domain": ".fotmob.com",
            "name": "FCNEC",
            "value": (
                "%5B%5B%22AKsRol-JmN4QCrePYRl17nPjbMPiel8dU"
                "nhjRKmFQK-LiF-P54yr8RbIHCJ0BhJT7LkSrtFH"
                "PpGTH57FA_HZhR1UyW2vNS90k-wH6y7WqItAf4AP-"
                "73wQkXIujqR6oPClrdtbkyWcokxZJUR-Qxd79_v"
                "r79Wxm9Byw%3D%3D%22%5D%5D"
            ),
            "path": "/",
        },
        {
            "domain": "www.fotmob.com",
            "name": "u:location",
            "value": (
                "%7B%22countryCode%22%3A%22DE%22%2C%22region"
                "Id%22%3A%22HE%22%2C%22ip%22%3A%22"
                "127.0.0.1%22%2C%22ccode3%22%3A%22DE"
                "U%22%2C%22ccode3NoRegion%22%3A%22DEU%22%2C"
                "%22timezone%22%3A%22Europe%2FBerlin%22%7D"
            ),
            "path": "/",
        },
    ]

    for cookie in cookies:
        driver.add_cookie(cookie)

    # Now navigate to the actual player URL
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

        # Switch to "Per 90" stats view
        try:
            per_90_button = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//button[contains(text(), "Per 90")]')
                )
            )
            per_90_button.click()

            # Wait briefly for stats to reload after switching to "Per 90"
            wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'div[class*="DetailedStatsCSS"]')
                )
            )
        except Exception as e:
            print("⚠ Could not switch to Per 90 stats:", e)

        soup = BeautifulSoup(driver.page_source, "html.parser")

    finally:
        driver.quit()

    player_data = {"URL": player_url}

    # Extract Birth Date only (ignore age)
    try:
        bio_items = soup.select(
            "div.css-qpoljv-BioContainerCSS div.css-1u6v53x-Play"
            "erBioStatCSS, div.css-1spuxeo-PlayerBioStatCSS"
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
            "div.css-qpoljv-BioContainerCSS div.css-1u6v53x-Pla"
            "yerBioStatCSS, div.css-1spuxeo-PlayerBioStatCSS"
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

        # Player average rating
    try:
        rating_blocks = soup.select("div[class*=StatBox]")
        for box in rating_blocks:
            label = box.find("span", class_=lambda c: c and "StatTitle" in c)
            value = box.find("div", class_=lambda c: c and "PlayerRatingCSS" in c)
            if label and "rating" in label.get_text(strip=True).lower() and value:
                player_data["Average Rating"] = value.get_text(strip=True)
                break
    except Exception as e:
        print("Rating parsing error:", e)

    return player_data


if __name__ == "__main__":
    player_urls = [
        "https://www.fotmob.com/players/299981/pablo-mari",
        "https://www.fotmob.com/players/540088/ollie-watkins",
        "https://www.fotmob.com/players/729731/matty-cash",
        "https://www.fotmob.com/players/1137668/moises-caicedo",
        "https://www.fotmob.com/players/891855/jakub-moder",
        "https://www.fotmob.com/players/642230/andi-zeqiri",
        "https://www.fotmob.com/players/1065940/michal-karbownik",
        "https://www.fotmob.com/players/974618/jan-paul-van-hecke",
        "https://www.fotmob.com/players/304455/joel-veltman",
        "https://www.fotmob.com/players/818975/eberechi-eze",
        "https://www.fotmob.com/players/883075/nathan-ferguson",
        "https://www.fotmob.com/players/662936/ben-godfrey",
        "https://www.fotmob.com/players/1104441/niels-nkounkou",
        "https://www.fotmob.com/players/185236/joshua-king",
        "https://www.fotmob.com/players/299572/terence-kongolo",
        "https://www.fotmob.com/players/662428/antonee-robinson",
        "https://www.fotmob.com/players/683402/tosin-adarabioyo",
        "https://www.fotmob.com/players/956161/joe-gelhardt",
        "https://www.fotmob.com/players/671529/konstantinos-tsimikas",
        "https://www.fotmob.com/players/424609/ben-davies",
        "https://www.fotmob.com/players/614006/ruben-dias",
        "https://www.fotmob.com/players/835409/nahuel-lautaro-bustos",
        "https://www.fotmob.com/players/1109171/yan-couto",
        "https://www.fotmob.com/players/1108884/diego-rosa",
        "https://www.fotmob.com/players/1099974/issa-kabore",
        "https://www.fotmob.com/players/612836/donny-van-de-beek",
        "https://www.fotmob.com/players/428672/alex-telles",
        "https://www.fotmob.com/players/1073402/facundo-pellistri",
        "https://www.fotmob.com/players/864983/jamal-lewis",
        "https://www.fotmob.com/players/841150/rhian-brewster",
        "https://www.fotmob.com/players/609504/oliver-burke",
        "https://www.fotmob.com/players/492589/max-lowe",
        "https://www.fotmob.com/players/789646/jayden-bogle",
        "https://www.fotmob.com/players/1035202/ismaila-coulibaly",
        "https://www.fotmob.com/players/938539/ibrahima-diallo",
        "https://www.fotmob.com/players/717174/joe-rodon",
        "https://www.fotmob.com/players/586467/karlan-grant",
        "https://www.fotmob.com/players/522651/matheus-pereira",
        "https://www.fotmob.com/players/760398/cedric-kipre",
        "https://www.fotmob.com/players/31306/branislav-ivanovic",
        "https://www.fotmob.com/players/491883/said-benrahma",
        "https://www.fotmob.com/players/524437/tomas-soucek",
        "https://www.fotmob.com/players/307317/vladimir-coufal",
        "https://www.fotmob.com/players/1024169/frederik-alves-ibsen",
        "https://www.fotmob.com/players/1050158/fabio-silva",
        "https://www.fotmob.com/players/1010733/ki-jana-hoever",
        "https://www.fotmob.com/players/1013277/toti-gomes",
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
        if "Birth Date" in keys:
            keys.remove("Birth Date")
        fieldnames = ["URL", "Birth Date"] + keys

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
