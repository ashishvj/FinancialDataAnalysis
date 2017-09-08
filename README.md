# FinancialDataAnalysis
I am writing this as a part of a tutorial series on http://kengroo.com
and also as a way to enhance my own programming and algorithm development
experience.

This script has been written in Octave, but should also be compatible with MATLAB (not tested)


### file: fin_data_analysis_p1.m
This is the first script written in this series.
This script, scrapes NASDAQ.com to get a singular value i.e current stock price
(See http://kengroo.com/data-analysis-financial-data-analysis-part-1/ for description)

The stock that is being checked is defined by the variable ticker
ticker=["AAPL"];

The output generated is printed to the command window looks like this

    Stock price for AAPL on 2017-09-07 12:39:15 = 161.1801
    >>

### file: fin_data_analysis_p2.m
This is an update to the p1 file. Added extraction of more parameters from the NASDAQ website
i.e Today's High/ Low, 52-week High/Low, Net change and Net percentage change

Planned updates

- [x] Add previous close, (added in fin_data_analysis_p2.m) 
- [x] Add todays high/low, (added in fin_data_analysis_p2.m)   
- [x] Add 52 Week High low, (added in fin_data_analysis_p2.m)
- [x] Add net change, percent change in stock price (added in fin_data_analysis_p2.m)
- [ ] Incorporte checking stock price for multiple stocks
- [ ] Pull historical data.
- [ ] Store data locally (database?)
- [ ] Check if data exists, so that there is no need to scrape data from the NASDAQ website everytime,
- [ ] Visual data representation of stock price fluctuation and volume for 1 day, 5 day, 1 month, 6 month, 1 year (and maybe more)
- [ ] Add error catching and testing functionality

If you have any suggestions on what changes or updates could be made feel free to reach out to me at ashishvjagtiani AT gmail.com

