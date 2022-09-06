email = input("enter your email")

if '@' in email and len(email) >= 11 and ('.com' in email or 'org' in email):
    print('good email')
else:
    print('not looks like email')


print('PROFESSIONAL WAY')

email = input("enter your email")

if '@' not in email:
    print('your email does not have @')
elif len(email) < 11:
    print('length of email not valid')
elif '.com' not in email and 'org' not in email:
    print('invalid domain')
else:
    print('your email look valid')

