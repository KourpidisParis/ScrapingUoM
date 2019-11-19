import requests
from bs4 import BeautifulSoup


def scraping(url):
    names = []
    tel = []
    emails = []
    source = requests.get(url).text

    soup = BeautifulSoup(source, "lxml")

    temp = soup.findAll("div", class_="range offset-top-15")[0]
    title = temp.find("th").text

    temp = soup.findAll("div", class_="range offset-top-15")[1]
    title2 = temp.find("th").text

    # I'm doing the following if_else because some departments have a dean and a president
    # and some only a dean

    if title == "Πρόεδρος Τμήματος" and title2 == "Κοσμήτορας":
        # president or dean of the department
        name_of_president = get_president(soup.findAll("div", class_="range offset-top-15")[0])
        print("-----------------------------------------------------------------")

        # dean
        name_of_dean = get_dean(soup.findAll("div", class_="range offset-top-15")[1])
        print("-----------------------------------------------------------------")

        # professors
        professor_info(soup.findAll("div", class_="range offset-top-15")[2], names, tel, emails)
        print("-----------------------------------------------------------------")

        # deputy professors
        professor_info(soup.findAll("div", class_="range offset-top-15")[3], names, tel, emails)
        print("-----------------------------------------------------------------")

        # assistant professors
        professor_info(soup.findAll("div", class_="range offset-top-15")[4], names, tel, emails)
    else:
        # dean
        name_of_dean = get_dean(soup.findAll("div", class_="range offset-top-15")[0])
        print("-----------------------------------------------------------------")

        # professors
        professor_info(soup.findAll("div", class_="range offset-top-15")[1], names, tel, emails)
        print("-----------------------------------------------------------------")

        # deputy professors
        professor_info(soup.findAll("div", class_="range offset-top-15")[2], names, tel, emails)
        print("-----------------------------------------------------------------")

        # assistant professors
        professor_info(soup.findAll("div", class_="range offset-top-15")[3], names, tel, emails)


def get_dean(temp):
    title = temp.find("th").text
    print(title)
    name = temp.find("span", class_="text-black").text
    print(name)
    return name


def get_president(temp):
    title = temp.find("th").text
    print(title)
    name = temp.find("span", class_="text-black").text
    print(name)
    return name


def professor_info(temp, temp_names, temp_tels, temp_emails):
    # print(temp.prettify())
    title = temp.find("th").text
    print(title)

    for name in temp.findAll("a"):
        temp_names.append(name.text)  # i take the name

    data = []
    for prof in temp.findAll("td"):  # At this point we can export name, telephones and mail, but I want them
        # separately to manage them better
        data.append(prof.text)
        # print(prof.text)

    i = 2
    while i < data.__len__():
        temp_tels.append(data[i])  # i take the telephone number
        i = i + 4

    i = 3
    while i < data.__len__():
        data[i] = fix_the_email(data[i])
        temp_emails.append(data[i])  # i take the email
        i = i + 4

    # printing infjormation
    i = 0
    while i < temp_names.__len__():
        print(temp_names[i] + "," + temp_tels[i] + "," + temp_emails[i])
        i = i + 1


def fix_the_email(email):
    # emails that scraped have no @

    temp = email.split(" ")
    temp[1] = "@"  # In this place is the problem
    fixed_email = "".join(temp)
    return fixed_email


ans = True
while ans:
    print("Chose 1-8 for educational staff: ")
    print("""
    1.Department of Applied Informatics
    2.Department of Economics
    3.Department of Business Planning & Management
    4.Department of Accounting and Finance
    5.Department of International & European Studies
    6.Department of Education & Social Policy
    7.Department of Music Science & Art
    8.Department of Balkan, Slavic & Eastern Studies
    9.Exit/Quit
    """)
    ans = input("What would you like to do?")
    if ans == "1":
        print("Department of Applied Informatics")
        scraping("https://www.uom.gr/dai/akadhmaiko-prosopiko")
    elif ans == "2":
        print("Department of Economics ")
        scraping("https://www.uom.gr/eco/akadhmaiko-prosopiko")
    elif ans == "3":
        print("Department of Business Planning & Management")
        scraping("https://www.uom.gr/ba/akadhmaiko-prosopiko")
    elif ans == "4":
        print("Department of Accounting and Finance")
        scraping("https://www.uom.gr/fin/akadhmaiko-prosopiko")
    elif ans == "5":
        print("Department of International & European Studies")
        scraping("https://www.uom.gr/ies/akadhmaiko-prosopiko")
    elif ans == "6":
        print("Department of Education & Social Policy")
        scraping("https://www.uom.gr/esp/akadhmaiko-prosopiko")
    elif ans == "7":
        print("Department of Music Science & Art")
        scraping("https://www.uom.gr/msa/akadhmaiko-prosopiko")
    elif ans == "8":
        print("Department of Balkan, Slavic & Eastern Studies")
        scraping("https://www.uom.gr/bso/akadhmaiko-prosopiko")

    elif ans == "9":
        print("\n Goodbye")
        break
    elif ans != "":
        print("\n Not Valid Choice Try again")
