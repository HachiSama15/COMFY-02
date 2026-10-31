import csv
import os
import re
from datetime import date, datetime

#NA S-SAVE YUNG FILE SA FOLDER KUNG ASANG FOLDER NAKA-LAGAY YUNG CODE NATIN.
StudentsFILE = "StudsF.csv"
AccountsFILE = "StudentsAcc.csv"
AdminFILE = "Admin.csv"

#FIELDS

#YUNG TATLONG LIST NA'TO AY YUNG MGA COLUMN TITLES [FIRST ROW] FOR CSV FILE AT SA LOOP
STUDENTS = ["StudentsNumber", "LastName", "FirstName", "MiddleInitial", "FullName", "date_of_birth", "sex", "college", "department", "email", "phone",
            "year_level", "section"]
ACCOUNTS = ["StudentsNumber", "password"]
ADMIN = ["username", "password"]

#COLLEGE
#DICTIONARY ETOY NUKWA: SA LEFT SIDE IS YUNG COLLEGE NAME AT SA RIGHT SIDE NAMAN IS DEPARTMENT
#EXAMPLE: kolehiyo["Dentistry"] gives ["Doctor of Dental Medicine"].
kolehiyo = {
    "Engineering": ["Computer Engineering", "Electrical Engineering",
                    "Electronics Engineering", "Civil Engineering",
                    "Mechanical Engineering", "Agricultural and Biosystem Engineering",
                    "Ceramic Engineering", "Chemical Engineering"],
    "Computing and Information Sciences": ["Computer Science", "Information Technology"],
    "Arts & Sciences": ["Biology", "Mathematics", "Psychology", "Communication", "English Language",
                        "Sociology", "Meteorology"],
    "Business, Economics and Accountancy": ["Accountancy", "Business Administration", "Cooperative Management",
                                            "Economics", "Entrepreneurship", "Hospitality Management", "Tourism Management"],
    "Agriculture, Food and Sustainable Development": ["Agribusiness", "Agriculture", "Development Communication",
                                                      "Environmental Science", "Food Technology", "Forestry"],
    "Aquatic Sciences and Applied Technology": ["Fisheries", "Marine Biology"],
    "Dentistry": ["Doctor of Dental Medicine"],
    "Health and Sciences": ["Nursing", "Pharmacy", "Physical Therapy", "Radiologic Technology"],
    "Industrial Technology": ["Automotive Technology", "Industrial Technology"],
    "Teacher Education": ["Culture and Arts Education", "Early Childhood Development", "Elementary Education",
                          "Physical Education", "Secondary Education", "Special Need Education",
                          "Technical Vocational Teacher Education", "Technology and Livelyhood"],
    "Veterinary Medicine": ["Doctor of Veterinary Medicine"]
}

yearlevels = ["First Year", "Second Year", "Third Year", "Fourth Year", "Fifth Year", "Other"]

#STUDENT NUMBER
#BALE DITO DINEDECLARE KO NA YUNG MGA KINAKAILANGAN KASE MAGAGAMIT NATIN TO SA MGA LINES TO COME
#PATTERN SYA WITH re.match(). ^ = start, $ = end, [0-9] = range {2} = exactly 2 digits,- = yung hypen, [0-9] = range {6} = exactly 6 digits.
#SO YUNG STUDENT NUMBER AY DAPAT EXACT 8 DIGITS WITH HYPEN (example: 23-123456).
STUDENTNOPATTERN = r"^[0-9]{2}-[0-9]{6}$"

#EMAIL PATTERN NAMAN: letters/numbers/symbols, then @, TAPOS domain with at least one dot (LIKE gmail.com).
EMAILPATTERN = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)+$"

#PHONE PATTERN NAMEAN: 09 + 9 digits, or +639 + 9 digits. YUNG | IS "OR" (YUNG \+ NAMAN IS PARA MAGING ACTUAL NA + SIGN)
PHONEPATTERN = r"^(09[0-9]{9}|\+639[0-9]{9})$"

#DEFAULT ADMIN (username gianpogi123, password pogian). 
#BALE ETO GAGAMITIN NATIN SA PRESENTATION KASE DEFAULT NA EH. PERO MAY ANO NAMAN NA PWEDE PANG GUMAWA NG IBA.
ACCNGADMIN = {"username": "gianpogi123", "password": "pogian"}

PASSWORDLENGHT = 8
LOGINATTEMPTS = 5

#BALE ITO NAKITA KO LANG SA TIKTOK, WHEREIN YUNG SCREEN DIBA KAPAG NAG COCOMAND TAYO SA CMD IS ANDAMING GANAP EVERYTIME NA MAY CHOICE. 
#ETO NAMAN GINAGAWA NITO IMBES NA IMANO MANO NATIN NA ITTYPE YUNG CLS, ETO NA GAGAWA. DITO RIN NAGAGAMIT YUNG INIMPORT NATIN NA OS
CLEAR = "cls"
WIDTH = 50
LINE = "=" * WIDTH #MAS MINADALI NA PAG PRINT NG "=============" MINUMULTIPLY LANG SA WIDTH
SPACE = " " * WIDTH

