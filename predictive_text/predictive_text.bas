REM A Predictive Text Algorithm
REM Matthew Else, L1 - AS COMPUTING
REM 06/09/2013

REM Define the words to test with.
REM Should load from text file, ideally.
DIM words$(26)
DIM originalwords$(26)

words$(0) = "AARDVARK"
words$(1) = "BALLOON"
words$(2) = "CAT"
words$(3) = "DOG"
words$(4) = "ELEPHANT"
words$(5) = "FLOCCINAUCINIHILIPIFICATION"
words$(6) = "GOAT"
words$(7) = "HIPPO"
words$(8) = "INTERESTING"
words$(9) = "JUMPING"
words$(10) = "KITE"
words$(11) = "LOLIPOP"
words$(12) = "MATTHEW"
words$(13) = "NOBODY"
words$(14) = "OCTOPUS"
words$(15) = "PUMPKIN"
words$(16) = "QUAIL"
words$(17) = "RABBIT"
words$(18) = "STAPLER"
words$(19) = "TRAMP"
words$(20) = "UNDULATE"
words$(21) = "VANADIUM"
words$(22) = "WOLFRAM"
words$(23) = "XRAY"
words$(24) = "YOGHURT"
words$(25) = "ZIRCONIUM"

REM File loading can be left at the moment,
REM as there's an 8K limit in BBC BASIC TRIAL

REM filename$ = "dict.txt"
REM infile% = OPENIN(filename$)
REM IF infile% = 0 THEN
REM   ERROR 100, "Couldn't open the input file "+filename$
REM ENDIF

REM WHILE NOT EOF#file%
REM   a$ = GET$#file%
REM HERE, WE CAN ADD THE FILES TO THE ARRAY.
REM ENDWHILE

REM CLOSE #file%

originalwords$() = words$()

REM Convert the words to numbers
FOR i%=0 TO 25
	word$ = words$(i%)
	FOR j%=0 TO LENword$
		ascii% = ASC(MID$(word$,j%,1))
		
		IF ascii% >= 65 AND ascii% <= 67 THEN
			MID$(word$, j%, 1) = "2"
		ENDIF
		
		IF ascii% >= 68 AND ascii% <= 69 THEN
			MID$(word$, j%, 1) = "3"
		ENDIF
		
		IF ascii% >= 70 AND ascii% <= 73 THEN
			MID$(word$, j%, 1) = "4"
		ENDIF
		
		IF ascii% >= 74 AND ascii% <= 76 THEN
			MID$(word$, j%, 1) = "5"
		ENDIF
		
		IF ascii% >= 77 AND ascii% <= 79 THEN
			MID$(word$, j%, 1) = "6"
		ENDIF
		
		IF ascii% >= 80 AND ascii% <= 83 THEN
			MID$(word$, j%, 1) = "7"
		ENDIF
		
		IF ascii% >= 84 AND ascii% <= 86 THEN
			MID$(word$, j%, 1) = "8"
		ENDIF
		
		IF ascii% >= 87 THEN
			MID$(word$, j%, 1) = "9"
		ENDIF
		
	NEXT j%
	
	words$(i%) = word$
NEXT i%

REM Read the numbers to be predicted
numbers$ = ""
INPUT "Enter numbers: "; numbers$

REM loop through words, and look for coincidences
FOR i%=0 TO LENnumbers$
	FOR j%=0 TO 25
		IF words$(j%) <> "" THEN
			IF LENwords$(j%) < i% THEN
				words$(j%) = ""
				
			ELSE
				IF MID$(words$(j%), i%, 1) <> MID$(numbers$, i%, 1) THEN
					words$(j%) = ""
				ENDIF
			ENDIF
		ENDIF
	NEXT j%
NEXT i%

REM Output all possible solutions
FOR i%=0 TO 25
	IF words$(i%) <> "" THEN
		PRINT originalwords$(i%)
	ENDIF
NEXT i%
