# Project: Company Data Collection from Annual Reports

## Project Overview

This project involves developing a set of Scrapy spiders to gather company information from different stock exchanges listed on the Annual Reports website. Each spider is tailored to a specific exchange and retrieves data based on predefined starting URLs.

## Project Structure

The project includes the following Scrapy spider classes:

- `AimSpider`: Targets the AIM exchange
- `AmexSpider`: Targets the Amex exchange
- `AsxSpider`: Targets the ASX exchange
- `LseSpider`: Targets the LSE exchange
- `PdfSpider`: Targets the NASDAQ exchange
- `NyseSpider`: Targets the NYSE exchange
- `OtcSpider`: Targets the OTC exchange
- `TsxSpider`: Targets the TSX exchange
- `TsxVSpider`: Targets the TSX Venture exchange

Each spider class starts by navigating to its designated start URL, which contains a list of companies. Using CSS selectors within the parse method, the spiders scrape company names and their corresponding links. These links direct to the "Most Recent Annual Report" section for each respective company, providing access to their annual reports.
## Data Processing Functions

The project includes the following data processing functions:

- `compare_data(file_name, file2='forbes')`: Compares data from JSON files obtained from Annual Reports and another source (typically Forbes), creating a new JSON file with company matches.
- `compare_json_file(files: list)`: Merges data from JSON files containing company information from different exchanges into a single consolidated JSON file.

## Important
This project is for educational purposes only.
Before using, ensure you have permission to gather and use data from the Annual Reports website or any other sources from which you retrieve information.

