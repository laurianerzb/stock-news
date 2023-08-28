# Stock News Notifier

![App Screenshot]()

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Author](#author)

## Description
This program fetches stock price data and news articles related to a given stock, 
and sends notifications via Twilio SMS if certain conditions are met.


## Requirements
- Python 3.x
- Twilio Account: You need a Twilio account with a valid account_sid and auth_token.
- requests library (`pip install requests`)
- twilio library (`pip install twilio`)
- Alpha Vantage API key

## Features
- Stock Price Analysis: The script retrieves daily stock price data for a specified stock 
using the Alpha Vantage API. It calculates the price difference between the most recent 
two days and determines whether the stock price has gone up or down.

- News Article Retrieval: The script fetches news articles related to the specified company 
using the News API. It filters articles based on the company name and provides headlines 
and descriptions.

- Automated Notifications: If the percentage difference in the stock price exceeds a certain 
threshold, the script sends SMS notifications using Twilio. 

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/laurianerzb/stock-news.git
2. Navigate to the project directory:
   ```bash 
   cd stock-news
3. Run the program
   ```bash
   python main.py
4. install the requests and twilio libraries
    ```bash
    pip install requests twilio requests

## Author
- [laurianerzb](https://github.com/laurianerzb)
