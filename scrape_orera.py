from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup
driver = webdriver.Chrome()
driver.get("https://rera.odisha.gov.in/projects/project-list")
wait = WebDriverWait(driver, 10)

# Wait for project cards to load
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "project-card")))

# Process only the first 6 projects
for i in range(6):
    print(f"\n➡️ Processing project {i + 1}...")

    try:
        # Re-fetch project cards each time to avoid stale references
        projects = driver.find_elements(By.CLASS_NAME, "project-card")
        project = projects[i]

        # Find and click the "View Details" button
        view_button = WebDriverWait(project, 10).until(
            EC.element_to_be_clickable((By.XPATH, ".//a[contains(text(), 'View Details')]"))
        )
        driver.execute_script("arguments[0].click();", view_button)

        # Wait for detail page to load
        wait.until(EC.presence_of_element_located((By.ID, "mainContent")))
        time.sleep(1.5)

        # --- Extract from Project Overview ---
        try:
            project_name = driver.find_element(By.XPATH, "//label[contains(text(),'Project Name')]/following-sibling::*[1]").text
        except:
            project_name = "N/A"

        try:
            rera_reg_no = driver.find_element(By.XPATH, "//label[contains(text(),'RERA Regd. No.')]/following-sibling::*[1]").text
        except:
            rera_reg_no = "N/A"

        # --- Navigate to Promoter Details ---
        try:
            promoter_tab = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Promoter Details')]"))
            )
            promoter_tab.click()
            time.sleep(1.5)
        except:
            print("❌ Could not open Promoter Details tab.")

        # --- Extract from Promoter Details ---
        try:
            company_name = driver.find_element(By.XPATH, "//label[contains(text(),'Company Name')]/following-sibling::*[1]").text
        except:
            company_name = "N/A"

        try:
            office_address = driver.find_element(By.XPATH, "//label[contains(text(),'Registered Office Address')]/following-sibling::*[1]").text
        except:
            office_address = "N/A"

        try:
            gst_no = driver.find_element(By.XPATH, "//label[contains(text(),'GST No.')]/following-sibling::*[1]").text
        except:
            gst_no = "N/A"

        # Print the extracted information
        print(f" RERA Reg. No.: {rera_reg_no}")
        print(f" Project Name: {project_name}")
        print(f" Promoter Name: {company_name}")
        print(f" Promoter Address: {office_address}")
        print(f" GST No.: {gst_no}")

        # Go back to listing page
        driver.back()
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "project-card")))

    except Exception as e:
        print(f"❌ Failed to process project {i + 1}: {e}")

# Done
print("\n✅ Finished scraping first 6 projects.")
driver.quit()
