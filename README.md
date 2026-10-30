STUDENT REGISTRATION SYSTEM - FINAL PROJECT 101

> PRINT, IF/ELSE TAS LOOPS LANG TO
> # YUNG MGA MAY HASHTAG NOTE YAN
MY INFORMATION
PANO NAG WO-WORK?
  - ONE BIG WHILE LOOP (MAS BASIC KESA LAGYAN NATIN NG DEFINE FUNCTION)
  - The variable "screen" says which screen to show: "main", "dashboard" or "edit".
  - YUNG MGA DATA NAKA SAVE SA: StudsF.csv, StudentsAcc.csv, AT Admin.csv
   (BALE PAG NI RUN YUNG CODE TSAKA MAG T-TYPE NA KAYO AT NA REGISTER DON PALANG MAGAGAWA 
   YUNG MGA FILES, OKEH?)
  - YUNG STARTTING PASSWORD NG MGA STUDENTS IS YUNG KANILA RING STUDENT NUMBER LIKE 26-050030
  - BALE MAS SIMPLE NA YUNG CSV DITO: read each file once at the start, and every time something
    changes, save the WHOLE list again (header row first, then every row).

#CSV = READ AND WRITE CSV FILES (YUNG NAGLALAGAYAN NG MGA DATA)
#OS = PARANG ANO SYA NAKIKIPAG USAP SYA SA MISMONG SYSTEM: CHECK NIYA IF ANDON BA YUNG 
MGA NAGAWANG FILES AND MAG C-CLEAR NG SCREEN IF TRUE YUNG COMMAND.
#RE = REGULAR EXPRESSION. CHECK NIYA IF YUNG NAI INPUT NA STUDENT NUMBER, EMAIL,
  KEN PHONE KET USTO J PATTERN NA A NAKA DECLARE.
#input = KASLANG "INPUT(), NGEM ILEMMENG NA EJAY I TTYPE JE USER NGA PASSWORD. KASLANG PRIVACY GANON.

=======READ ME===========
Check niyo yung isa pang file, download niyo nalang sya baahin niyo
 kung ano andyan para maintindihan niyong Mabuti.

Disclaimer: AI po yan, bale sinned ko yung whole na code ko sakanya then 
pina explain ko yung mga functions. Need niyo nalang silang ifamiliarize and
magpatulong kayo kay ai kung medyo may di kayo naiintindihan haaa. 
Tas yung buong system eh aralin niyo. Yon lang, salamat.

////jiyan2k26
