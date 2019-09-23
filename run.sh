# !/bin/bash

# open new terminal window to make it cleaner to kill the chromedriver instance later
# this is needed since we have to have ChromeDriver running to have selenium do it's thing
if [[ "$OSTYPE" == "linux-gnu" ]]; then
	if dpkg --get-selections | grep -q "^$pkg[[:space:]]*install$" >/dev/null; then
		echo "Package is not installed.  Please install the package";
		apt-get install $pkg;
		
		if apt-get -qq install $pkg; then
			echo "Package $pkg successfully installed"
		else
			echo "Error installing $pkg"
		fi
	fi
	gnome-terminal --window-with-profile=HOLD_OPEN -e chromedriver&
elif [[ "$OSTYPE" == "darwin"* ]]; then
	osascript -e chromedriver
fi


echo "detected OS"

# once chromedriver has started, we can now automatically run python scripts
echo "Beginning webpage scraping"
python ./scrape.py

