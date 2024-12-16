import streamlit as st
import requests
from bs4 import BeautifulSoup
from inference import run_inference

def scrape_amazon(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find_all("span", class_="a-list-item")

def scrape_amazon_image(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    span_list_items = soup.find_all("span", class_="a-list-item")
    
    for span in span_list_items:
        img = span.find('img')
        if img:
            return img.get('src')
    
    return None

def main():
    st.title("Product Score Analyzer")
    amazon_url = st.text_input("Enter the Amazon product URL:")

    if st.button("Analyze ESG Score"):
        if amazon_url:
            list_items = scrape_amazon(amazon_url)
            get_image = scrape_amazon_image(amazon_url)
            texts = [item.get_text(strip=True) for item in list_items]
            concatenated_text = " ".join(texts)
            prompt = f"Analyze this content: {concatenated_text}"

            # Make the API request
            response = run_inference(prompt)
            st.balloons()

            if isinstance(response, str):
                st.markdown(response)  # Display the sustainability analysis
            else:
                st.error(response)
        else:
            st.error("Please enter a valid Amazon product URL.")

if __name__ == "__main__":
    main()
