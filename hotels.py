import http.client

conn = http.client.HTTPSConnection("hotels4.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "5e1f8d911dmshb5aa1f1b7f0b470p198d8djsn21c588b9da4a",
    'X-RapidAPI-Host': "hotels4.p.rapidapi.com"
    }

conn.request("GET", "/v2/get-meta-data", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))