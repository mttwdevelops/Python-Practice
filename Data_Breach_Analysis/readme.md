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

### Socially Engineered Into Your Systems

Another interesting breach method is social engineering, where an employee of an entity is psychologically manipulated into divulging sensitive information or performing actions in favor of an intruder. In __[this case](https://www.cyberscoop.com/social-engineering-hack-judge-rules-poor-contract-wont-save-american-hosting-company-lawsuits/)__, someone was able to convince the hosting service of an online community website xat.com to be added to the website's own account (on the host) and take control of their servers, downloading account information, and then finally then wipe them. This attack resulted in over 6 million data records to be leaked.

Social engineering tends to be known from specific examples such as phishing attacks, scareware, and online impersonation. 

Some recommendations to combatting social engineering include:
1. Use multi-factor authentication when using any online account. Scammers may have your password, but if they do not have access to authorize your account through your set up authenticator application, then they cannot get access to that account - still change your password though.
2. Be skeptical of every link in an email. If an email is asking for you to log into your account and they include a link, it's often just better to navigate to the site with a link you have used before or looking up the website and navigating to it rather than clicking links. In that regard, **be skeptical of every email you get..**
3. Use common sense. Often times, you don't even need any external antivirus software if you exercise a health dose of common sense.
4. **Often times scammers can specifically target individuals to scam based off of publicly-available information, such as where you work, live, or who you associate with. This is called Spear-Phishing. Be cautious of what you put online, even showing up in an old photo wearing a shirt with a company's logo can be used to identify you. Scammers are creative, great hackers moreso than what you can expect.**

### The Facebook Problem

Yes, this is the part of any security / privacy report that tells you to get rid of Facebook.

Of any company, Facebook (now Meta), has had over 864,500,000 records leaked since 2013 within five different breaches, with __[Statista reporting](https://www.statista.com/statistics/272014/global-social-networks-ranked-by-number-of-users/)__ that Facebook still has over 2.9 billion monthly active users worldwide, with them also owning WhatsApp, Instagram, and Facebook Messenger (also highly used social media platforms). These breaches stem from two different ways: poor security, and records being "accidentally published." It should be noted that from the collected publicly-sourced data, Facebook leaked records are ***two-thirds*** of total social media record leaks since 2004.

Facebook being hacked does not come as a surprise, as it contains as a single entity the largest registry of publically-volunteered information collection on a significant portion of the entire world's population. This social platform transcends international borders, collecting email addresses, phone numbers, and location data while also performing __[facial recognition](https://web.archive.org/web/20160605165148/http://www.theregister.co.uk/2015/11/10/facebook_scans_camera_for_your_friends/)__, __[snooping on phone calls and texts not made on Facebook through "metadata"](https://www.theguardian.com/technology/2018/mar/25/facebook-logs-texts-and-calls-users-find-as-they-delete-accounts-cambridge-analytica)__, among *many* other intrusive instances found __[here](https://stallman.org/facebook.html#privacy)__.

These actions to gather massive amounts of data on individual users, coupled with Facebook's record of being hacked, is a prime example of the social trend of temporary convenience over true security along with the commercialization of social connection. 

Arguments against purging Facebook come from the idea of its convenience, while true, comes at a significant price. 

There are a few recommendations I propose in its place:
1. Switching to SMS / texting. While any company that deals with anything related to cell-phones are not to be trusted either, as they provide your information to the government (as evidenced from Edward Snowden's leaks and even further back), removing any potential points of privacy-failure is better. **Side note: it would be ideal to use a gpg-encrypted messaging app instead of SMS, but regardless removing any separate-entity traces of your data is better than none.** Before deleting social media, privately offer any connection on social media your contact information, if they never reach out after, then that connection was never meant to be.
2. Being much more conscious and careful about what you put online. Even "spoofing," or faking personal information is okay, but these social media apps still collect your geolocation and sell them to third-parties. This is often stipulated in the Terms of Service (ToS) that you also often skip reading. Faking specific account information but linking it to an email that contains your true identifiable information is a bit awash.