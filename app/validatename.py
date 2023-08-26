import openai

def validate_company_name_gpt(prompt, modality, api_key):
    user_prompt = f"""Please confirm that {prompt} is a valid company name by checking is listed on a stock exchange:
    the New York Stock Exchange NYSE,
    the NASDAQ,
    the London Stock Exchange LSE,
    the Tokyo Stock Exchange TSE,
    the Shanghai Stock Exchange SSE,
    the Hong Kong Stock Exchange HKSE,
    the Euronext,
    the Shenzhen Stock Exchange SZSE,
    the Toronto Stock Exchange TSX,
    the Bombay Stock Exchange BSE,
    the National Stock Exchange of India NSE,
    the SIX Swiss Exchange SIX,
    the Korea Exchange KRX,
    the Australian Securities Exchange ASX,
    the JSE Limited JSE,
    the Deutsche Börse XETRA,
    the BME Spanish Exchanges BME,
    the B3 B3,
    the Stock Exchange of Thailand SET,
    the Indonesia Stock Exchange IDX,
    the Bursa Malaysia BHD Bursa Malaysia,
    the Saudi Stock Exchange Tadawul,
    the Tel Aviv Stock Exchange TASE,
    the Singapore Exchange SGX,
    the Philippine Stock Exchange PSE,
    or that it exists in a recognized corporate database:
    the S&P Global Market Intelligence,
    the Bureau van Dijk,
    the Dun & Bradstreet,
    the Experian,
    the Equifax 
    the TransUnion
    the Moody's Analytics
    the Fitch Group
    the A.M. Best
    the DBRS Morningstar
    the RapidRatings
    the S&P Global Ratings
    the Fitch Ratings
    the Moody's Investors Service
    the Kroll Bond Rating Agency
    https://www.ciregistry.ky/
    https://www.systemday.com/
    https://www.caymanresident.com/
    https://web.caymanchamber.ky/
    https://www.campaign.cima.ky/
    Answer 'yes' or 'no'."""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": f"You are a {modality}."},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.3,  # Lower temperature to make validation more precise
    )

    final_response = response.choices[0]["message"]["content"].strip().lower()

    if 'yes' in final_response or 'valid' in final_response:
        return True
    else:
        return False
