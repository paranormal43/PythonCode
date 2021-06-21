import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = "EMAIL_ADDRESS"
MY_PASSWORD = "MAIL_PASSWORD"
AMAZON_URL ="https://www.amazon.co.jp/dp/B081C2RP1S/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B081C2RP1S&pd_rd_w=klKmJ&pf_rd_p=d33ff8eb-7fee-4a16-8ef7-469a9348381a&pd_rd_wg=ERMdX&pf_rd_r=HAS77JJPTRJ6B7Z4D72Z&pd_rd_r=035da090-61e8-4c24-a58a-cf5bf853a290&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExRVlDT1c1TDg1UUImZW5jcnlwdGVkSWQ9QTA3NDA2ODIxTFYzWTA2V1E2QkkwJmVuY3J5cHRlZEFkSWQ9QTVCWUtFUzBLQVIwNSZ3aWRnZXROYW1lPXNwX2RldGFpbCZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url=AMAZON_URL, headers=header)

# print(response.content)

soup = BeautifulSoup(response.content,"lxml")

# print(soup.prettify())

price = soup.find(id="priceblock_ourprice").get_text()
price_without_currency = price.split("￥")[1].replace(",", "")

price_as_float = float(price_without_currency)
print(price_as_float)

if price_as_float <= 5000:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg="Subject: Amazon Price Alert !!!!!\n\nThis Email sent by Python Code for the product of Amazon Price"
                                "is Below than your expect. Please Buy")

