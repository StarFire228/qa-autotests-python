emails = ["user@mail.ru", "test@gmail.com", "admin@yandex.ru", "boberyandex.ru", "shlepa@vovaru", ""]

print(emails)        # весь список

for email in emails:
    if "@" in email and "." in email:
        print(f"{email} - есть символ @ и точка")
    else:
        print(f"{email} - нет символа @ или точки")