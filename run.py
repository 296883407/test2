import requests

def test():
    url = "https://api.mailgun.net/v3/sandbox70fe41fe48874cbea46db863daab12e2.mailgun.org/messages?from=test@test.com&to=fredzhou@deloitte.com.cn&subject=Mailgun Send Test&text=Test successful."
    payload={}
    headers = {
    'Authorization': 'Basic YXBpOjcxMjRkMDEwYzVhMzQ0ZDBhOTkyOGE3YjU5NjA3NTRkLTc3NzUxYmZjLTI3MTQ1MmY1'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages",
		auth=("Authorization", "Basic YXBpOjcxMjRkMDEwYzVhMzQ0ZDBhOTkyOGE3YjU5NjA3NTRkLTc3NzUxYmZjLTI3MTQ1MmY1"),
		data={"from": "test@test.com",
			"to": ["fredzhou@deloitte.com.cn"],
			"subject": "Mailgun Send Test",
			"text": "Test successful."})
