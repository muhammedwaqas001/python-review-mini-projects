email = "Muhammad.Waqas@Gmail.com"
lowercase_email = email.lower()
gmail_account = lowercase_email.endswith("@gmail.com")
position_check = lowercase_email.find("@")
username = lowercase_email[:position_check]
domain = lowercase_email[position_check + 1:]
dot_count = lowercase_email.count(".")
print(f"Email: {lowercase_email}")
print(f"Gmail Account: {gmail_account}")
print(f"@ Position: {position_check}")
print(f"Username: {username}")
print(f"Domain: {domain}")
print(f"Dot Count: {dot_count}")

