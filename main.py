import http_requests
import html_parser
import data_processing

def fetch_ticket_prices():
    html_dict = http_requests.get_html_from_skyscanner()
    ticket_prices_dict = html_parser.parse_html(html_dict)
    processed_prices = data_processing.process_data(ticket_prices_dict)
    return processed_prices

if __name__ == "__main__":
    prices = fetch_ticket_prices()
    #print(prices)  # Optional: Print prices to console for verification
    #data_processing.save_to_csv(prices, "ticket_prices.csv")