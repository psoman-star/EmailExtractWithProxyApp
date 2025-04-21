from googlesearch import search
from socket import timeout
import http
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import URLError, HTTPError
import random
import os
import time
import sqlite3
from sqlite3 import Error
import sys
import re
from fake_useragent import UserAgent
from socket import timeout
from urllib.error import HTTPError, URLError
from datetime import datetime
import csv



def extractUrl(url):
	try:
		print ("Searching emails... please wait")

		count = 0
		listUrl = []

		req = urllib.request.Request(
    			url, 
    			data=None, 
    			headers={
        		'User-Agent': ua.random
    		})

		try:
			conn = urllib.request.urlopen(req, timeout=10)

		except timeout:
			raise ValueError('Timeout ERROR')

		except (HTTPError, URLError):
			raise ValueError('Bad Url...')

		status = conn.getcode()
		contentType = conn.info().get_content_type()

		if(status != 200 or contentType == "audio/mpeg"):
			raise ValueError('Bad Url...')

		html = conn.read().decode(conn.headers.get_content_charset())

		emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}', html)

		for email in emails:
			if (email not in listUrl and not email.endswith(imageExt)):
				count += 1
				print(str(count) + " - " + email)
				listUrl.append(email)
				if(searchEmail("Emails.db", email, "Especific Search") == 0):
					insertEmail("Emails.db", email, "Especific Search", url)

		print("")
		print("***********************")
		print(str(count) + " emails were found")
		print("***********************")

	except KeyboardInterrupt:
		input("Press return to continue")
		menu()

	except Exception as e:
		print (e)
		input("Press enter to continue")
		menu()

def extractUrl(url):
	print ("Searching emails... please wait")
	print ("This operation may take several minutes")
	try:
		count = 0
		listUrl = []
		req = urllib.request.Request(
    			url, 
    			data=None, 
    			headers={
        		'User-Agent': ua.random
    		})

		try:
			conn = urllib.request.urlopen(req, timeout=10)

		except timeout:
			raise ValueError('Timeout ERROR')

		except (HTTPError, URLError):
			raise ValueError('Bad Url...')

		status = conn.getcode()
		contentType = conn.info().get_content_type()

		if(status != 200 or contentType == "audio/mpeg"):
			raise ValueError('Bad Url...')

		html = conn.read().decode(conn.headers.get_content_charset())
		
		emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", html)
		print ("Searching in " + url)
		
		for email in emails:
			if (email not in listUrl and not email.endswith(imageExt)):
					count += 1
					print(str(count) + " - " + email)
					listUrl.append(email)
					if(searchEmail("Emails.db", email, "Especific Search") == 0):
						insertEmail("Emails.db", email, "Especific Search", url)

		soup = BeautifulSoup(html, "lxml")
		links = soup.find_all('a')

		print("They will be analyzed " + str(len(links) + 1) + " Urls..." )
		time.sleep(2)

		for tag in links:
			link = tag.get('href', None)
			if link is not None:
				try:
					print ("Searching in " + link)
					if(link[0:4] == 'http'):
						req = urllib.request.Request(
							link, 
							data=None, 
							headers={
							'User-Agent': ua.random
							})

						try:
							f = urllib.request.urlopen(req, timeout=10)

						except timeout:
							print("Bad Url..")
							time.sleep(2)
							pass

						except (HTTPError, URLError):
							print("Bad Url..")
							time.sleep(2)
							pass

						status = f.getcode()
						contentType = f.info().get_content_type()

						if(status != 200 or contentType == "audio/mpeg"):
							print("Bad Url..")
							time.sleep(2)
							pass
						
						s = f.read().decode('utf-8')

						emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", s)

						for email in emails:
							if (email not in listUrl and not email.endswith(imageExt)):
								count += 1
								print(str(count) + " - " + email)
								listUrl.append(email)
								if(searchEmail("Emails.db", email, "Especific Search") == 0):
									insertEmail("Emails.db", email, "Especific Search", url)

			
				except Exception:
					pass
		
		print("")
		print("***********************")
		print("Finish: " + str(count) + " emails were found")
		print("***********************")
		input("Press return to continue")
		

	except KeyboardInterrupt:
		input("Press return to continue")
		

	except Exception as e:
		print(e)
		input("Press enter to continue")
		


def extractFraseGoogle(frase, cantRes):
	print ("Searching emails... please wait")
	print ("This operation may take several minutes")
	try:
		listUrl = []
		listEmails = []

		for url in search(frase, stop=cantRes):
			listUrl.append(url)

		for i in listUrl:
			try:
				req = urllib.request.Request(
							i, 
							data=None, 
							headers={
							'User-Agent': ua.random
							})
				try:
					conn = urllib.request.urlopen(req)
				except timeout:
					print("Bad Url..")
					time.sleep(2)
					pass
				except(HTTPError, URLError):
					print("Bad Url..")
					time.sleep(2)
					pass

				status = conn.getcode()
				contentType = conn.info().get_content_type()

				if(status != 200 or contentType == "audio/mpeg"):
					print("Bad Url..")
					time.sleep(2)
					pass

				html = conn.read()

				soup = BeautifulSoup(html, "lxml")
				links = soup.find_all('a')

				print("They will be analyzed " + str(len(links) + 1) + " Urls..." )
				time.sleep(2)

				for tag in links:
					link = tag.get('href', None)
					if link is not None:
    					# Fix TimeOut
						searchSpecificLink(link, listEmails, frase)
		
			except urllib.error.URLError as e:
				print("Problems with the url:" + i)
				print(e)
				pass
			except (http.client.IncompleteRead) as e:
				print(e)
				pass
			except Exception as e:
				print(e)
				pass
		
		print("")
		print("*******")
		print("Finish")
		print("*******")
		input("Press return to continue")


	except KeyboardInterrupt:
		input("Press return to continue")


	except Exception as e:
		print(e)
		input("Press enter to continue")
	
		




