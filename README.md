## TITLE:  Clinton Python Projects.
### AUTHOR: Clinton Muthungu Ndegwa.


Hello, Welcome to my space, Am showcasing my personnal python-trials.
I have used simple, medium and complex programs to sharpen my Python knowledge both in theory and practically.

I have a index.py programs categorized based on environment of study.

### index.py.

    Though pip I have installed and used different packages.
    Dependancies to install :
                                
        ~ os
        ~ random
        ~ pyqrcode
        ~ argparse
        ~ time
        ~ dns.revolver
        ~ json
        ~ socket
            
### Do you know Menu Driven Program?.

    It's a type of computer pogram which accepts the input from the user by showing a list of options and users 
    have to select ant of the options to perform any operation.

    I've used functions to illustrate Menu Driven Program, After executing. The compiler will display the list 
    of menu options. The user has to choose the option and enter it.
    
    I have created programs linked together in a Menu Driven Program. The programs are:
    
       ~ Body Mass Index.
       ~ Rock, Paper, Scissors Game.
       ~ Web Scrapper.
       ~ Port Scanner.

Here is a brief documentation of each program. A detailed explaination of each.

### Body-Mass-Index:
    
    This is a tool used to assess a person's body weight in relation to their height.
    It is a simple mathematical calculation that provides an estimate of body fat and
    can be used to determin whether a person is underweight, normal weight, overweight,
    obese.
                      
             The formula for calculating BMI is;
                      
             BMI = weight (kg) / height(m)*height(m).
             Here's a breakdown of the BMI categories:
                       
                ~ Underweight: BMI less than 18.5.
                ~ Normal weight: BMI between 18.5 and 24.9.
                ~ Overweight: BMI between 25 and 29.9.
                ~ Obese: BMI 30 or higher.
                       
    It typically involves a person's weight and height calculation automatically.
    It generates the corresponding BMI valueand provides an interpretation of the
    results based on the established categories.
                      
             Limitations:
                         It doesn't take into account factors such as muscle mass,
                         bone density, or overall body composition.
                                  
                         It doesn't provide information about the distribution of body fat,
                         which can be relevant for assessing health risks associated with 
                         obesity.
        
    The BMI serves as a quick and straightforward method for estimating body weight
    status.
    
    
### Rock, Paper and Scissors.

     This is a simple program that allows the player to enter their choice (Rock, Paper, Scissors) and 
     play against the computer, which randomly selects its choice.
     
     A function compares the choices and determines the winner based on the game rules.
     
     Its run on a Python environment, and it wil keep prompting you for your choice until you type
     'quit' to exit. After each round, it displays the computer's choice and the result.
     
     It can be customized to add more features.

### Web Scarper:
     
     This a software ued to extract data from websites, it acesseses web pages, reads their content, and 
     collects specific information for further analysis and storage.
     
     It can be used to gather various data such as product details, prices, reviews, news arrticles, 
     contact information, and more. It employs different methods and techniquesto extratc data from 
     websites, such as:
                       ~ HTML Parsing:
                                      It uses HTML parsig libraries to navigate through the structure 
                                      of web pages and extract relevant data by locating specific
                                      elements based on their HTML tags, classes, or identifiers.
                                      
                       ~ Regular Expressions:
                                             It uses regular expressions to search for patterns within
                                             the HTML source code and extract desired information, 
                                             usually used when the daya is not easily accessible using
                                             parsing methods.
                                             
                       ~ API Intergration:
                                          Some websites provide APIs that allow direct access to their 
                                          data, it can utilize these APIs to retrieve information in a
                                          structured manner.
                       
                       ~ headless Browsers:
                                           It can employ headless browsers to interact with web pages 
                                           just like a regular user, this enables it to handle dynamic
                                           content, Javascript rendering, and user interactions.
      
      It is possible for website administrators to detect and block web scrapers. Common techniques
      used to detect scrapers are:
                                  ~ IP Address Monitoring.
                                  ~ User-Agent Analysis.
                                  ~ CAPTCHAs and Anti-Scraping Measures.
      
      To avoid detection you can employ techniques such as:
                       
                      ~ Respect Robot.txt:
                                          Chek the websites robots.txt file, which specifies the 
                                          crawling permissions and restrictions. 
                                          
                      ~ Limit Requests:
                                       Control the rate and frequency of your requests to avoid 
                                       overwhelming the target website, mimic human browsing behaviour
                                       by adding delays between requests.
                                       
                      ~ Use Proxies:
                                    Rotate your IP Address or use a pool of proxies to distribute the
                                    the scarping requests among multiple IP addresses.
                                    
                      ~ Randomize User-Agent:
                                             Vary the User-Agent header in your HTTP requests to make it
                                             harder for websites to identify your scraper, use a 
                                             diverse set of User-Agent strings to mimic different browsers
                                             and devices.
                                             
                      ~ Session Management:
                                           Implement session management to handle cookies and session 
                                           identifiers, to allow the scraper to handle login sessions and 
                                           maintain ccontinuity between requests.
     
    
