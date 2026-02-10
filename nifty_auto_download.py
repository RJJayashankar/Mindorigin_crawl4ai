import asyncio
import os
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode

async def download_multiple_indices():
    # --- 1. YOUR LINKS ---
    urls = [
       "https://www.niftyindices.com/indices/equity/sectoral-indices/nifty-psu-bank"
    ]

    # --- 2. SETUP FOLDER ---
    download_folder = os.path.join(os.getcwd(), "nifty_downloads")
    os.makedirs(download_folder, exist_ok=True)
    
    # --- 3. BROWSER CONFIG ---
    browser_cfg = BrowserConfig(
        headless=True,            # Keep this True usually
        accept_downloads=True,
        downloads_path=download_folder
    )

    # --- 4. SMARTER CLICK LOGIC ---
    # Instead of looking for a specific title, we look for any link containing 'Constituent'
    js_click_code = """
    const links = Array.from(document.querySelectorAll('a'));
    const downloadBtn = links.find(el => el.textContent.includes('Constituent') || el.title.includes('Constituent'));
    
    if (downloadBtn) {
        downloadBtn.click();
    } else {
        console.log("Could not find a link with 'Constituent' in text.");
    }
    """

    # --- 5. RUN CONFIG ---
    run_cfg = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        # ERROR FIX: Changed from specific button to just 'body' to prevent timeouts
        wait_for="css:body",       
        js_code=js_click_code,
        # Keep browser open for 5s after click to ensure download starts
        delay_before_return_html=5.0 
    )

    print(f"🚀 Starting downloads to: {download_folder}\n")

    # --- 6. EXECUTION ---
    async with AsyncWebCrawler(config=browser_cfg) as crawler:
        for url in urls:
            name = url.split('/')[-1]
            print(f"Processing: {name} ...") 
            
            try:
                # We simply run the crawler; errors are caught in the try/except block
                result = await crawler.arun(url=url, config=run_cfg)

                # Check if we got files
                if result.downloaded_files:
                     print(f"   ✅ Downloaded: {os.path.basename(result.downloaded_files[0])}")
                else:
                    # Sometimes the file downloads but isn't instantly reported in 'result'
                    # We check if the file actually exists in the folder
                    expected_files = [f for f in os.listdir(download_folder) if name.replace('-', '') in f.lower() or 'constituent' in f.lower()]
                    if expected_files:
                        print(f"   ✅ Found file in folder (Manual check)")
                    else:
                        print(f"   ⚠️ Page loaded, but file not detected.")

            except Exception as e:
                print(f"   ❌ Error processing {name}: {e}")

    print("\nAll tasks completed.")

if __name__ == "__main__":
    asyncio.run(download_multiple_indices())