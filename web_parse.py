from bs4 import BeautifulSoup

def extract_main_paragraphs(html_string):
    soup = BeautifulSoup(html_string, 'html.parser')
    paragraphs = soup.find_all('p')
    
    main_paragraphs = []
    for paragraph in paragraphs:
        # Skip short UI phrases based on character count
        if len(paragraph.get_text(strip=True)) > 10:
            main_paragraphs.append(paragraph.get_text(strip=True))
    
    return "\n\n".join(main_paragraphs)