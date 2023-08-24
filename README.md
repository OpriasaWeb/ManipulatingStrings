# Manipulating Strings

Instructions: You are making a text editor and need to implement find/replace functionality.
The code declares a text string. You need to take two string inputs, which represent the substring to find and what to replace it with in the text.
Your program needs to output the number of replacements made, along with the new text.

For example, for the given text "I weigh 80 kilograms. He weighs 65 kilograms.":

Sample Input
kilograms
kg

Sample Output
2
I weigh 80 kg. He weighs 65 kg.

The program replaced 2 occurrences of the word kilograms with kg.


Pseudocode:





            BEGIN
              DECLARE text equals to "I weigh 80 kilograms. He weighs 65 kilograms."

              DECLARE split the text

              DECLARE input("Find word: ")
              INPUT find

              DECLARE input("Replacement: ")
              INPUT replace

              DECLARE count to check how many INPUT find occurrences, it is equals to 0

              FOR i in split
                IF i in find
                  text replace the find by replace
                  count plus 1
                ENDIF

              ENDFOR

              PRINT count
              PRINT modified text if condition satisfied

            END