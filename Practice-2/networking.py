## This is a program for scraping information from websites
## Information such as text, links, images, tables...
##

def Webscrapper():

                # Accept user input for domain or IP address
                 url = input("Enter the domain or IP address: ")

                 print("Select a technique:")
                 print("1. HTML Parsing")
                 print("2. Regular Expressions")
                 technique = input("Enter the technique number: ")

                # The type of data to be extracted
                 print("Select the type of data to be extracted:")
                 print("1. Text")
                 print("2. Links")
                 print("3. Images")
                 print("4. Tables")
                 data_type = input("Enter the data type number: ")

                 # The for techniques to employ
                 print("Select techniques to employ (maximum 2):")
                 print("1. Limit Requests (Rate and Frequency)")
                 print("2. Use of Proxies")
                 print("3. Randomize User-Agent")
                 print("4. Session Management")
                 techniques = input("Enter the technique numbers separated by a comma (e.g., 1,2): ").split(",")

                 # Initialize empty dictionary for storing scraped data
                 scraped_data = {}

                 # Perform web scraping based on user selections
                 if technique == '1':
                     # HTML Parsing
                     if '1' in techniques:
                         # Limit Requests (Rate and Frequency) technique
                         rate_limit = int(input("Enter the rate limit (in seconds): "))
                         frequency_limit = int(input("Enter the frequency limit (in requests per minute): "))
                         time.sleep(rate_limit)
                         time_elapsed = 0
                         request_count = 0
                         start_time = time.time()

                         response = requests.get(url)
                         soup = BeautifulSoup(response.content, 'html.parser')
                         if data_type == '1':
                             # Extract text
                             text = soup.get_text()
                             scraped_data['text'] = text
                         elif data_type == '2':
                             # Extract links
                             links = [link.get('href') for link in soup.find_all('a')]
                             scraped_data['links'] = links
                         elif data_type == '3':
                             # Extract images
                             images = [image.get('src') for image in soup.find_all('img')]
                             scraped_data['images'] = images
                         elif data_type == '4':
                             # Extract tables
                             tables = [str(table) for table in soup.find_all('table')]
                             scraped_data['tables'] = tables

                     elif technique == '2':
                         # Regular Expressions
                        if '1' in techniques:
                            # Limit Requests (Rate and Frequency) technique
                            rate_limit = int(input("Enter the rate limit (in seconds): "))
                            frequency_limit = int(input("Enter the frequency limit (in requests per minute): "))
                            time.sleep(rate_limit)
                            time_elapsed = 0
                            request_count = 0
                            start_time = time.time()

                        response = requests.get(url)
                        data = response.text
                        if data_type == '1':
                            # Extract text
                            text = re.findall(r'<[^>]*>([^<]+)<[^>]*>', data)
                            scraped_data['text'] = text
                        elif data_type == '2':
                            # Extract links
                            links = re.findall(r'<a\s+href=["\'](.*?)["\']', data)
                            scraped_data['links'] = links
                        elif data_type == '3':
                            # Extract images
                            images = re.findall(r'<img\s+src=["\'](.*?)["\']', data)
                            scraped_data['images'] = images
                        elif data_type == '4':
                            # Extract tables
                            tables = re.findall(r'<table[^>]*>(.*?)</table>', data, re.DOTALL)
                            scraped_data['tables'] = tables

                            # Save scraped data to a JSON file
                     with open('scraped_data.json', 'w') as json_file:
                         json.dump(scraped_data, json_file)

                         # Print status message
                     print("Scraping completed. Data saved in 'scraped_data.json' file.")

# This is a program for scanning ports of a computer
# Port Scanner
