# Mail-Sender

This program is a Python script that sends repetitive email sequences using the smtplib library. It prompts the user to input the sender's email address, password, recipient's email address, email content, and subject. Additionally, it allows for attaching a file. The script then logs into the sender's email account, attaches the specified file (if any), and sends the email.

The program utilizes the schedule library to send emails at regular intervals. It schedules the maile() function to run every two seconds. The program also displays a message indicating successful login and the initiation of the email sending process.
