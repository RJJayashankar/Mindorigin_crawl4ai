# Mindorigin_crawl4ai 🕷️📈

A robust Python automation script designed to scrape and download **Index Constituent** CSV files from the [Nifty Indices](https://www.niftyindices.com/) website.

This project leverages **Crawl4AI** (powered by Playwright) to handle dynamic JavaScript content, ensuring reliable downloads even when button IDs or page layouts change.

---

## 🚀 Key Features

- **Multi-URL Support**: Define a list of sectoral URLs (Auto, Bank, IT, etc.) to download multiple indices in a single run.
- **Smart Link Detection**: The script dynamically searches for links containing the text "Constituent," making it resilient to website updates.
- **Headless Operation**: Runs efficiently in the background without opening visible browser windows.
- **Auto-Organization**: Automatically creates and manages a `nifty_downloads` folder to store all retrieved files.

---

## 📋 Prerequisites

- **Python 3.7+**
- **pip** (Python package installer)
- **venv** (Always install in venv)

---

## 🛠️ Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/RJJayashankar/Mindorigin_crawl4ai.git
   cd Mindorigin_crawl4ai

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

3. **Install Browser Engines**

   Critical Step: This downloads the Chromium engine required for the scraping engine to function.

   ```bash
   crawl4ai-setup

---

## 🏃‍♂️ Usage

1. **Configure URLs**: Open `nifty_auto_download.py` and update the `urls` list with the pages you want to scrape:

   ```python
   urls = [
       "https://www.niftyindices.com/indices/equity/sectoral-indices/nifty-auto",
       "https://www.niftyindices.com/indices/equity/sectoral-indices/nifty-bank",
       "https://www.niftyindices.com/indices/equity/sectoral-indices/nifty-it"
   ]

2. **Run the Script**:
   ```bash
   python nifty_auto_download.py

3. **Check Output**: The script will create a folder named `nifty_downloads` and save all CSV files there.

---

## ⚙️ Configuration

You can tweak the script behavior inside `nifty_auto_download.py`:

- **Download Path**: Modify the `download_folder` variable to change where files are saved.
- **Wait Time**: Adjust `delay_before_return_html` (default: 5.0 seconds) if you have a slower internet connection.
- **Debug Mode**: Set `headless=False` in `BrowserConfig` to watch the browser perform actions in real-time.

---


