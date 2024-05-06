# Introduction

This project was developed as a complement to [The Complete Python Developer](https://www.udemy.com/course/complete-python-developer-zero-to-mastery/) course I've recently finished, with my own modifications and additions. The program scrapes the information from [Hacker News](https://news.ycombinator.com/), filters out the posts above 100 likes and uses [Speech Synthesis](https://pypi.org/project/pyttsx3/) to read the titles of the posts. 

<br/>

# Requirements

For convenience a requirements.txt file is provided in the config, to use it run the following command:

<p align="center">
    <img width="640" src="https://raw.githubusercontent.com/dumiii/image-processing/master/images/install.png" alt="Download Instructions">
</p>

<br/>

# Usage

The program takes in a number of pages and scrapes the data from all of them, simply pass it as an argument when executing:

<p align="center">
    <img width="640" src="https://raw.githubusercontent.com/dumiii/web-scraping/master/images/usage.png" alt="Executing the Program">
</p>

After the information is processed the titles will be read one by one until the end. Unfortunately the speech quality is not very good, I have considered using a different library such as [Google Text-to-Speech (gTTS)](https://pypi.org/project/gTTS/) but due to several errors and limitations this was not a viable solution. Definitely worth looking more into this in the future, perhaps come up with a better version.

<br/>

# Credits

[The Complete Python Developer](https://www.udemy.com/course/complete-python-developer-zero-to-mastery/) for the original script, [Hacker News](https://news.ycombinator.com/) for all the scraped data, [Speech Synthesis](https://pypi.org/project/pyttsx3/) for the text-to-speech and credits for the awesome instruction images go to [Carbon](https://carbon.now.sh/).