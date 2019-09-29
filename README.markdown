## Introduction
Sophie,

Good job! you made it this far!  Hopefully this opened in Chrome (or whatever browser you use, but the script I made is configured for Chrome.  Let me know if you use something else).  

There are a few things you might have to install.  I'll run through those later.  For now, to run the script, just follow the instructions in the instructions section.  

---

## Instructions
I'm assuming that I remembered to install all of the right things on your computer.  

1. Open a terminal window (⌘ + Space, then type "terminal" in the spotlight window.  I would highly recommend putting the terminal in to your dock if you are planning on becoming a CS student.  You use it a lot).  

2. Navigate to the directory that has the Python scripts in them using the `cd` command.  If you opened a new terminal window, you will probably have to run this command a few times.  If you type the first few letters of the folder name, you can use the tab key to auto-complete it.  

3. Run the `ls` command.  You should see this file (README.markdown), as well as a backup folder, and some .py files.  The .py files are the important ones.  

4. If you want to scrape for the new ticket site, run `python3 scrape.py`.  This will run the scaper script that finds the id of the new ticket buying page, and it will automatically update the config file to reflect the new id.  If you want, I can run this on my computer at home.  Remember to update `data.json` and `config.json` with the right details (like a credit card number and the right name and stuf).  You ned to update these two files <strong>EXACTLY</strong> like they are shown before you edit them.  You can also use textedit to edit them, although I recommmend getting a good text editor like Visual Studio Code, or use the built-in one called Vim (although it was made around the time when Dad graduated from college, so it's a little old and kind of clunky).  

5. Once you have the right id for the page in config.json, you can now run `python3 tickets.py`, which will buy one ticket for you.  As of right now, the website will have to be active or it will crash your computer eventually, but it buys the tickets really fast.  

6. If the script doesn't work, text me immediately.  I can run it from my desktop from almost anywhere, so in an emergency, I have a folder set up that has all of the right data included in the thing.  Also, your data is <strong>NOT</strong> secure in this, so don't share any of these files with others for right now.  It's ok to buy tickets for your friends, but DONT share these files with anyone.  


## Terminal Basics
Think of the terminal window as a shitty version of Finder that is actually way better than anything that Finder could ever do.  The terminal is always in a "folder" on your computer, and a lot of commands depend on the folder that you are working in.  I'll try to find you a good website that can explain the terminal better than I can.  If you get good at using the terminal, people will think you're a super good hacker and shit like that, even if all you do is `ls` and list all of the files in a directory.  

---

## Helpful Terminal Commands
Here are a few helpful terminal commands and what they do.  

`cd <folder>`: This changes the directory that the terminal window is currently in to a different directory.  It defaults to `~`, which is your home directory `/Users/Sophie/`.  To go to a folder, replace `<folder>` with the name of the folder (don't include the brackets!).  

`ls`: this command lists all of the files in the current directory.  You can run `ls -a` to list all of the files (even hidden ones!), and `ls -G` to make the files pretty colors.  The little flags (like `-a` and `-G`) are case sensitive btw

`brew install <package name>`: brew is a package manager for MacOS that lets you install cool things that other people have made for you.  It's a way of getting more terminal utilities without having to make them yourself.  You shouldn't need this to use the scripts right now, but you might need it in the future if I use more things.  These are called "Dependencies", and they are usually listed in a document in the Git repository for a project.  

`pwd`: Shows you the path to the folder you're in right now from the root directory (where everything begins).  This is useful for telling others how to get there.  Remember that `~`  is equiavlent to `/Users/Sophie/` or whatever your user name is. 


## Other Notes
<strong>Seriously</strong> don't run the buy script more than once.  It *should* work, but if it doesn't, <strong>**please**</strong> don't immediately exit the window.  Take a screenshot (command + shift + 4), and then continue buying tickets.  The script is fast enough such that it will at least get you most of the way there.  


## Dependencies
- You will need the following:
- git ( I installed this on your computer when I visited SC for family weekend)
- Homebrew (I also refer to this as `brew`, this was also installed when I visited)
- Python 3 and pip (same as above, these will need to be updated by running `brew upgrade python3` and `pip install --upgrade pip` to update pip (which is like brew but for Python packages only))
- selenium (this is installed through pip, running `pip install selenium` and updating by running `pip install --upgrade selenium`)
- ChromeDriver: You can install this by running `brew cask install chromedriver`.  You need this to let the automation work since I was lazy and didn't acutally automate anything myself, I made a testing tool do it for me instead.  

---
That should be it.  In most cases, if you get an error message, screenshot it and send it to me.  
