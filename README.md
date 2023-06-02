**Python assignments**

**Question-1
(Iterators_Iterables)**


To find the probability that at least one of the K indices selected will contain the letter: 'a' from given list values.

     • Imported the itertools library to use combinations method.
     • Used loggers for logging the information and warnings.
     • Defined  a function named iterables() to perform Iterables combination.
     • Given ‘n’ , ‘k’ and list values in a variable letters.
     • Converted a combination values using combination( ) method.
     • Counted number of times the ‘a’ keyword is repeated in the letter using conditional statements.
     • Found probability value by dividing count/ length of letters.
     • Using test case verified catual input and expected output was passed.

**Question-2
(Calendar_module)**

Date is given as input and output needs to be only day of given date in capitalized.

     • Imported logging for using Info, warning logs and assigned a file path.
     • Created a function for calendar module.
     • Received the date as input and assigned it to day, month, and year.
     • Used calender.weekday function to get week day.
     • And converted as capitalized and printed output, called funtion in driver file.
     • Verified  the actual input with expected output is passed in testcase file.

**Question-3
 (Floor, ceil, rint)**
 
Task is to print the floor, ceil, and rint values from the array given.

     • Defined a list and received the values by split function.
     • Converted list to array.
     • Used logging for information log.
     • Defined a individual  functions to get the floor, ceil, rint values.
     • Called the function in driver file.
     • Received the expected output and test cases passed

**Question-4
 (Linear algebra)**
 
Given a square matrix  with dimensions n X n. need to find the determinant value as round value.

     • Defined a linear algebra method as linear_alg().
     • Declared an array and received the n values to get the array data.
     • Appended values to the array using loops.
     • Converted the array to matrix using matrix().
     • Determined value is received by linalg.det().
     • Made round value with return value.
     • Called the function in driver file.
     • And used testcase file for verifying the test cases.


**Question-5
 (Python List)**
 
Using a list (list = []). Need to perform the following commands insert, print, remove, append, sort, pop, reverse based on user options.

     • Declared a list [ ] and received input values from user.
     • Users option is stored in a new list.
     • Based on option if Insert ,insert() method is used and added the values tolist.
     • Print() method is used if print is option.
     • To remove a particular value  remove() with index value is received.
     • Finally list values are returned from the function.
     • List_methods function is called in driver file.
     • Using testcase file test cases are verified passed as expected and actual values are same.

**Question-6
 (Marks_Percentage)**
 
Need to read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

     •	Using input() number students records are received in a stu_marks{} dictionary.
     •	Student name and marks are received using map and assigned marks values to separate list.
     •	Student name is used as key and values are assigned as marks.
     •	Based on users option student name is received and verified.
     •	Average of total marks of particular student is calculated in average_matks().
     •	If the record is not found prints as record is not added.
     •	Average_marks() is called in driver files.
     •	And the actual values are verified with expected values in testcase file.
 
**Question-7
(Mean_var_std)**

2-d array is given and need to find the mean, var, std values of the array in given axis.

     • Defined  a function as mean_var() to find mean, var and std values.
     • Used loggers for logging the information and warnings.
     • Received n, m values and array values for n rows.
     • Printed mean, var , and std values in a array for testcases.
     • Using testcase file verified actual input and expected output and passed.
     • Called the function from the driver file.

**Question-8
(min_max)**

Given a 2-D array with dimensions N, M. Task is to perform the min function over axis 1  and then find the max of that.

     • Used loggers for logging the information and warnings.
     • Defined a function min_max( ) to find the min and max values.
     • Imported numpy and created array.
     • Appended the array values using the loop.
     • Assigned min value to a variable using numpy.min(array, axis=1).
     • Using numpy.max(min_axis) found max value. And returned.
     • Function was called and verified with testcase file passed.



**Question-9
(No_Idea)**

There are 2 disjoint sets A and B . and array is compared with each set if belongs to A happiness is +1 and -1 if it belongs to B.

     • Defined a function as no_idea.
     • N and M values are received by input() method.
     • Array values are received from user.
     • A set values and B set values are received.
     • Happiness is initialized as zero.
     • Using loop and conditional statements each array is compared.
     • Id array value is of set A +1 or -1.
     • Final calculated happiness value is returned.
     • Called the function from driver file.
     • Testcases verified actual input and expected output passed.

**Question-10
(Second_max)**

Given the participants' score sheet for the University Sports Day, required to find the runner-up score with given x scores. Store them in a list and find the score of the runner-up.

     • Used loggers for logging the information logs in file.
     • Defined second_max( ) function to find the second maximum value.
     • Received array values and splited using map.
     • Stored the sorted values in a variable and removed duplicate values using set.
     • Once sorted using the -2 index value is received and stored as second max value.
     • Returned the runner up value.
     • Called the function from the driver file.
     • Verified the testcases using the actual input and expected output values passed.

**Question-11
(String_formatting)**

Given an integer n, task is to print the following values for each integer i from 1 to n .Get the values in Decimal,Octal,Hexadecimal (capitalized),Binary.

     • Defined the function as print_formatted().
     • Declared  the list for dec,octa,hexambinary.
     • Used loggers for getting the information weather the flow is correct.
     • Using the control statement appended the values to the lists.
     • For octal,hexa and binary values indexed from [2:] to get only the exact output.
     • Using rjust method required spaces were given in the outpt and printed.
     • Function was called in driver file and verified test cases.

**Question-12
(String mutation)**

Read a given string, change the character at a given index and then print the modified string.

     • Defined a function for mutation of string.
     • Assigned the input old string value.
     • Converting string to list and finding the position of the string.
     • And changing the old string to new by assigning the new character to the string list.
     • Using join method joined the string.
     • Returned the updated string value.
     • Verified the test cases passed.

**Question-13
( validate email Id)**

To find the valid email Id and print in lexicographical order.

     • Defined a function to validate email Id.
     • Using control loop received 3 values as emails individually at each iteration.
     • Verifying If onlt 1- @ is available in mail given.
     • Splitting the strings as @ before and after @ values in different variables.
     • Verifying if the strings are alphanumeric and ‘ – _’ are available each value.
     • Remaining part is verified by extension of ‘.’ After extenstion value is >=3.
     • Verifying if remaining string is alpha numeric.
     • And if valid valid is printed and appended to the list.
     • List value is returned. Test cases is verified.

**Question-14
(Word order)**

Given n  words, to find for each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word.

     • Using loop received the list values and stored.
     • Used loggers for verifying ,if the conditional statements are worked.
     • Finds if the word is available in lsit and counts and stored the count[word].
     • Defined a function to if the word is not in wordlist and count is 0 does not prints the value.
     • Else prints the words .
     • Function is called in driver file.
     • Testes cases is verified actual input is same as expected output is passed.
