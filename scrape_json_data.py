import requests
import json 
import pandas as pd

def parsing_data(items):
    data = []  # Initialize data outside the loop
    for item in items:
        id_value = None
        ip = None
        for key, value in item.items():
            if key == '_id' and value is not None:
                id_value = str(item['_id'])
            if key == 'ip' and value is not None:
                ip = str(item['ip'])
            if key == 'port' and value is not None:
                port = str(item['port'])
            if key == 'city' and value is not None:
                city = str(item['city'])
            if key == 'country' and value is not None:
                country = str(item['country'])
            if key == "responseTime"  and value is not None:
                responseTime = str(item['responseTime'])
                
        if id_value is not None:
            proxy_link = "https://"+ ip + ":" +  port
            data.append({'Id': id_value, 'Ip': ip, 'Port': port, 'City': city, 'Country' : country, 'Response Time': responseTime, 'Proxy link': proxy_link})
            
    return data     

def main():
    
    #  URL_START = "https://geonode.com/free-proxy-list"
    
    all_data = []  # Initialize all_data outside the loop
    for page in range(1, 4):  
        link = f"https://proxylist.geonode.com/api/proxy-list?limit=500&page={page}&sort_by=lastChecked&sort_type=desc"
        try:
            response = requests.get(link)
            response.raise_for_status()  # Raise an exception for bad status codes
            txt = response.json()
            items = txt["data"]
            all_data.extend(parsing_data(items))
        except requests.RequestException as e:
            print(f"Failed to fetch data from page {page}. Error: {e}")
        
    if all_data:
        df = pd.DataFrame(all_data)  # Directly pass the list of dictionaries
        df.to_excel('data.xlsx', index=False)
        print("Data saved successfully to data.xlsx")
    else:
        print("No data saved")

if __name__ == "__main__":
    main()
