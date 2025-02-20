import http.client

conn = http.client.HTTPSConnection("gpt-4o.p.rapidapi.com")

payload = "{\"model\":\"gpt-4o\",\"messages\":[{\"role\":\"user\",\"content\":\"There are ten birds in a tree. A hunter shoots one. How many are left in the tree?\"}]}"

headers = {
    'x-rapidapi-key': "42b0b84d5emshe5466aeb8769e21p1aef96jsnfdb83a5a4128",
    'x-rapidapi-host': "gpt-4o.p.rapidapi.com",
    'Content-Type': "application/json"
}

conn.request("POST", "/chat/completions", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))