#============CVS FILE==========================
#LABELS FOR STUDENTS RECORDS
#LIST OF PAIRS TO: (SA LEFT SIDE IS YUNG I PR-PRINT NA LABEL, YUNG SA RIGHT NAMAN IS YUNG KEY DON SA STUDENT'S DICTIONARY)
#BALE MAGAGAMIT TO LATER ON SA LOOP PARA I PRINT YUG STUDENT'S INFO
RECORDS = [("Student Number", "StudentsNumber"), ("Name", "FullName"), ("Date of Birth", "date_of_birth"), ("Sex(Male/Female)", "sex"), ("College Of", "college"),
           ("Department of", "department"), ("Year Level", "year_level"), ("Section", "section"), ("Email Address", "email"),
           ("Phone Number", "phone")]

#COLUMN TITLES AND YUNG WIDTH SA ADMINS' TABLES OF STUDENTS
TableTitles = ["No.", "Student No.", "Full Name", "College of", "Department of", "Year", "Section", "Email", "Phone"]
TableWidths = [4, 12, 18, 15, 16, 6, 8, 16, 14]

# ======== StudsF.csv ========
#IF WALA PANG FILE, MAG CCREATE SYA AND GAGAWA SYA NG COLUMN TITLES
#"with open(...) as file" INO-OPEN  NYA YUNG FILE SYEMPRE AND I CCLOSE NYA RIN AUTOMATICALLY. "w" = write (MAG SSTART SYA NG FILE FROM NOTHING).
if not os.path.exists(StudentsFILE):
    with open(StudentsFILE, "w", newline="", encoding="utf-8") as file:
        csv.writer(file).writerow(STUDENTS)

students = [] #BALE KADA STUDENTS KET AG STAY DITUY LIST HABANG NGA AG RRUN ETOY PROGRAM
with open(StudentsFILE, newline="", encoding="utf-8-sig") as file:
    #ETONG DictReader NAMAN IS MAGBIBIGAY SA EVERY ROW AS A DICTIONARY, LIKE {"StudentsNumber": "23-123456", "LastName": "CRUZ"}.
    for row in csv.DictReader(file):
        #IF MAY DAMAGE LANG NA ROW KUNG MADAMI OR KUNTI LANG. I KKEEP NA LANG AGIDYAY ROWS NGA RIGHT NUMBER TI COLUMNS.
        if len(row) == len(STUDENTS) and None not in row.values():
            students.append(row)

# ======== StudentsAcc.csv ========
#SAME CODE DIFFERENT LANG YUNG MGA NILAGAY NA VARS LIKE SA UNA US StudentsFILE DITO NAMAN IS YUNG AccountsFILE SAME RIN SA BABA SA
if not os.path.exists(AccountsFILE):
    with open(AccountsFILE, "w", newline="", encoding="utf-8") as file:
            csv.writer(file).writerow(ACCOUNTS)

accounts = []
with open(AccountsFILE, newline="", encoding="utf-8-sig") as file:
    for row in csv.DictReader(file):
        if len(row) == len(ACCOUNTS) and None not in row.values():
                accounts.append(row)

# ======== Admin.csv ========
if not os.path.exists(AdminFILE):
    with open(AdminFILE, "w", newline="", encoding="utf-8") as file:
        csv.writer(file).writerow(ADMIN)

admins = []
with open(AdminFILE, newline="", encoding="utf-8-sig") as file:
    for row in csv.DictReader(file):
        if len(row) == len(ADMIN) and None not in row.values():
            admins.append(row)

#ETO NAMAN DINEDECLARE NIYA NA KUNG WALA PANG ADMINISTRATOR EH MAGAGAMIT YUNG DEFAULT NA ADMIN WHICH IS YUNG ACCNGADMIN SA TAAS
if len(admins) == 0:
    admins.append(ACCNGADMIN)
    #PARA MA SAVE: WRITE COLUMN TITLE FIRST (writeheader), THEN YUNG EVERY ROW SA LIST (writerows).
    with open(AdminFILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=ADMIN)
        writer.writeheader()
        writer.writerows(admins)

#MAIN PROGRAM (IF ELSE TSAKA LOOP LANG TO PARA BASIC LANG I EXPLAIN)
#BALE YUNG WHOLE PROGRA KET NASA LOOB NG ISANG MALAKING LOOP. YUNG MGA VARIABLE NA "MAIN", "DASHBOARD", OR "EDIT" DECIDES KUNG ANONG SCREEN YUNG I SSHOW.
#TO GO TO ANOTHER SCREEN/MENU OR JUST CHANGE YUNG SCREEN.
screen = "main"        #KUNG ANONG SCREEN ISSHOW
role = ""              #EITHER STUDENTS OR ADMIN

