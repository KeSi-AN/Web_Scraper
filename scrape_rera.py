
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://rera.odisha.gov.in/projects/project-list")

        await page.click("button:has-text('Projects Registered')")
        await page.wait_for_timeout(4000)

        projects = []

        view_buttons = await page.query_selector_all("button:has-text('View Details')")
        view_buttons = view_buttons[:6]

        for i in range(6):
            await view_buttons[i].click()
            await page.wait_for_selector("#projectName")

            data = {
                "Project Name": await page.locator("#projectName").text_content(),
                "RERA Regd. No": await page.locator("#reraRegNo").text_content(),
                "Promoter Name": await page.locator("#promoterName").text_content(),
                "Promoter Address": await page.locator("#promoterRegAddress").text_content(),
                "GST No": await page.locator("#promoterGST").text_content(),
            }
            projects.append(data)

            await page.go_back()
            await page.click("button:has-text('Projects Registered')")
            await page.wait_for_timeout(2000)
            view_buttons = await page.query_selector_all("button:has-text('View Details')")
            view_buttons = view_buttons[:6]

        await browser.close()

        for i, project in enumerate(projects, 1):
            print(f"\nProject {i}:")
            for key, val in project.items():
                print(f"{key}: {val}")

asyncio.run(main())
