from censys.search import CensysHosts


from dotenv import dotenv_values

config = dotenv_values(".env")

# Set up Censys API credentials from environment variables
API_ID = config.get("API_ID")
API_SECRET = config.get("API_SECRET")


h = CensysHosts(API_ID, API_SECRET)


# get all supershell
for page in h.search('services.http.response.html_title:"Supershell - 登录"', pages=-1, fields=["ip", "protocols"]):
    
    print(page)
    for p in page:
        
        # get the ip address
        ip = p.get('ip')
        ports = []
        for service in p.get('services'):
            ports.append(service.get('port'))


        if 8888 in ports:
            print("SuperShell found on: " + ip)
        print(ip)
        print(ports)

        # write the ips to a file
        with open('supershell.txt', 'a') as f:
            f.write("http://" + ip + ":8888\n")

# get all gophish
for page in h.search('services.http.response.html_title:"Gophish - Login"', pages=-1, fields=["ip", "protocols"]):
    
    print(page)
    for p in page:
        
        # get the ip address
        ip = p.get('ip')
        ports = []
        for service in p.get('services'):
            ports.append(service.get('port'))


        if 3333 in ports:
            print("Gophish found on: " + ip)
        print(ip)
        print(ports)

        # write the ips to a file
        with open('gophish.txt', 'a') as f:
            f.write("https://" + ip + ":3333\n")


# # View each result returned
# # For `hosts` this looks like a mapping of IPs to view results
# query = h.search("service.service_name: HTTP", per_page=5, pages=2)
# print(query.view_all())