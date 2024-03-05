# LinkedIn Saved Items Scraper

This Python script allows you to scrape your saved items from LinkedIn and save them to a CSV file. The intended use is to facilitate access to your saved items, making it easier to filter and access the content compared to LinkedIn's interface, where items are often buried in infinite scrolls.
Once your CSV file is ready, upload it to the [Linkedin Library App](https://linkedin-library.streamlit.app/) and enjoy your content! 

## How to Use

1. **Clone the Repository**: Clone this repository to your local machine.

2. **Install Dependencies**: Ensure you have Python installed on your machine. Install the required Python packages by running:
    ```
    pip install -r requirements.txt
    ```

3. **Set Up Chromedriver**: Download the appropriate chromedriver executable for your system and specify its path in the script.

First, find out [which version of Chrome](https://www.lifewire.com/check-version-of-chrome-5222040) you are using. Let's say you have Chrome 72.0.3626.81.

Take the Chrome version number, remove the last part, and append the result to URL "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_". For example, with Chrome version 72.0.3626.81, you'd get a URL "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_72.0.3626".

Use the URL created in the last step to retrieve a small file containing the version of ChromeDriver to use. For example, the above URL will get your a file containing "72.0.3626.69". (The actual number may change in the future, of course.)

Use the version number retrieved from the previous step to construct the URL to download ChromeDriver. With version 72.0.3626.69, the URL would be "https://chromedriver.storage.googleapis.com/index.html?path=72.0.3626.69/"

5. **Run the Script**: Execute the script from the command line, providing your LinkedIn username, password, and desired output path for the CSV file. For example:
    ```
    python scrape_linkedin.py --driver_path /path/to/chromedriver --username your_username --password your_password --output_path /path/to/output.csv
    ```

6. **Access Your Saved Items**: Once the script completes execution, you can find your saved items stored in the CSV file specified by the `output_path` argument.

## Enjoy your content on Linkedin Library App

Go to [Linkedin Library](https://linkedin-library.streamlit.app/) and upload your CSV

## Contributions

This project is based on data scraping and may return incomplete data or you may encounter bugs.
Happy to hear from your feedbacks or ideas to improve the project, feel free to [reach out](https://www.linkedin.com/in/manuel-cellier-821325166/).