#None MEANS "WALA". KUNG MERON MANG NAKA LOG IN, ETONG VARIABLE NA'TO KET NAKA-HOLD OR STAY JE ACCOUNT NA NUKWA
loggedIn = None       #YUNG ACCOUNT NA NAKA LOG IN

# =========MAIN SYSTEM===========

while True:
    os.system(CLEAR) # TI USAR NA ETUY KET I CLEAR NA EJAY SCREEN NUKWA (SEE CLEAR = "cls" SA TAAS)
    #SCREEN 1: MAIN MENU
    #BALE ETO YUNG SINABI KO SA GC NA SHORTCUT HAHAHAHHAH
    if screen == "main":
        print(SPACE + "\n" + "WELCOME!".center(WIDTH) + SPACE)
        print(LINE + "\n" + "STUDENT REGISTRATION SYSTEM".center(WIDTH) + "\n" + LINE)
        print("\n[1] Register as a Student") #\N MEANS NEW LINE
        print("[2] Student Login")
        print("[3] Administrator Login")
        print("[4] Exit")
        choice = input("\nEnter your choice: ").strip()

        # ============= [1] REGISTER ============
        if choice == "1":
            os.system(CLEAR)
            print(LINE + "\n" + "REGISTER".center(WIDTH) + "\n" + LINE)
            student = {}
            #LIST COMPREHENSION TAWAG NA ETA ADDA DITA BABA = SHORTCUT PARA MAKA ARAMID ITI LOOP. I-COLLECT NA JE EVERY StudentsNumber in students,
            #TAS MAG A-ADD SA MGA ACCOUNTS. SAME LANG SA: for s in students: used_numbers.append(s["StudentsNumber"])
            used_numbers = [s["StudentsNumber"] for s in students] + \
                           [a["StudentsNumber"] for a in accounts] #DI BA MAS SHORT

            #STUDENTS NUMBER (DAPAT DI PA SYA NAKA REGISTER)
            while True:
                StudentsNumber = input("Student Number (School ID): ").strip().upper()
                #re.match(pattern, TEXT) BALE TRUE 'TO IF I-FFOLLOW YUNG PATTERN. SYEMPRE YUNG "not" BABALIKTARIN NIYA, SO MAGIGING TRUE IF YUNG FORMAT IS WRONG.
                if not re.match(STUDENTNOPATTERN, StudentsNumber):
                    print("Student Number must be 8 digits (23-123456).")
                elif StudentsNumber in used_numbers:
                    print("Student Number is already Registered.")
                else:
                    break #BREAK MEANS AGSARDENG HAHAHAHA OKAY??
            student["StudentsNumber"] = StudentsNumber

            #LAST NAME TAS FIRST NAMELast Name and First Name
            #BALE MAMINDWA NGA AG RUN ETOY LOOP. 1ST LOOP: field = "LastName", label = "Last Name". 2ND LOOP: "FirstName", "First Name".
            #SO IISANG LOOP EH TINATANONG YUNG DALAWANG QUESTION WHICH IS LASTN AND FIRST N.
            for field, label in [("LastName", "Last Name"), ("FirstName", "First Name")]:
                while True:
                    TEXT = input(label + ": ").strip()
                    if TEXT == "":
                        print(" This field is required.")
                    else:
                        #TEXT.split() cuts the TEXT into words. " ".join(...) joins them back with ONE space. .upper() = capital letters.
                        student[field] = " ".join(TEXT.split()).upper()
                        break

            #MIDDLE INITIAL
            while True:
                TEXT = input("Middle Initial (If none leave Blank): ").strip()
                #.isalpha() TRUE KUNG LAHAT AY LETTER. len(TEXT) == 1 MEANING NITO ISANG CHARACTER LANG DAPAT.
                if TEXT == "" or (len(TEXT) == 1 and TEXT.isalpha()): #ETA .ISALPHA GUYS KET I DDECLARE NA LANG NGA DAPAT LETTERS LANG SYA AT HINDI NUMBERS, NO SPACES, OR SYSMBOS ISU AG ERROR NUKWA
                    student["MiddleInitial"] = TEXT.upper()
                    break
                print("Only ONE letter.")

            #DATE OF BIRTH
            while True:
                TEXT = input("Date of Birth (YYYY-MM-DD, example 2008-05-31): ").strip() #NU STRIP() MET KET IKKATEN NA ITI SPACES
                try:
                    dob = datetime.strptime(TEXT, "%Y-%m-%d").date()
                except ValueError:
                    print("Invalid Date.")
                    continue 
                if dob > date.today() or dob.year < 1950:
                    print("Please Enter a Valid Date")
                else:
                    #isoformat() WRITES THE DAY ASSSS YYYY-MM-DD.
                    student["date_of_birth"] = dob.isoformat()
                    break
            #SEX, NEVER PA
            while True:
                    TEXT = input("Sex(Male/Female): ").upper().strip()
                    if TEXT in ("MALE", "FEMALE"):
                        student["sex"] = TEXT.upper()
                        break
                    print("Enter only (Male/Female)")

            #COLLEGE
            #kolehiyo.keys() = #BALE ETA .KEYS() TI FUNCTION NA ETA KET ALAEN NA EJAY IMMUNA NGA NAKA "" OR BEFORE :  KASTA IDJAY TAAS (KOLEHIYO). 
            #list(...) NEW FUNCTION NA DI NIYO PA NAKIKITA, GINAGAWA NITO IS GINAGAWA NIYANG LIST PARA EASY NUMBERING NALANG..
            colleges = list(kolehiyo.keys())
            print("\nSelect your College: ")
            #range(len(colleges)) BALE AG BILANG 0, 1, 2, ... INGGA NA J NUMBER OF COLLEGES. i is the position; i + 1 is the number we show (IMBES NA 0, 1, 2, 3, .... EH MAGIGING 1,2,3,4,5, ......).
            for i in range(len(colleges)):
                print("  [" + str(i + 1) + "] " + colleges[i]) #NU DIYO MAAWATAN ETOY: BALE ETA STR(I+1) + COLLEGE - TI OUTPUT NA ETA KET "[1]ENGINEERING" AND SO ON.
                #SO IMBES NGA MANO MANO NGA AGIKABIL ITI PRINT KINEME, AL ALISTO ETAN KASE IN LOOP KON.
            while True:
                TEXT = input("Enter your choice: ").strip()
                #1 <= int(TEXT) <= len(colleges) means "from 1 up to the last number".
                if TEXT.isdecimal() and 1 <= int(TEXT) <= len(colleges): #T.ISDECIMAL NAMAN SYEMPRE NU DECIMAL AG ERROR I CCHECK NA NU WHOLE NUMBER BA TA INTYPE MO OR ADDA DECIMAL NA
                    #YUNG LIST NAG START SA 0, KAYA NAG SUBRTACT TAYO NG 1: colleges[int(TEXT) - 1].
                    student["college"] = colleges[int(TEXT) - 1]
                    break
                print(" Enter a number from 1 to " + str(len(colleges)) + ".")

            #DEPARTMENT 
            #BALE NAULIT LANG SYA PERO SA DEPARTMENT NA
            #ONLY THE DEPARTMENTS SA COLLEGE NA NAPILI NG STUDENT
            departments = kolehiyo[student["college"]]
            print("\nSelect your Department:")
            for i in range(len(departments)):
                print("  [" + str(i + 1) + "] " + departments[i])
            while True:
                TEXT = input("Enter your choice: ").strip()
                if TEXT.isdecimal() and 1 <= int(TEXT) <= len(departments):
                    student["department"] = departments[int(TEXT) - 1]
                    break
                print(" Enter a number from 1 to " + str(len(departments)) + ".")
            print()

            #EMAIL
            while True:
                TEXT = input("Email Address: ").strip().lower() #ETA LOWER() NU ADDA ITI NAKA CAPS A NAITYPE PAGBALBALINEN NA NGA LOWERCASE MATIC
                if not re.match(EMAILPATTERN, TEXT): #ETA .REMATCH MET KITKITAEN NA EJAY EMAILPATTERN NGA ADDA JE TAAS (EMAILPATTERN) IF MATCH METLANG
                    print(" Invalid email (example: juan@example.com).")
                #LIST COMPREHENSION MANEN GOIZ
                #CHECK NALANG ULIT SA CVS IF MAY SIMILAR EMEAIL SA LIST
                elif TEXT in [s["email"].lower() for s in students if s["StudentsNumber"] != StudentsNumber]: #BALE ETY MARIGATAN NAK NGA MANGI ANO KASE INNALAK LANG J GITHUB ETOY NGA IDEA, NGEM SAME IDEA METLA KAETA IMMUN UNA
                    print(" Email address is Already Registered.")
                else:
                    student["email"] = TEXT
                    break

            #PHONE NUMBER
            while True:
                TEXT = input("Phone Number (09XXXXXXXXX or +639XXXXXXXXX): ").strip()
                TEXT = TEXT.replace(" ", "").replace("-", "")
                if re.match(PHONEPATTERN, TEXT):
                    student["phone"] = TEXT
                    break
                print(" Invalid phone number.")

            #YEAR LEVEL
            print("\nSelect your Year Level: ")
            for i in range(len(yearlevels)):
                print("  [" + str(i + 1) + "] " + yearlevels[i]) #MATIK AGARAMID ITI NUM LIST LIKE [1][2], NAKA LOOP EH, SA,E IDEA SA COLLEGE
            while True:
                TEXT = input("Enter your choice: ").strip()
                if TEXT.isdecimal() and 1 <= int(TEXT) <= len(yearlevels):
                    student["year_level"] = yearlevels[int(TEXT) - 1]
                    break
                print(" Enter a number from 1 to " + str(len(yearlevels)) + ".")
            print()

            #SECTION
            while True:
                TEXT = input("Section (Example: 1C or BSCPE-1C): ").strip().upper()
                if TEXT == "" or len(TEXT) > 15:
                    print(" Section is required.")
                else:
                    student["section"] = TEXT
                    break

            # STUDENT NUMBER ITI PASSWORD (PWEDE SYA MA CHANGE LATER ON)
            account = {"StudentsNumber": StudentsNumber, "password": StudentsNumber}

            # DISPLAY NAME (MAKIKITA TO AFTER NIYA MAKA LOG IN)
            name = student["LastName"] + ", " + student["FirstName"]
            if student["MiddleInitial"] != "":
                name += " " + student["MiddleInitial"] + "."
            student["FullName"] = name.upper()

            # ISSAVE NIYA DON SA CSV FILE NANAGAWA
            # SIMPLE EXPLANATION: ADD NEW STUDS SA LIST, THEN MASSAVE SYA SYA SA CSV FILE ULIT
            accounts.append(account)
            students.append(student)
            #MAULIT LA JE CODE
            try:
                with open(AccountsFILE, "w", newline="", encoding="utf-8") as file:
                    writer = csv.DictWriter(file, fieldnames=ACCOUNTS)
                    writer.writeheader()
                    writer.writerows(accounts)
                with open(StudentsFILE, "w", newline="", encoding="utf-8") as file:
                    writer = csv.DictWriter(file, fieldnames=STUDENTS)
                    writer.writeheader()
                    writer.writerows(students)
                print("\nREGISTRATION SUCCESSFUL!!!!!")
                print("Student Number: " + StudentsNumber)
                print("Your password is your Student Number.")
                print("Please Log In again and change it using Change Password.")
            except OSError as error:
                accounts.remove(account)
                students.remove(student)
                # FIXED: before, nothing was printed when saving failed
                print("\nCould not save. Close the CSV files if they are open in another program, then try again.")
            input("\nPress Enter to Continue")

        # ============= [2] STUDENT LOGIN / [3] ADMIN LOGIN =============
        elif choice == "2" or choice == "3": #BALE PINAGSAMA KO NA SILANG DALAWA KASE SAME LANG NAMAN EH ALANGABN UULIT ULITIN KO PANG HILINGIN SA BATHALA NA BUMALIK SYA?
            # SAME LOG IN STEPS KAY ADMIN AT STUDENTS
            if choice == "2":
                role = "student"
                title = "LOG IN AS A STUDENT"
                label = "Student Number"
                key = "StudentsNumber"
                #SOOOO WALANG COPY MAGAGWA: login_rows and accounts are the SAME list. WE ONLY CHOOSE WHAT LIST TO CHECK
                #(STUDENTS' ACC OR ADMINS')
                login_rows = accounts
                login_file = AccountsFILE
                login_fields = ACCOUNTS
            else:
                role = "admin"
                title = "LOG IN AS ADMINISTRATOR"
                label = "Username"
                key = "username"
                login_rows = admins
                login_file = AdminFILE
                login_fields = ADMIN

            os.system(CLEAR)
            print(LINE + "\n" + title.center(WIDTH) + "\n" + LINE)
            loggedIn = None
            attempts_left = LOGINATTEMPTS
            while attempts_left > 0:
                name = input(label + ": ").strip()
                password = input("Password: ")
                if name == "" or password == "":
                    print(" Both fields are required.\n")
                    continue

                #BALE HERE, YUNG SYSTEM TITIGNAN NIYA YUNG CVS FILE KUNG ANDON BA TALAGA YUNG ACC MO O WALA,
                #KUNG MERON MAKAKA LOG IN KA AT KUNG WALA EDI HINDI LALA
                #TITIGNAN NG SYSTEM IF MAY SAME Student Number / username. .upper() SA DALAWANG SIDE
                #EITHER UPPERCASE SYA OR LOWERCASE, PARANG AKO, IT DOESN'T MATTER IF AVOIDANT SYA O HINDI BASTA BUMALIK LANG SYA
                for account in login_rows:
                    if account[key].upper() == name.upper():
                        if account["password"] == password:
                            loggedIn = account
                        break
                #"is not None" EHH SYEMPRE MAY NAKA LOG IN
                if loggedIn is not None:
                    break
                attempts_left -= 1
                print(" Incorrect " + label.lower() + " or password. Attempts left: " + str(attempts_left) + "\n")

            if loggedIn is not None:
                screen = "dashboard"
            else:
                print("Too many failed attempts.")
                input("\nPress Enter to continue...")

        # ============== [4] EXIT ==============
        elif choice == "4":
            while True:
                answer = input("Are you sure you want to exit? (Y/N): ").strip().lower() #YUNG LOWER EH DINEDECLARE NIYA NA KAHIT CAPS OR LOWERED YUNG Y/N TATANGGAPIN PARIN
                if answer == "y" or answer == "n":
                    break
                print(" Please enter Y or N.")
            if answer == "y":
                break    #PROGRAM ENDS

        else:
            print(" Invalid choice. Enter 1 to 4.")
            input("\nPress Enter to continue...")

    # SCREEN 2: DASHBOARD
    elif screen == "dashboard":
        if role == "student":
            # HAHANAPIN YUNG MGA NAKA LOG IN NA STUDENTS SA CVS FILE
            student = None
            for s in students:
                if s["StudentsNumber"] == loggedIn["StudentsNumber"]:
                    student = s
            if student is None:
                print(" Your student record was not found.")
                input("\nPress Enter to continue...")
                screen = "main"
                continue

            print(LINE + "\n" + "STUDENT MENU".center(WIDTH) + "\n" + LINE)
            print("Welcome, " + student["FullName"] + "\n")
            print("[1] View My Information")
            print("[2] Edit My Personal Information")
            print("[3] Change Password")
            print("[4] Log Out")
            #DICTIONARY TO NGA AG CHCHANGE TI NUMBER IF NAGTYPE YUNG USER TI WORD (an "action").
            #SO AYUN, YUNG CODE SA IBABA KET SHARED BOTH BY THE STUDENT MENU KEN ADMIN TAPNO HAAN A MAULIT NGA ICODE MANEN
            actions = {"1": "view", "2": "edit", "3": "password", "4": "logout"}
        else:
            print(LINE + "\n" + "ADMINISTRATOR MENU".center(WIDTH) + "\n" + LINE)
            print("Logged in as: " + loggedIn["username"] + "\n")
            print("[1] View All Registered Students")
            print("[2] View Student Information")
            print("[3] Change Administrator Password")
            print("[4] Log Out")
            actions = {"1": "all", "2": "info", "3": "password", "4": "logout"}

        choice = input("\nEnter your choice: ").strip()
        #.get(choice, "") KITAEN NA IF YUNG TINYOE NA CHOICE IS ANDON SYA DICTIONARY.KUNG WALA SA DICTIONARY EDI WALA.
        action = actions.get(choice, "")

        # ====== View My Information (STUDENT) / View Student Information (ADMIN) ======
        if action == "view" or action == "info":
            os.system(CLEAR)
            if action == "view": #STUDENT DITO
                print(LINE + "\n" + "MY INFORMATION".center(WIDTH) + "\n" + LINE)
                record = student
            else: #ADMIN DITO
                print(LINE + "\n" + "VIEW STUDENT INFORMATION".center(WIDTH) + "\n" + LINE)
                number = input("Enter Student Number: ").strip().upper()
                record = None
                for s in students:
                    if s["StudentsNumber"] == number:
                        record = s
            if record is None:
                print(" No student found with that Student Number.")
            else:
                print("-" * WIDTH)
                # Each item in RECORDS is a pair. label gets the first one (TEXT to print), key gets the second
                # (which information to show). .ljust(15) adds spaces so the colons line up.
                for label, key in RECORDS:
                    print(label.ljust(15) + ": " + record[key])
                print("-" * WIDTH)
            input("\nPress Enter to continue...")

        # ========== Edit My Personal Information (STUDENTS) ==========
        elif action == "edit":
            original = student
            #dict(student) GAGAWA SYA NG COPY NG STUDENTS' INFO. MA CCHANGE YUNG COPY KEN I SAVE NALANG IF JE STUDENTS KET I SAVE NA.
            updated = dict(student)
            screen = "edit"

        # ========== View All Students (ADMIN) ==========
        elif action == "all":
            results = students
            os.system(CLEAR)
            print(LINE + "\n" + "ALL REGISTERED STUDENTS".center(WIDTH) + "\n" + LINE)
            if len(results) == 0:
                print("\nNo records found.")
            else:
                #YUNG TABLE IS A LIST OF ROWS (LIST INSIDE A LIST). YUNG FIRST ROW KET COLUMN TITLES.
                #str(number) GINAGAWANG STRING YUNG NUMBERS, BAKIT? KASE SA TABLE PRINTED AS TEXT SYA, SO KUNG HINDI MA CCONVERT YUNG INTIGER TO STRINGS MAG EERROR
                table = [TableTitles]
                number = 1
                for s in results:
                    table.append([str(number), s["StudentsNumber"], s["FullName"],
                                  s["college"], s["department"],
                                  s["year_level"].split(" ")[0], s["section"],
                                  s["email"], s["phone"]])
                    number += 1
                
                #AI NA TO, DITO SA PART NA TO KASE HINDI KO NA GETS HAHAHAHAHA PERO MAY EXPLANATION YUNG AI KAYA KINOPY KO NALANG. YAN YUNG MGA COMMENTS
                for index in range(len(table)):
                    line = ""
                    #zip walks through two lists at the same time: each cell together with the width of its column.
                    for TEXT, width in zip(table[index], TableWidths):
                        if len(TEXT) > width:
                            #TEXT[:n] takes the first n characters. This cuts long TEXT and adds ... so the columns stay straight.
                            TEXT = TEXT[:width - 3] + "..."
                        #ljust(width) adds spaces on the right so the TEXT takes exactly width characters.
                        #       += adds it to the end of line.
                        line += TEXT.ljust(width) + " "
                    print(line)
                    if index == 0:
                        print("-" * 118)
                print("\nTotal: " + str(len(results)) + " Student/s")
                print("Select 'View Student Information' for full details.")
            input("\nPress Enter to continue [ ] ")

        # ============ Change Password (STUDENT AND ADMINISTRATOR) ============
        elif action == "password":
            os.system(CLEAR)
            print(LINE + "\n" + "CHANGE YOUR PASSWORD".center(WIDTH) + "\n" + LINE)
            current = input("Current Password: ")
            if current != loggedIn["password"]:
                print(" Incorrect password.")
            else:
                while True:
                    NEWPASSWORD = input("New Password (at least " + str(PASSWORDLENGHT) + " characters): ")
                    if len(NEWPASSWORD) < PASSWORDLENGHT:
                        print(" Password is too short.")
                    elif NEWPASSWORD == current:
                        print(" The new password must be different from the old one.")
                    elif input("Confirm Password: ") != NEWPASSWORD:
                        print(" Passwords do not match.")
                    else:
                        break

                #loggedIn IS ANO SAME DICTIONARY NA NASA LOOB NG LIST (accounts or admins), KAYA PAG NAG CHANGE NG PASS EDI MA CCHANGE RIN KUNG ANO NASA LOOB NG LIST
                loggedIn["password"] = NEWPASSWORD
                # FIXED: added try/except. Before, the program crashed if the CSV file was open in Excel
                try:
                    with open(login_file, "w", newline="", encoding="utf-8") as file:
                        writer = csv.DictWriter(file, fieldnames=login_fields)
                        writer.writeheader()
                        writer.writerows(login_rows)
                    print("Your password has been changed.")
                except OSError:
                    loggedIn["password"] = current      # saving failed, so put the old password back
                    print("Could not save. Close the CSV files if they are open in another program.")
            input("\nPress Enter to continue...")

        # ========= Log Out =========
        elif action == "logout":
            loggedIn = None
            screen = "main"

        else:
            print(" Invalid choice.")
            input("\nPress Enter to continue...")

    # SCREEN 3: EDIT MY PERSONAL INFORMATION (STUDENT LANG)
    elif screen == "edit":
        StudentsNumber = original["StudentsNumber"]
        print(LINE + "\n" + "EDIT MY PERSONAL INFORMATION".center(WIDTH) + "\n" + LINE)
        print("Student Number : " + StudentsNumber + " [CAN'T CHANGE]")
        print("[1] Last Name         : " + updated["LastName"])
        print("[2] First Name        : " + updated["FirstName"])
        print("[3] Middle Initial    : " + updated["MiddleInitial"])
        print("[4] Date of Birth     : " + updated["date_of_birth"])
        print("[5] Sex (Male/Female) : " + updated["sex"])
        print("[6] College/Department: " + updated["college"] + " / " + updated["department"])
        print("[7] Email Address     : " + updated["email"])
        print("[8] Phone Number      : " + updated["phone"])
        print("[9] Year Level        : " + updated["year_level"])
        print("[10] Section          : " + updated["section"])
        print("[11] Save changes")
        print("[0] Go back")
        choice = input("\nWhich do you want to change? ").strip()

        # [1] Last Name / [2] First Name
        # AI RIN TO
        if choice == "1" or choice == "2":
            #One-line if/else: if the choice is 1 the field is LastName, otherwise FirstName.
            field = "LastName" if choice == "1" else "FirstName"
            label = "Last Name" if choice == "1" else "First Name"    # FIXED: the old code showed "New Lastname"
            while True:
                TEXT = input("New " + label + ": ").strip()
                if TEXT == "":
                    print(" This field is required.")
                #all(...) is True if EVERY character c is a letter, or a space, dot, apostrophe or hyphen.
                #       It is the same as writing a loop that checks each letter.
                elif not TEXT[0].isalpha() or not all(c.isalpha() or c in " .'-" for c in TEXT):
                    print(" Use letters only.")
                else:
                    updated[field] = " ".join(TEXT.split()).upper()
                    break
        #AI UNTIL HERE

        # [3] Middle Initial
        elif choice == "3":
            while True:
                TEXT = input("Middle Initial: ").strip().replace(".", "")
                if TEXT == "" or (len(TEXT) == 1 and TEXT.isalpha()):
                    updated["MiddleInitial"] = TEXT.upper()
                    break
                print(" Enter only ONE letter.")

        # [4] Date of Birth
        elif choice == "4":
            while True:
                TEXT = input("Date of Birth (YYYY-MM-DD, example 2008-05-31): ").strip()
                try:
                    dob = datetime.strptime(TEXT, "%Y-%m-%d").date()
                except ValueError:
                    print("Invalid Date.")
                    continue 
                if dob > date.today() or dob.year < 1950:
                    print("Please Enter a Valid Date")
                else:
                    updated["date_of_birth"] = dob.isoformat()
                    break

        # [5] Sex
        elif choice == "5":
            while True:
                TEXT = input("Sex (Male/Female): ").upper().strip()
                if TEXT in ("MALE", "FEMALE"):
                    updated["sex"] = TEXT.upper()
                    break
                print("Enter only (Male/Female)")

        # [6] College and Department
        # BALE NA DUPLICATE LANG JE CODE NU NAGUSAR NAK IT DEFINE FUNCTION BASBASSIT KUMA ETOY KEN HAAN A MAULIT ULIT SABALI
        elif choice == "6":
            colleges = list(kolehiyo.keys())
            print("\nSelect College:")
            for i in range(len(colleges)):
                print("  [" + str(i + 1) + "] " + colleges[i])
            while True:
                TEXT = input("Enter your choice: ").strip()
                if TEXT.isdecimal() and 1 <= int(TEXT) <= len(colleges):
                    updated["college"] = colleges[int(TEXT) - 1]
                    break
                print(" Enter a number from 1 to " + str(len(colleges)) + ".")

            departments = kolehiyo[updated["college"]]
            print("\nSelect Department:")
            for i in range(len(departments)):
                print("  [" + str(i + 1) + "] " + departments[i])
            while True:
                TEXT = input("Enter your choice: ").strip()
                if TEXT.isdecimal() and 1 <= int(TEXT) <= len(departments):
                    updated["department"] = departments[int(TEXT) - 1]
                    break
                print(" Enter a number from 1 to " + str(len(departments)) + ".")

        # [7] Email Address
        elif choice == "7":
            while True:
                TEXT = input("Email Address: ").strip().lower()
                if not re.match(EMAILPATTERN, TEXT):
                    print(" Invalid email (example: giantolentino@example.com).")
                elif TEXT in [s["email"].lower() for s in students if s["StudentsNumber"] != StudentsNumber]:
                    print(" That email address is already registered.")
                else:
                    updated["email"] = TEXT
                    break

        # [8] Phone Number
        elif choice == "8":
            while True:
                TEXT = input("Phone Number (09XXXXXXXXX or +639XXXXXXXXX): ").strip()
                TEXT = TEXT.replace(" ", "").replace("-", "")
                if re.match(PHONEPATTERN, TEXT):
                    updated["phone"] = TEXT
                    break
                print(" Invalid phone number.")

        # [9] Year Level
        elif choice == "9":
            print("\nSelect Year Level:")
            for i in range(len(yearlevels)):
                print("  [" + str(i + 1) + "] " + yearlevels[i])
            while True:
                TEXT = input("Enter your choice: ").strip()
                if TEXT.isdecimal() and 1 <= int(TEXT) <= len(yearlevels):
                    updated["year_level"] = yearlevels[int(TEXT) - 1]
                    break
                print(" Enter a number from 1 to " + str(len(yearlevels)) + ".")

        # [10] Section
        elif choice == "10":
            while True:
                TEXT = input("Section (example: 1A or CPE-1A): ").strip().upper()
                if TEXT == "" or len(TEXT) > 15:
                    print(" Section is required.")
                else:
                    updated["section"] = TEXT
                    break

        # [11] Save changes

        elif choice == "11":
            #WALANG NAGBAGO IF YUNG COPY IS YUNG ORIGINAL NAMAN
            if updated == original:
                print("No changes to save.")
                input("\nPress Enter to continue...")
                screen = "dashboard"
            else:
                while True:
                    answer = input("Save these changes? (Y/N): ").strip().lower()
                    if answer == "y" or answer == "n":
                        break
                    print(" Please enter Y or N.")

                if answer == "y":
                    updated["StudentsNumber"] = StudentsNumber
                    name = updated["LastName"] + ", " + updated["FirstName"]
                    if updated["MiddleInitial"] != "":
                        name += " " + updated["MiddleInitial"] + "."
                    updated["FullName"] = name.upper()

                    #BACKUP LANG TO IF EVER NA DI MA SAVE
                    backup = dict(original)
                    #Copy every value from "updated" into the real student (original).
                    for key in updated:
                        original[key] = updated[key]
                    try:
                        with open(StudentsFILE, "w", newline="", encoding="utf-8") as file:
                            writer = csv.DictWriter(file, fieldnames=STUDENTS)
                            writer.writeheader()
                            writer.writerows(students)
                        print("Your information has been updated.")
                        screen = "dashboard"
                    except OSError:
                        original.update(backup)
                        # FIXED: the old message said "Registration Failed" and was shown even when saving worked
                        print("Could not save. Close the CSV files if they are open in another program.")
                    input("\nPress Enter to continue...")
        # [0] BACK
        elif choice == "0":
            screen = "dashboard"

        else:
            print(" Invalid choice. Enter 0 to 11.")
            input("\nPress Enter to continue...")

print("PAALAMMMMM!")