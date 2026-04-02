import os
from playwright.sync_api import sync_playwright

def verify_website():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Get absolute path for the local HTML file
        file_path = "file://" + os.path.abspath("Showcase_Website/index.html")
        print(f"Opening: {file_path}")
        
        page.goto(file_path)
        page.wait_for_load_state('networkidle')
        
        # Capture screenshot for visual verification (simulated for agent)
        screenshot_path = "Showcase_Website/preview.png"
        page.screenshot(path=screenshot_path, full_page=True)
        print(f"Screenshot saved to: {screenshot_path}")
        
        # Print page title and main headings to verify content
        print(f"Page Title: {page.title()}")
        headings = page.locator("h1, h2, h3").all_text_contents()
        print(f"Headings found: {headings}")
        
        browser.close()

if __name__ == "__main__":
    verify_website()
