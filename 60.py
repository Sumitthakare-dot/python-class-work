#List of email addresses(some duplicates)
email_addresses = [
    "user1@example.com","user2@example.com","user1@example.com",
    "user1@example.com","user4@example.com","user3@example.com",
]
#use a set to remove duplictes
unique_emails = set(email_addresses)

#convert the set back to sorted list if needed
unique_emails_list = sorted(unique_emails)

print(unique_emails_list)
#output the unique email addresses
print ("unique email addresses:")
for email in unique_emails_list:
    print(email)