import smtplib

my_email = "ahsan.shahid.cssfl@gmail.com"
password = "password"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="ahsanshahid.cssfl@yahoo.com",
                        msg="Subject:Hello Ahsan\n\nthis is a test email from python")
