# Adventures_in_MachineLearning
A playground for all projects I plan to do related to Machine Learning and Data Science


For the basics.py and the data I have used:

Context: The data were obtained in a survey of students math and portuguese language courses in secondary school. It contains a lot of interesting social, gender and study information about students. You can use it for some EDA or try to predict students final grade. Used and obtained from the University of California, Irvine's Machine Learning Repository hosted on their website

Content: Attributes for both student-mat.csv (Math course) and student-por.csv (Portuguese language course) datasets:

1. school - student's school (binary: 'GP' - Gabriel Pereira or 'MS' - Mousinho da Silveira)
2. sex - student's sex (binary: 'F' - female or 'M' - male)
3. age - student's age (numeric: from 15 to 22)
4. address - student's home address type (binary: 'U' - urban or 'R' - rural)
5. famsize - family size (binary: 'LE3' - less or equal to 3 or 'GT3' - greater than 3)
6. Pstatus - parent's cohabitation status (binary: 'T' - living together or 'A' - apart)
7. Medu - mother's education (numeric: 0 - none, 1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – 8. higher education)
9. Fedu - father's education (numeric: 0 - none, 1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – 10. higher education)
11. Mjob - mother's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')
12. Fjob - father's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')
13. reason - reason to choose this school (nominal: close to 'home', school 'reputation', 'course' preference or 'other')
14. guardian - student's guardian (nominal: 'mother', 'father' or 'other')
15. traveltime - home to school travel time (numeric: 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - >1 hour)
16. studytime - weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)
17. failures - number of past class failures (numeric: n if 1<=n<3, else 4)
18. schoolsup - extra educational support (binary: yes or no)
19. famsup - family educational support (binary: yes or no)
20. paid - extra paid classes within the course subject (Math or Portuguese) (binary: yes or no)
21. activities - extra-curricular activities (binary: yes or no)
22. nursery - attended nursery school (binary: yes or no)
23. higher - wants to take higher education (binary: yes or no)
24. internet - Internet access at home (binary: yes or no)
25. romantic - with a romantic relationship (binary: yes or no)
26. famrel - quality of family relationships (numeric: from 1 - very bad to 5 - excellent)
27. freetime - free time after school (numeric: from 1 - very low to 5 - very high)
28. goout - going out with friends (numeric: from 1 - very low to 5 - very high)
29. Dalc - workday alcohol consumption (numeric: from 1 - very low to 5 - very high)
30. Walc - weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)
31. health - current health status (numeric: from 1 - very bad to 5 - very good)
32. absences - number of school absences (numeric: from 0 to 93)
33. These grades are related with the course subject, Math or Portuguese:

34. G1 - first period grade (numeric: from 0 to 20)
35. G2 - second period grade (numeric: from 0 to 20)
36. G3 - final grade (numeric: from 0 to 20, output target)

References: https://archive.ics.uci.edu/ml/datasets/STUDENT+ALCOHOL+CONSUMPTION

Neural Network: The neural network coded predicts wheher the student has a drinking problem using their past grade history. Since this is a very popular dataset, it was a challenge to not take inspirations from somewhere when I ran into problems. Although I used medium as an inspiration, there were some slight problems in said tutorials that included the merging of datasets(somehow screwed up the accuracy of the predication dataset), as well as the inclusion of some students that did not drink. The dataset was modified to include nly students who drink(to make it easier). 

References: https://medium.com/@curiousily/tensorflow-for-hackers-part-ii-building-simple-neural-network-2d6779d2f91b
