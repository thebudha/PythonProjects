from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
import csv
import time

# Setup Selenium WebDriver
service = Service()
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=options)

# Load the page
driver.get("https://www.lotterypost.com/results/nc/megamillions/past")
time.sleep(3)  # Wait for full page text

# Cutoff for 90 days ago
cutoff = datetime.now() - timedelta(days=90)
results = []

# Grab all lines of visible text
lines = driver.find_element(By.TAG_NAME, "body").text.split("\n")

for line in lines:
    if "Mega Ball:" in line:
        try:
            # Parse line like: "Friday, July 11, 2025  12 23 24 31 56 Mega Ball: 1"
            date_part = line.split("  ")[0].strip()  # Double space splits date from numbers
            numbers_part = line.split("Mega Ball:")[0].split("  ")[1].strip()
            mega_ball = line.split("Mega Ball:")[1].strip()

            # Parse date
            draw_date = datetime.strptime(date_part, "%A, %B %d, %Y")
            if draw_date < cutoff:
                continue

            main_nums = numbers_part.split()
            if len(main_nums) == 5:
                results.append([draw_date.strftime("%Y-%m-%d")] + main_nums + [mega_ball])
        except Exception as e:
            print(f"Skipped a line due to error: {e}")

driver.quit()

# Write to CSV
with open("nc_megamillions_last_90_days.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Date", "Num1", "Num2", "Num3", "Num4", "Num5", "MegaBall"])
    writer.writerows(results)

print(f"Saved {len(results)} draws to nc_megamillions_last_90_days.csv")
