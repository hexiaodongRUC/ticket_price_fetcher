# html_parser.py

from bs4 import BeautifulSoup

def parse_html(html_dict):
    ticket_prices_dict = {}
    # Parse the HTML using BeautifulSoup or any other HTML parsing library
    for idx, html in html_dict.items():
        soup = BeautifulSoup(html, 'html.parser')
        # 找到推荐的机票信息所在的容器
        recommendations = soup.find_all("div", class_="BpkText_bpk-text__2NH4L BpkText_bpk-text--body__19Pnr DetailsPanelContainer_priceDetails__3gpkw")

        # 提取前5行推荐的机票价格和航空公司
        for index, recommendation in enumerate(recommendations[:5], start=1):
            price = recommendation.find("span", class_="BpkText_bpk-text__2NH4L BpkText_bpk-text--lg__2gZYD")
            airline = recommendation.find("span", class_="BpkText_bpk-text__2NH4L BpkText_bpk-text--sm__33PGB DetailsPanelContainer_airline__1FgJH")
            
            if price and airline:
                print(f"Recommendation {index}: Price - {price.text.strip()}, Airline - {airline.text.strip()}")
            

    # Extract relevant ticket price information
    # Implement logic to extract ticket prices here

    return ticket_prices_dict