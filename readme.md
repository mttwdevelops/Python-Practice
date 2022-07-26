Purpose of this repo is to upload different test files created as I learn Python and other languages. I also keep a daily log (on days I do something) here and will track any further progress on both learning and towards getting a job.

Task List:
- [X] [July 22] Complete Python Developer in 2022: Zero to Mastery
- [ ] 100 Days of Python Projects
- [ ] SQL - MySQL for Data Analytics and Business
- [ ] Tableau 2020 A-Z

Started on June 09, 2022.

@mttwdevelops

## July 26, 2022
Today's focus is on deepwork, or getting things done rather than worrying about getting them done while constantly looking at the clock. I removed the clocks in my room and computer and turned my phones off to help focus. I'll updated this entry with how it goes. 

The project course has many days that focus on GUIs and non-data science related tasks, all of which are important at building Python and other library skills, but not what I should be focusing on. In light of that, I'm going from finishing day 25 and going straight for day 45, which focuses on BeautifulSoup, which I experimented before from the ZtM course, found [here](https://github.com/mttwdevelops/Practice-Files/blob/master/Scape.py) or on July 19th's entry. Today's practice files can be found [here](https://github.com/mttwdevelops/100-Days-of-Code/tree/master/Day_26_BeautifulSoup_Practice), and the project for today is scraping a movie list and printing and outputing it in a new file. It can be found [here](https://github.com/mttwdevelops/100-Days-of-Code/tree/master/Day_26_BeautifulSoup_Practice/MoviesProject).

I also worked on the SQL course, finishing sections four and five. This means I've installed MySQL, and created my first database. Working files will be updated and uploaded [here](https://github.com/mttwdevelops/SQL_Course).

In addition to this, I also began reading and finished chapter one of [this book](https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/), which Ken Jee recommends and builds off of what I learned so far. I want to learn more about Scikit-Learn and get into the "TensorFlow" that seems pretty hot in the machine learning community. "Neural nets" seem pretty cool too, let's see where this goes.

## July 25, 2022
I started today off by picking more online seminars and talks to attend, all of them on breaking into tech and AI related things. 

