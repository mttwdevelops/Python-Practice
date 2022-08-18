# Data Base Breach Analysis

@mttwdevelops

August 18, 2022

## Project Overview

The topic of this analysis is on largely-public database breaches recorded between the years of 2004 to now. 

The scope of this analysis is to look at different variables from the data such as *Organization type*, *Method*, *Records*, and *Year* to identify any common patterns or interesting outliers, and propose ways that consumers can minimize further leaks of their consumer data.

It is important that I stress that one can *minimize* the ways that one can be hacked but whether or not an entity gets hacked is often out of the hands of just a single consumer. This means that one cannot *entirely prevent* getting their personal information leaked, unless they exist totally "off the grid." Suggestions will be provided at the latter portion of the report.

The scraper file is provided in the **Code and Resources Used** section, and can be run at any time before running this file to get an up-to-date listing of publically-published data breaches. 

For any further questions on the data source's sources, refer to the provided **Data Source** link provided.

For any further questions on the analysis, refer to the provided **db_analysis.ipynb** file provided.

## Code and Resources Used

**Data Source**: https://en.wikipedia.org/wiki/List_of_data_breaches

**Source Scraper**: https://github.com/mttwdevelops/Practice-Files/blob/master/Data_Breach_Analysis/db_breach_webscrape.py

**IDE and Language**: Visual Studio Code, Python Version 3.9.2

**Full Analysis Notebook**: [NEED LINK HERE FOR .IPYNB]

## Data Cleaning

I imported the dataset, and removed the 'Unnamed' and 'Sources' columns, as the first is just a repeated index and the second does not include the links in the Pandas dataframe object. I then set the 'Records' column to be a numeric, eliminating non-numeric values. This also removed vague values such as "unknown," "tens of thousands," or "millions," although these entries are more uncommon. At this point, the data does not need to be touched-up much.

## Exploratory Data Analysis

add method and year photos

## Findings

