import smtplib

def prompt(prompt):
    return input(prompt).strip()

fromaddr = prompt("From: ")
toaddrs  = prompt("To: ").split()
print("Enter message, end with ^D (Unix) or ^Z (Windows):")

# Add the From: and To: headers at the start!
msg = ("From: %s\r\nTo: %s\r\nSubject:test\r\n\r\n"
       % (fromaddr, ", ".join(toaddrs)))
while True:
    try:
        line = input()
    except EOFError:
        break
    if not line:
        break
    msg = msg + line

print("Message length is", len(msg),'\n',msg)

server = smtplib.SMTP_SSL('smtp.qq.com',465)
server.login('2325227059@qq.com','')
server.set_debuglevel(1)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()