I also completed day 25 of the 100 projects course, practice for pandas is [here](https://github.com/mttwdevelops/100-Days-of-Code/tree/master/Day_25_Pandas_Practice), but the project itself is [here](https://github.com/mttwdevelops/100-Days-of-Code/tree/master/us-states-game-start).

Then, I completed sections one through three of the SQL course, which covered the basics of the theory and terminology. Some important notes include:
- Databases should be relational, or use "relationship algebra" to separate large volumes of data into more efficient queries for users.
- Primary keys is a column or a set of columns that are unique identifiers in a table they cannot contain null or missing values
- Foreign keys are used to identify relationships between tables
- Unique keys are similar to primary keys in the sense that they have unique values, but can contain null or missing values

## July 22, 2022
Job update: I didn't get the job I interviewed for and mentioned previously, but I'm not upset or stressing about it. It wasn't purely data science or analytics so it would have been a nice paying stepping stone but oh well.

I wrapped up the machine learning section and finished the ZtM course, the files for the ML practice can be found [here](https://github.com/mttwdevelops/Practice-Files/tree/master/MachineLearningPractice). I am also starting the SQL course now; I'm thinking it'll take a week or two to finish completely.

At this point, I'm going to continue working on machine learning and with the tools mentioned before. I also started watching [Ken Jee's YouTube](https://www.youtube.com/c/KenJee1), and started with [this video](https://www.youtube.com/watch?v=I3FBJdiExcg). The whole project is based off of [Kaggle's Titanic competition](https://www.kaggle.com/competitions/titanic), and I'll keep looking over different submissions' code to see what they're doing through what cleaning processes and tools they are using, along with their statistical and analytical methodology. 

## July 21, 2022
I finished and uploaded a regression analysis project in R, which can be found [here](https://github.com/mttwdevelops/Regression-Analysis-Boston-Historic-Housing-Prices). This focuses on data collected from Boston neighborhoods in 1970, and while the [original paper](https://www.researchgate.net/publication/4974606_Hedonic_housing_prices_and_the_demand_for_clean_air) the data was used for measured median home values based off of air quality, I focused on what specific variables are signficant in the data and built a forward regression model. I also updated my resume, deleting the actuarial exam portion and focusing more on work experience and projects, like the regression model I just uploaded. More goodies to come!

I continued with the ZtM videos on data science and machine learning. Here are some things I learned:

Data science and AI intersect at several points, and machine learning is one of them.

Steps to Machine Learning:
1. Importing data
2. Cleaning the data (missing entries / columns)
3. Splitting data into training and testing sets
4. Create a model (importing an algorithm from a library typically)
5. Check the output
6. Improve the model (extra input / data or change the model)

Tools for Machine Learning:
- **Numpy** is for multi-dimensional arrays
- **Pandas** is for data reading and database structuring
- **Scikit** is for algorithms
- **Matplotlib** is for visualizing data
- **Jupyter notebooks** lets us step through code, pretty much the same as Rmarkdown
- **Kaggle** is for datasets for all of our tools

## July 20, 2022
I was having issues with yesterday's [Scrape.py](https://github.com/mttwdevelops/Practice-Files/blob/master/Scape.py) file, as it would turn out, I was using 'storylink' rather than 'titlelink', which was resulting in empty lists to be returned for the link variable. This issue is now fixed. 

I'm now at the machine learning section of the ZtM course, and am about ~80% done with the course. I feel more confident with my python skills, but the road is much longer to land a job. 

## July 19, 2022
I continued with section seventeen of the ZtM course, specifically focusing on PDFs and sending automated emails. The library used for the PDF automation is [PyPDF2](https://pypdf2.readthedocs.io/en/latest/index.html), and the code I worked on is merging PDFs and also adding a [watermark](https://pypdf2.readthedocs.io/en/latest/user/add-watermark.html#watermark-underlay); the folder can be found [here](https://github.com/mttwdevelops/Practice-Files/tree/master/pdf-playground). The automated email process was not working since Google authentication was being a pain, but here is the [file](https://github.com/mttwdevelops/Practice-Files/blob/master/email-playground/email_sender.py). I also got to the [compromised password checker](https://replit.com/@mttwdevelops/passwordchecker#check.py) and uploaded it onto repl.it, since vscode was not working properly with the requests library.

I also skipped the twitter and sms automation bots since I'm focusing on web scraping, which is the data collection part that leads to data analysis (section eighteen). My sense of wanting to complete things rather than just take what is needed and move on can bog down my progress a bit, but I am slowly getting deeper into data science. The main package for data scraping is called [beautiful soup](https://beautiful-soup-4.readthedocs.io/en/latest/), which pulls data from HTML and XML files. With the video lectures from the ZtM course I am currently trying to select news posts on [Hacker News](https://news.ycombinator.com/) that have over 100 upvotes, [here](https://github.com/mttwdevelops/Practice-Files/blob/master/Scape.py) is the file.

## July 18, 2022
I began today with reviewing my work in file IO, lambda functions, and decorators. I then finished half of section seventeen of the ZtM course, which puts me at about 70% completion. Section seventeen focuses on scripting, which is something I needed to learn, as scripting has many different applications like PDF scraping, bot writing, and automated messages. My first program with scripting is converting .jpg to .png files. The folder to that project is [here](https://github.com/mttwdevelops/Practice-Files/tree/master/images-playground).

I had also begun working around with Jupyter notebooks, how they work, and their formatting. My [test notebook](https://github.com/mttwdevelops/Practice-Files/blob/master/TestNotebook.ipynb) tried basic syntax, along with matplotlib graphing for the [facebook csv](https://github.com/mttwdevelops/Practice-Files/blob/master/facebook.csv) I kept from the financial analysis course.

## July 15, 2022
I spent today reviewing the code for the past week, mainly the file IO from project day 24, 14, and decorators. I finished section seven and eleven from ZtM, which focuses on functional programming (opposite of OOP) and modules respectively.

I also covered:
1. **Lambda functions** are one-time, anonymous functions that can replace longer for loops or functions. They can also be used in list, set, and dictionary comprehension for the same reasons.

I also began to review my previous R projects and am drafting up a new linear regression project. I'm looking at [UCI's machine learning repository](https://archive.ics.uci.edu/ml/index.php) and [Kaggle](https://www.kaggle.com/) for datasets. I'm also looking at [Ken Jee](https://www.kaggle.com/kenjee)'s portfolio and will try his datasets and code files to see how a professional documents and models.

## July 14, 2022
I continued on the ZtM course, and finished the section on [decorators](https://github.com/mttwdevelops/Practice-Files/blob/master/Decorators_Exercise.py) and on [map, filter, and reduce functions](https://github.com/mttwdevelops/Practice-Files/blob/master/MapFilterReducePractice.py). 

## July 13, 2022
I have spent the past bit more on the project course, but since I have moved on from OOP from the project course I should delve much further into specific topics that I want to cover or think are interesting rather than just keep laying other topics which I *may* use instead of want to, doing so would kill my drive to continue practicing. In that spirit, I watched the lectures on contributing to open source and a bit more on git, which offered a nice refresher and showed me ways to solve merge conflicts. I also covered more file IO videos. I am now little over the halfway mark in total content completion for the ZtM course. Another thing that is mentioned is the 'why' I do what I do, and while I know that I should be asking myself these questions, it's good to remind myself since I can also forget. Everything I do should be for the bigger picture of my life and making the time I have left meaningful rather than just leaving an impact anywhere without any direction.

My bigger picture is to further build my statistical analysis skills so I can make actionable reports for my work. Programming is a means to doing my analytical work.

I should also begin to spend time working on projects in R, since I haven't touched it too much since graduating back in May. I'm scrapping up to run another linear regression analysis project, akin to what I did during undergrad. More to come.

## July 11, 2022
I completed day [twenty four](https://github.com/mttwdevelops/100-Days-of-Code/tree/master/Mail%20Merge%20Project) of the projects course, which focused on the file directory and path. This one was a bit more difficult, and I did make a jump in content from day fifteen/sixteen to twenty four, which means I skipped content. This challenge was interesting, and I'll be sure to revisit it.

## July 8, 2022
I completed day [fourteen](https://github.com/mttwdevelops/100-Days-of-Code/blob/master/HigherLower_Day_14.py) and have moved on to the OOP (and intermediate) portion of the online course. At this point, I feel my programming is coming along and I'm more comfortable in Python, and I need to keep up with my R now to make sure I don't lose it. I'm also thinking of jumping around in the course to find interesting topics and working on those instead of just going sequentially, this will help keep interest while also making sure I learn more interesting topics. 

## July 7, 2022
Finally finished the [Blackack simulator](https://github.com/mttwdevelops/100-Days-of-Code/blob/master/Blackjack_Day_11.py) and also completed day [twelve](https://github.com/mttwdevelops/100-Days-of-Code/blob/master/GuessNumber_Day_12.py), which is a number guessing game that works on declaring functions. I also started working on the last beginner project, which is for day [fourteen](https://github.com/mttwdevelops/100-Days-of-Code/blob/master/HigherLower_Day_14.py).

## July 6, 2022
I continued working on the Blackjack simulator, but still hit bug after bug. I took a break and began working on day [thirteen](https://github.com/mttwdevelops/100-Days-of-Code/blob/master/Debugging_Day_13.py), which is all about debugging practice. It helped a lot with some debugging tips such as print statements, running code after writing it bit by bit rather than writing a bunch of lines only to have a hive of bugs, and visualizing my code through either online editors or through my editor.

## July 5, 2022
I wrapped up day [nine's](https://github.com/mttwdevelops/100-Days-of-Code/blob/master/BlindAuction_Day_9.py) project, which covered dictionaries and how to modify and pull specific elements (its max value). I also completed day [ten](https://github.com/mttwdevelops/100-Days-of-Code/blob/master/Calculator_Day_10.py), which was a calculator that involved dictionaries, recursion, and while loop flags (to allow a program to continue to run while a certain condition remains true). I also started day [eleven's](https://github.com/mttwdevelops/100-Days-of-Code/blob/master/Blackjack_Day_11.py) project, which is a command line version of the game Blackjack. I created functions that check both the user and computer's hands, and also set up basic if-statements for whether the user or computer won a specific hand. 

## July 4, 2022
I took a bit of a break last Friday since I bought tickets to a convention and didn't realize it came up so quickly, so I went during the weekend.

Today's focus is to get back into the swing of things by doing some review of previous code, specifically the object oriented programming and the past few projects I completed, especially after taking three days off. I also completed day [eight](https://github.com/mttwdevelops/100-Days-of-Code/blob/master/CaesarCipher_Day_8.py) for the project course.

No update yet from my final round, but that make sense since today is the fourth, which most companies take off.

## June 29, 2022
Today's focus is to knock out more projects from the 100 Days of Python Projects course until the project material matches what I'm learning from ZtM's course. Because of this, I need to keep working on projects up to day 16's project, where the course finally covers OOP.

I finished day [seven's](https://github.com/mttwdevelops/100-Days-of-Code/blob/master/Hangman_Day_7.py) project, which took a bit longer since I was having a conditional issue that was fixed by going line by line and figuring out how the computer was interpreting my logic. The issue was for the lives deduction code if you guessed a letter wrong (for the game hangman), but I just needed to move the conditional outside a for loop to prevent too many lives from being deducted.

I also spent some time today preparing for my three-round third interview, which is most likely a social talk rather than hardcore technical questions. I'm not stressed, and I think I'll be alright, I see this more as a "does the team like me as a person" rather than a "let's figure out if he's a coding genius."

## June 28, 2022
Job update: I also applied to two more analyst jobs, both of which had pretty vague job requirements but long job requirements. As it would turn out, the second round interview I had yesterday wasn't the last, and they want me to talk to four more people (other directors, actuaries, and data engineers). How fun!

Today I continued with both courses, first starting with the project course to complete days [four](https://github.com/mttwdevelops/100-Days-of-Code/blob/master/RockPaperScissors.py), [five](https://github.com/mttwdevelops/100-Days-of-Code/blob/master/PasswordGenerator.py), and [six's](http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json) projects. 

Since day six's project is through a website, the solution code for that is:
```
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
```
This solves a maze, and I think it's pretty efficiently written. The projects covered the random library, loops, and function declaration, so it wasn't difficult to complete. 

I then finished the object oriented programming lectures from the ZtM course, finishing section six. It covered a bit more on:
1. **Inheritance** allows objects to inherit their parent object features
2. **Abstraction** is meant to hide things from the user, like how I don't need to know how the len() function is coded, I just use it
3. **Encapsulation** packages functions and data that work together into a single object
4. **Private vs Public Variables**
5. **Polymorphism** allows for different objects to use the "same" methods for different purposes
6. **Object Introspection** gives the type of an object at runtime
7. **Dunder methods** are short for "Double underscore" methods and are special methods that can also be declared in a class in order to be altered for whatever reason

## June 27, 2022
Job update: I had a second (and more than likely last round) interview this morning at the same company as June 23's entry, this time speaking to the hiring manager. They emphasized the lack of data analytics and more communciations in the role, which I don't mind, but my endgame is still further than just data communication and checking excel spreadsheets.

I also put some time this weekend to think not only about jobs, but also what I actually want to contribute towards in the grand scheme of my life. I don't want to just be an analyst or scientist; I was also thinking about computer hardware and software security, particularly encryption. 

I also continued watching more zero to mastery lectures and am currently working on object oriented programming within Python. The current lectures overlap and review a lot of material from the video I mentioned in [this practice file](ObjectOrientedPractice.py), but refreshing and reviewing is important. I made updates at the bottom of the file with more practice from the lectures.

I finished section 12 and 16 as well, which goes over debugging and different career aspects. These lectures do help with figuring out more projects I can work on as I continue, and I like the idea of creating other blog posts for different technologies and projects I find interesting. 

## June 23, 2022
Job update: So I just had the interview and I thought it went alright. I was a little bit jittery around some responses, but the interviewer mentioned I should be hearing back by early next week so it doesn't seem bad. Salary was a bit low, but given that it is an entry level, I'm not entirely against taking a little bit of a salary hit if it means I can get the necessary experience, but I'm not setting my standards that low to work for a ridiculously bad salary. Besides that, I'll just keep applying.

I spent today's morning to early afternoon preparing for my interview since this is my first time interviewing in a while, and it's for a non-actuary role. I will be working with actuaries since it's for a life insurance position, so I definitely have a foot in the door with experience, but I'm not going to jinx it. 

Besides that, I continued with another day of the project course, this time completing day 3's [project](https://github.com/mttwdevelops/100-Days-of-Code/blob/master/TreasureIsland.py). I also added project purposes and "scopes" to the other days' projects, which are to show what new skills a program I wrote focuses on.

## June 22, 2022
I finished section 4 of the Developer course, which focused on more advanced basics such as loops, function, *args and **kwargs, among other things. It took about four hours, but I'm now complete with sections 1-5 and am now over a third done with the course, albeit I'm familiar with most of the content so far. 

Some cool things I wasn't as aware about include:
1. **docustrings** (including ''' ''' when defining functions as documentation)
2. ***args and **kwargs**** for when you are not sure how many arguments you throw into your parameters
3. **local vs nonlocal** and **global variables**

I also now have an interview with a health insurance company for a systems analyst job tomorrow, so maybe I'll land an offer sooner than I expected. As far as I can tell from the listing, it doesn't seem like I'll use programming a whole lot compared to Excel, but with how I think certain things in the economy are going, having a decently-paying job to bolster my savings is not looking like a bad idea. Just hope this goes well.

## June 21, 2022
I started my 100 Days of Python Projects course, and completed the exercises until day 3. They just about covered most of what I have learned in the Zero to Mastery course, so I'll work on both courses in tandem (instead of finishing the Zero to Master course and then working on the project course). Most of the code done in the project course was simple variable declaration, so I didn't bother saving it in the repository, rather it was done on [an online Python editor](https://www.online-python.com/). I did create a new [repository](https://github.com/mttwdevelops/100-Days-of-Code) for the first day project of the course, and the code for that project can be found [here](https://github.com/mttwdevelops/100-Days-of-Code/blob/master/BandNameGenerator.py). I also completed the second day, which can be found [here](https://github.com/mttwdevelops/100-Days-of-Code/blob/master/TipCalculatory.py).

## June 20, 2022
Today's focus was on pushing through the Python Developer course's first basics section, which was about 4 hours of videos and readings. I also wrapped up section 2, which was the continuation to the introduction, so in total I have sections 1 - 3 and 5 (of a total of 25) done today. 

Here's a review of what I covered today:
1. Coding basics (variables, data types, expressions vs statements)
    - Data types include:
        - Lists (lots of different methods that can be applied)
        - Matrices (examples are lists within lists and their indexes)
        - Dictionaries (keys are immutable but have a wide range of different values they can take)
        - Tuples (more efficient lists that are immutable)
        - Sets (lists that tend to have only unique entries)
2. Logic and conditionals (the beginning of section 4, which covers more advanced basics)

I also applied to 6 more jobs today, all of which I am confidently qualified for. They're all for data analyst positions, which coincidentally have nearly identical job descriptions and requirements. Hopefully I can hear back from them. 

I'm also going to be trying out more linux distributions, either arch or other gnome distributions (currently on ubuntu). 

## June 17, 2022
I'm having trouble determining what projects to complete or even their scope so to minimize that difficulty I enrolled in some python classes along with a project course to help. I know I do well in an "official" learning environment (or when I feel like I'm in a classroom), so I can manage working in those classes. I've also gone ahead and gotten SQL and Tableau courses too, which I may add to the repository. Here's the current general learning plan:

1. Complete Python Developer in 2022 Course
2. SQL - MySQL for Data Analytics and Business
3. Tableau 2020 A-Z
4. 100 Days of Code (done after the first and during the other courses)

After this, rounding things out with Excel practice should also be good. I feel fine with SQL and Excel since I have working experience with both, but I've already recieved two job rejection emails as of today. Doesn't sting, but I struck much better as an actuary.

I also completed sections 1 and 5 of the Python Developer in 2022 course, which means I went through the course basics and set up Jupyter notebook, which had been an absolute pain to use because I didn't have Anaconda installed. 

## June 16, 2022
I recalibrated my learning priorities today, so I don't just code every day without a general direction, which I can do from time to time. I'm looking at my June 10th entry, which talks about what I should work on to become more advanced and I'm thinking on both PIP and file IO since I need to become more familiar with working with different libraries (along with installing them) and file practice. The [Financial Analysis Coursera code](FinancialAnalysisCoursera.py) I did seems to be a good start for that, since I'm reading in the .csv files and also working with Pandas, so I'll keep going with that course. 

I also went to a data science talk today, which was mainly for networking and just curiosity. I did learn about resources like [Datakind](https://www.datakind.org/) and [all tech is human](https://alltechishuman.org/), which I'll take a longer look at when I have more experience, and it's probably not good to stretch myself out too thin looking too long at everything when I should be focusing on a few things for now. 

## June 15, 2022
Uploaded facebook.csv and microsoft.csv for the [Financial Analysis Coursera code](FinancialAnalysisCoursera.py) I was working on. Getting Jupyter notebooks to work and everything was a little tricky for my first time. I figured how to take the 'head' of a table and open the file with the Pandas package, but have not figured mmatplotlib yet. 

I also finished the entirety of course 1 from the Google Data Analystics course. Looking over the rest of the schedule and coursework for the other courses, it's nearly all things I've done before in a school project or professional setting, so I'll keep it on the side if I need something to keep chipping at. Most of the teachings are *really* beginner level, which is what I wasn't looking for. I did like how the course taught me the process that an analyst would work with data and share their conclusions, which matched my experience as an actuary analyst.

On another note, I have been applying to jobs (about 7 so far), and got rejected from my first one already. I think my experience from looking for actuary internships and jobs has calloused me to the "pain" of professional rejection now. Most of the job listings have been for R and SQL / Excel, which I'm pretty comfortable with and have done before at work and my internship. I'm sure I can find a job now if I just set my standards low enough, but I'll keep going to find something that isn't totally wack. 

## June 13, 2022
I was a bit busy today, but I started and finished weeks 1 and 2 of the [Google Data Analytics course on Coursera](https://grow.google/certificates/data-analytics/). It seems easy enough to do full time, but I skipped a lot of the non-readings and skimmed through the videos since the material isn't non-intuitive (mind the double negative), and I'm familiar with most of it already. Had a lot of other things to take care of, so that's it for today. 

## June 10, 2022
Got back into python learning again, along with committing any changes I made just to practice with the terminal. Since I'm comfortable with most intro things like loops, I'll take a step further into object oriented programming, which can be found [here](ObjectOrientedPractice.py).

I then watched [this](https://www.youtube.com/watch?v=p15xzjzR9j0) video, so I'd place myself in between beginner - intermediate so far. I should cover though:

1. Mutable vs immutable data types
2. File IO
3. Data structures
4. Lambda functions
5. *args and **kwargs
6. Dunder methods (double underscore methods)
7. PIP
8. Splitting code into modules

## June 9, 2022
Just focusing on learning git today. Got setup with vscode and how to incorporate git so I can push updates instead of uploading the files themselves like a caveman. On another note, it feels good to be learning again, and on things I find interesting. Here are some important commands in case I forget:

```
git pull
git add .
git commit -m ""
git push
```

My head hurt after doing this for a few hours so I took the rest of today off.
