# Database Breach Analysis

@mttwdevelops

August 18, 2022

## Project Overview

The topic of this analysis is on largely-public database breaches recorded between the years of 2004 to now. 

The scope of this analysis is to look at different variables from the data such as *Organization type*, *Method*, *Records*, and *Year* to identify any common patterns or interesting outliers, and propose ways that consumers can minimize further leaks of their consumer data.

It is important that I stress that one can *minimize* the ways that one can be hacked but whether or not an entity gets hacked is often out of the hands of just a single consumer. This means that one cannot *entirely prevent* getting their personal information leaked, unless they exist totally "off the grid." Suggestions will be provided at the latter portion of the report.

The scraper file is provided in the **Code and Resources Used** section, and can be run at any time before running this file to get an up-to-date listing of publically-published data breaches. 

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

For all findings, refer to the **Full Notebook**.

### The Inside Jobs

Insider jobs, or when an individual inside an entity, either willingly or un/knowingly releases internal information, either through documents, cached customer records, or otherwise. This means that not all of the records that fall under the "inside job" category are malicously released, in fact, besides the previously mentioned Wikileaks government and military document releases, police filings and other government documents are often published unintentionally.

Of course, there are instances of financial incentives, such as the largest inside job within the dataset: AOL's database leak in 2004. __[This databreach](https://money.cnn.com/2004/06/23/technology/aol_spam/)__ occured from a software engineer whole stored a list comprising of 92 million AOL customers usernames and sold them for advertising purposes. Other similar cases include 20 million entries from the South Korean Credit Bureau, and 2.5 million entries from Countrywide Financial Corp.

But what I find most interesting are the moral reasons why an inside job happens. One that can be found within the data source is from Wikileaks, a 'public service' website that posts government documents meant to educate journalists, activists, and the general public on any internal government (typically US) activities. Or rather, insider "whistleblowers" release these documents to Wikileaks, who verify and publish them online. These entries can take up a smaller number of records, with the U.S. Army's classified Iraq War documents and embassy cables leaks totaling to only 0.52% of 'inside job' records. 

### The Facebook Problem

Of any company, Facebook (now Meta), has had over 1,064,500,000 records leaked since 2013 within five different breaches, with __[Statista reporting](https://www.statista.com/statistics/272014/global-social-networks-ranked-by-number-of-users/)__ that Facebook still has over 2.9 billion monthly active users worldwide, with them also owning WhatsApp, Instagram, and Facebook Messenger (also highly used social media platforms). These breaches stem from two different ways: poor security, and records being "accidentally published." It should be noted that from the collected publicly-sourced data, Facebook leaked records are ***over two-thirds*** of total social media record leaks since 2004.

Facebook being hacked does not come as a surprise, as it contains as a single entity the largest registry of publically-volunteered information collection on a significant portion of the entire world's population. This social platform transcends international borders, collecting email addresses, phone numbers, and location data while also performing __[facial recognition](https://web.archive.org/web/20160605165148/http://www.theregister.co.uk/2015/11/10/facebook_scans_camera_for_your_friends/)__, __[snooping on phone calls and texts not made on Facebook through "metadata"](https://www.theguardian.com/technology/2018/mar/25/facebook-logs-texts-and-calls-users-find-as-they-delete-accounts-cambridge-analytica)__, among *many* other intrusive instances found __[here](https://stallman.org/facebook.html#privacy)__.

## What Can Be Done For Your Digital Security

In summary, and in order:
1. Use common sense. So little needs to be done if used.
2. Delete Facebook and any subsidiary apps.
3. Delete user accounts that are not used. The fewer accounts you have, the fewer headaches, advertising emails, and accounts intruders can get access too. You'd be surprised how many accounts you generate over the years, and how few of them you regularly use. When any company asks about deleting your data, **you do live in California, and they must comply with [CCPA](https://oag.ca.gov/privacy/ccpa)**.
4. Set up an offline password manager, such as [KeepassXC](https://keepassxc.org/), and change passwords into 20+ length randomized characters / numbers. This ensures that one password to an account will not compromise another, even if there is a breach. [Here is a starting guide](https://www.youtube.com/watch?v=Bpc3EEQ-GoA).
5. Be more conscious of your activity online, along with anything that could be liked to you. Think before you post whether or not you include any uniqely identifiable information.


### What Can Be Done For Your Digital Privacy

This is one step further than the previous list.

1. You don't need to sign up for many services, especially retail. They often are just not worth the security risk and are just ads in your email. The data they collect as well makes them prime targets for breaches.
2. Cash is king. Banks and credit cards generate a lot of metadata that can be traced, and this is prime for ads. These entities socially engineer you to make purchasing decisions through bonus-point and cash-back deals. And forget about online investment websites, [brokers sell data about your trades](https://dailycaller.com/2021/02/02/robinhood-hedge-funds-citadel-order-flows-gamestop-stock-market/).
3. Be skeptical of any email you recieve. Links, attached files, and even the account they are contacting you with can be compromised.
4. Rid yourself of any social media at all. These webs of social connection can be used to link others to yourself, and that can make you prime for spear-phishing attacks.
5. Analog just works. Avoid "smart" products such as appliances, as they also collect massive amounts of data on your home and activities, with or without your full consent. 
6. For those that don't know already, use a VPN to tunnel network activity, and don't forget about the adblock.