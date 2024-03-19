import http_requests
import html_parser
import data_processing

def fetch_ticket_prices():
    html_dict = http_requests.get_html_from_skyscanner()
    ticket_prices_dict = html_parser.parse_html(html_dict)
    processed_data = data_processing.process_data(ticket_prices_dict)
    return processed_data

if __name__ == "__main__":
    processed_data = fetch_ticket_prices()
    data_processing.save_to_csv(processed_data, f"C:\\Users\\Admin\\Documents\\tickets_info.csv")