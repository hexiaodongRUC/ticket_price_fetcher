# html_parser.py

from bs4 import BeautifulSoup
import re

def parse_html(html_dict):
    ticket_prices_dict = {}
    # Parse the HTML using BeautifulSoup or any other HTML parsing library
    for idx, html in html_dict.items():
        soup = BeautifulSoup(html, 'html.parser')
        recommendations = soup.find_all("div", class_="BpkTicket_bpk-ticket__NzNiO")
        print(idx)
        # 找到推荐的机票信息所在的容器
        for recommendation in recommendations:
            try:
                aircompany = recommendation.find("span", class_="BpkText_bpk-text__MWZkY BpkText_bpk-text--xs__ZDJmY").get_text()
                price = recommendation.find("span", class_="BpkText_bpk-text__MWZkY BpkText_bpk-text--lg__NjNhN").get_text()
                fly_way = recommendation.find("span", class_=re.compile("^BpkText_bpk-text__MWZkY BpkText_bpk-text--xs__ZDJmY LegInfo_stopsLabel")).get_text()
                time_duration=recommendation.find("span", class_="BpkText_bpk-text__MWZkY BpkText_bpk-text--xs__ZDJmY Duration_duration__NmUyM").get_text()
                dep_time = recommendation.find_all("span", class_="BpkText_bpk-text__MWZkY BpkText_bpk-text--subheading__NzkwO")[0].get_text()
                des_time = recommendation.find_all("span", class_="BpkText_bpk-text__MWZkY BpkText_bpk-text--subheading__NzkwO")[1].get_text()
                print(f"{aircompany}, {price}, {fly_way}, {time_duration}, {dep_time}, {des_time}")
            except:
                print(Exception)
            

    # Extract relevant ticket price information
    # Implement logic to extract ticket prices here

    return ticket_prices_dict