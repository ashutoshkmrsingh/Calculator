# Smart-Calculator
***

## API
https://smartcalculatorapi.herokuapp.com

### Sending request with POST
- JSON Request
`{`
    `"text": "who are you?"`
`}`

- JSON Response
`{`
    `"text": "I'm Corlex Cool"`
`}`

- **Javascript - fetch**

```
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
  "text": "who are you?"
});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("https://smartcalculatorapi.herokuapp.com/api", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

- **Python - requests**
```
import requests
import json

url = "https://smartcalculatorapi.herokuapp.com/api"

payload = json.dumps({
  "text": "who are you?"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

- **cURL**
```
curl --location --request POST 'https://smartcalculatorapi.herokuapp.com/api' \
--header 'Content-Type: application/json' \
--data-raw '{
    "text": "who are you?"
}'
```

- **Java - OkHttp**
```
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\r\n    \"text\": \"who are you?\"\r\n}");
Request request = new Request.Builder()
  .url("https://smartcalculatorapi.herokuapp.com/api")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .build();
Response response = client.newCall(request).execute();
```

## .exe
**./dist/main.exe**