### Port Scanner:
    
     A Port Scanner is a software tool or application that is designed to probe a computer system
     or network for open ports. Ports are communication endpoints that applications use to send
     and recieve data. Each network service or application typically listens on a specific port
     for incoming connections.
                  
     They are used for various purposes, iincluding network security assessments, 
     vulnerability scanning a range of IP addresses or a specific target host for open ports. 
     The Scanner sends connection request to each port and analyzes the response to determine 
     if the port is open, closed, or filtered by a firewall.
                  
     Port Scanners can employ different scanning techniques, such as:
                  
             ~ TCP Connect Scan:
                                This scan attempts to complete the TCP three-way handshake with the
                                target host. If the handshake is successful, the port is considered
                                open.
                          
             ~ SYN Scan: 
                        It sends a SYN packet (the first step of the TCP handshake) to the target
                        port. If the target responds with a SYN-ACK packet, the port is considered
                        open.
                        This technique is often faster than the TCP Connect Scan. Also known as 
                        half-opening scanning.
                 
             ~ UDP Scan: 
                        The Scanner sends a UDP packet to the target port and analyzes the
                        response. If the port responds positively (e.g with an ICMP message or an
                        application-level response), it is considered open.
                 
     Port Scanner provide vairous information about the target system or network, depending on the
     type of scan and the response received.
                  
     Some of the information that can be obtained includes:
                 
              ~ Open Ports: 
                           It can identify which ports othe target system are open and actively
                           accepting connections. This infomation can be valuable for understanding
                           the services or applications running on the system.
                    
              ~ Service Idemtification:
                                       By examining the response received fron an open port, a port
                                       scanner can often determine the type of service or 
                                       application running on that port.
        
              ~ Operating System Detection:
                                           It can often infer the operating system of the target
                                           system based on the response received from open ports.
                                           It is achieved by analyzing various characteristics,
                                           such as behaviour of the TCP/IP stack or the presence of
                                           specific services or protocols.
                                   
              ~ FIrewall Filtering: 
                                   It can help identify if a firewall is in place and which ports
                                   are being filtered or blocked by the firewall. 
                                   By comparing the results of port scans from different locations,
                                   one can determine if certain ports are accessible only from
                                   specific networks or if they are completely blocked.
                                              
      There are techniques to use to avoid detection from the target host. The techniques 
      that the port scanner can employ to minimise their footprint or evade detection by 
      intrusion systems (IDS) or firewalls. These techniques include:
                  
              ~ Stealth Scanning:
                                 It uses a technique such as SYN scanning, which does not
                                 complete the TCP handshake, making it harder for IDS 
                                 systems to detect the scan. By sending the initial SYN packet and
                                 not completing the handshake, the scanner does not leave a full
                                 connection trace.
                                            
              ~ Timing and Rate Control:
                                        It can control the timing and rate of scan requests to 
                                        avoid triggering rate-based intrusion detection machanisms.
                                        By spacing out scan requests or randomizing the scan timing,
                                        the scanner can evade detection.
                                                   
              ~ IP Spoofing: 
                            This involves forging the IP address of the scan packets to make it 
                            appear as if the scan is originating from a different IP address.
                            This can help obfuscate the actual source of the scan.
                                       
Advanced security systems and network administrators with proper monitoring tools can identify and
           block port scanning activities.
           

