import smtplib

def generate_email():
    subject = input("Enter Subject: ")
    from_email = input("Enter email sending from: ")
    to_email = input("Enter email sending to: ")
    name = input("Enter a name: ")

    email = f"""Subject: {subject}
From: {from_email}
To: {to_email}

Hi, {name}

This is an email template.

Thanks,
Hey
"""
    return email, from_email, to_email


def send_email(from_email, password, to_email, content):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_email, password)

        server.sendmail(from_email, to_email, content)

        server.quit()
        print("Email sent successfully!")

    except Exception as e:
        print("Error:", e)



content, from_email, to_email = generate_email()

with open("email.txt", "w") as file:
    file.write(content)


password = input("Enter your email app password: ")

# Send email
send_email(from_email, password, to_email, content)