# Automated Song Downloader through Youtube
# Run this with the name of the song you want to download
# **For spaces use dashes**
# Example: python autoDown.py young-dumb-and-broke
# The example case will download Young Dumb and Broke by Khalid 


import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time

# This function takes the song link as input and goes to the website to download the song
def convertVidtoMP3(songLink):

	driver.get("https://videoconvert.com/")

	elem = driver.find_element_by_xpath('/html/body/header/div/div/div[2]/div/div[2]/form/div[1]/div/input')
	elem.clear()													
	elem.send_keys(songLink)										
	elem.send_keys(Keys.RETURN)		

	check = ' '
	confirmation = "Download"
	while(check != confirmation):
		try:	
			checkTxt = driver.find_element_by_xpath('/html/body/header/div/div/div[2]/div/div[2]/div[2]/div[3]/a')
			check = checkTxt.text
		except:
			check = ''


	link = (driver.find_element_by_xpath('/html/body/header/div/div/div[2]/div/div[2]/div[2]/div[3]/a')).get_attribute("href")
	driver.get(link)



# Get the second element from the input arguement
songName = str(sys.argv[1])

# Iterator and check for spaces
i = 0
spaceCheck = 0

while (i < len(songName)):
	if (songName[i] == '-'):
		spaceCheck = 1
	i = i +1

# If there are spaces split the string by -
if spaceCheck:
	songName = songName.split('-')

# Dashes should be gone and now you an join the name together
songName = ' '.join(songName)
lyrics = ' lyrics'
# Add lyrics to the search in order to prevent getting a music video
songName = songName + lyrics

driver = webdriver.Chrome()
driver.get('https://www.youtube.com/')

elem = driver.find_element_by_xpath('//*[@id="search"]')
elem.send_keys(songName)										# Input item to search for
elem.send_keys(Keys.RETURN)										# Execute

try:	# Try finding different links to get into the Park Site
	link = driver.find_element_by_partial_link_text('Lyric Video')
except:
	link = driver.find_element_by_partial_link_text('Lyrics')

# Pull the link from the hyperlink to the song's video
vidLink = link.get_attribute("href")

# Send to conversion website
convertVidtoMP3(vidLink)

# Wait some time to let download complete and then close
time.sleep(10)
driver.close()
