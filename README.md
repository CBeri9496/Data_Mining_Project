# Data_Mining_Project

# CHARACTERIZING VICTIMS OF IDENTITY THEFT

# Overview

+ We acquired an Identity Theft Supplement (ITS) to the National Crime Victimization Survey (NCVS). 
+ From January to June 2012, the ITS collected data from persons who experienced one or more attempted or successful incidents of identity theft during the 12 months preceding their interview. 
+ Approximately 16.6 million persons or 7% of all U.S. residents age 16 or older, were victims of one or more incidents of identity theft on 2012. 
+ Direct and indirect losses from identity theft totaled $24.7 billion in 2012. 
+ Among identity theft victims, existing bank (37%) or credit card accounts (40%) were the most common types of misused information.
+ About 14% of identity theft victims experienced out-of-pocket losses of $1 or more. 
+ Of these victims, about half suffered losses of less than $100. 
+ Over half of identity theft victims who were able to resolve any associated problems did so in a day or less; among victims who had personal information used for fraudulent purposes, 29% spent a month or more resolving problems. 
+ About 36% of identity theft victims reported moderate or severe emotional distress as a result of the incident before, we were interested in two main things: 
+ 1. It focuses on the most recent incident experienced to describe victim characteristics and victim responses to identity theft. 
+ 2. In addition to suffering monetary losses, some identity theft victims experienced other financial and legal problems.


# Data

+ Since this data comes from a survey, there were many records that had “bad” data. 
+ We ended up eliminating some of the data due to missing, invalid or inconsistent occurrences. 
+ This report uses data that differ from previous BJS statistical collections on the topic of identity theft. 
+ A final sample size of 69,814 of the original NCVS-eligible respondents completed the ITS questionnaire, resulting in a response rate of 91.9%. 
+ All of the data obtained from the bjs and datasets maintained at http://www.bjs.gov/index.cfm?ty=tp&tid=42
+ Dataset(s): National Crime Victimization Survey: Identity Theft Supplement, 2012
+ All of the data is in CSV format files. 
+ Those will make easy to do analysis on datasets. 
+ WEKA or WEKA with JAVA will be use to do the data analysis. 
+ There we will be going to use K-Mean Cluster and Classification algorithms for research questions. 

# Research Questions
+ Some of the questions we wanted to explore those are: 
+ 1. Are men or women more prone to being victims of identity theft? 
+ 2. Is the economic impact of identity theft is comprised of direct and indirect financial loss? 
+ 3. Does victims suffered with any emotional distress experience while resolving the problem?

+ To get answers for research questions we have used WEKA tool. 
+ We have found k-mean clustering analysis through WEKA with using related datasets. 
+ Below explations are research answers

To get answers we have used codebook. Which contained all related data set variable names.
1. Are men or women more prone to being victims of identity theft?
Principal_Person_Sex:
V2036 - PRINCIPAL PERSON SEX (ALLOCATED)

# 1. Principal Person - Sex
+ Notes: Variables V2032 through V2041 represent principal person information.

Value      Label
1             Male
2             Female
8             Residue
9 (M)     Out of universe
Answer: It has only one attribute that is V2036. Here we have collected 25001 people’s data. With the help of these data we have done some analysis. With using Simple K-Mean clustering analysis we found who are more prone to being victims of identity theft. Here 20640 people are female which means 83% of Female is victims in identity theft and 4361 are male which means 17% of male got prone in identity theft. With this analysis we observed most women were being victims than male in the year 2012.

# 2. Is the economic impact of identity theft is comprised of direct and indirect financial loss?
# EconomicImpact_DirectLoss:
In this task we have used 8 attributes and 25001 person’s data. We used Simple K-Mean Clustering analysis to analyze the data. We used 12 cluster points. With this clustering analysis we found some answers. Those are mentioned in every attribute’s answers section. 
Here, Every Attribute describes the following data:
V4317_1 = Other Items on Person

Value        Label
1                Yes
2                No
8                Residue
9 (M)        Out of universe

Answer: With this attribute we found most of the cases like 24942 people are out of universe, 56 people were didn’t get by theft. One person is residue. Only just 2 people got theft on person  with other items. So finally we have found that 0.0079% of people got theft on person.

V4318_1 = 1st Attempted theft item on person

Value        Label
04             Credit cards, checks, bank cards
05             Cars
06             Other motor vehicle
07             part of motor vehicle, (tire, hubcap, attach tape deck, attached CB radio, etc.)
08             Gasoline or oil
09             Bicycle or parts
10             TV, Stereo, other household appliances
11             Silver, china, art objects
12             Other house hold furnishings (furniture, rugs, etc.)
13             Personal effect (clothing, jewelry, toys, etc.)
14             Handgun (pistol, revolver)
15             Other firearms (rifle, shotgun)
16             Other
17             Don’t know
40             Tired to take everything marked in item 90 [V4292-V4308] directly from respondent
98             Residue
99             Blank or Original entry was 01 (cash) 02 (purse) 03 (wallet)

Answer: This attribute is about 1st time attempted theft on person. With this attribute we found most of the cases like 24998 people are under the list of blank or original entry was 01 (cash) 02 (purse) 03 (wallet). One person got theft on his/her personal effect. One person is residue and the other one is in other category. So finally from this attribute we can observe that only just one person got theft out of 25001 people.

V4319_1 = 2nd Attempted theft item on person

Value         Label
04              Credit cards, checks, bank cards
05              Cars
06              Other motor vehicle
07              part of motor vehicle, (tire, hubcap, attach tape deck, attached CB radio, etc.)
08              Gasoline or oil
09              Bicycle or parts
10              TV, Stereo, other household appliances
11              Silver, china, art objects
12              Other house hold furnishings (furniture, rugs, etc.)
13              Personal effect (clothing, jewelry, toys, etc.)
14              Handgun (pistol, revolver)
15              Other firearms (rifle, shotgun)
16              Other
17              Don’t know
40              Tired to take everything marked in item 90 [V4292-V4308] directly from respondent
98              Residue
99              Blank or Original entry was 01 (cash) 02 (purse) 03 (wallet)

Answer: This attribute is about 2nd time attempted theft on person. With this attribute we found that no one did not get theft on person. 25001 people are under the blank or Original entry was 01 (cash) 02 (purse) 03 (wallet). So from this attribute 0% of theft has done on person in 2nd time.

V4320_1 = 3rd  Attempted theft item on person

Value           Label
04                Credit cards, checks, bank cards
05                Cars
06                Other motor vehicle
07                part of motor vehicle, (tire, hubcap, attach tape deck, attached CB radio, etc.)
08                Gasoline or oil
09                Bicycle or parts
10                TV, Stereo, other household appliances
11                Silver, china, art objects
12                Other house hold furnishings (furniture, rugs, etc.)
13                Personal effect (clothing, jewelry, toys, etc.)
14                Handgun (pistol, revolver)
15                Other firearms (rifle, shotgun)
16                Other
17                Don’t know
40                Tired to take everything marked in item 
90                [V4292-V4308] directly from respondent
98                Residue
99                Blank or Original entry was 01 (cash) 02 (purse) 03 (wallet)

Answer: This attribute is about 3rd time attempted theft on person. We found analysis same as like V4319_1 attribute. With this attribute we found that no one did not get theft on person. 25001 people are under the blank or Original entry was 01 (cash) 02 (purse) 03 (wallet). So from this attribute 0% of theft has done on person in 3rd time. 

V4360_1 = Other Items on Person

Value          Label
1                  Yes
2                  No
8                  Residue
9 (M)          Out of universe

Answer: This attribute is about other items got theft on person. With this attribute we found 24167 people are under out of universe. 824 people did not have theft on person. One person is under residue. 9 person’s got theft on person. Finally, from this attribute we found that only 9 people got theft other items on person.

V4361_1 = 1st Item taken on person

Value           Label
04                Credit cards, checks, bank cards
05                Cars
06                Other motor vehicle
07                part of motor vehicle, (tire, hubcap, attach tape deck, attached CB radio, etc.)
08                Unattached motor vehicle accessories or equipment (unattached radio, etc.)
09                Gasoline or oil
10                Bicycle or parts
11                TV, Stereo, other household appliances
12                Silver, china, art objects
13                Other house hold furnishings (furniture, rugs, etc.)
14                Portable electronic and photographic gear (Personal stereo, TV, calculator, camera)
15               Clothing, furs, luggage, briefcase
16               Jewelry, watch, keys
17               Collection of stamps, coins, etc.
18               Toys, sports, and recreation equipment, (not listed above)
19               Other personal and portable items
20               Handgun (pistol, revolver)
21               Other firearm (rifle, shotgun)
22               Tools, machines, office equipment
23               Farm or garden produce, plants, fruits, logs
24               Animals - pet or livestock
25               Food or liquor
26               Other
27               Don't know
40               Everything marked in V4326-V4349 was taken directly from respondent
98               Residue
99               Blank or original entry was 01 (cash), 02 (purse), or 03 (wallet)

Answer: This attribute has 1st item was theft on person. From this attribute we found 24991 people are under blank or original entry was 01 (cash), 02 (purse), or 03 (wallet) list. 2 persons are under residue. 4 members got theft on Portable electronic and photographic gear (Personal stereo, TV, calculator, camera, etc.). 2 members got theft on Jewelry, watch, keys. One person got theft on Clothing, furs, luggage, briefcase. One person got theft on Other personal and portable items. So totally, out of 25001 people only 8 persons got theft on 1st item on person.

V4362_1 = 2nd Item taken on person

Value           Label
04                Credit cards, checks, bank cards
05                Cars
06                Other motor vehicle
07                part of motor vehicle, (tire, hubcap, attach tape deck, attached CB radio, etc.)
08                Unattached motor vehicle accessories or equipment (unattached radio, etc.)
09                Gasoline or oil
10                Bicycle or parts
11                TV, Stereo, other household appliances
12                Silver, china, art objects
13                Other house hold furnishings (furniture, rugs, etc.)
14                Portable electronic and photographic gear (Personal stereo, TV, calculator, camera, )
15               Clothing, furs, luggage, briefcase
16               Jewelry, watch, keys
17               Collection of stamps, coins, etc.
18               Toys, sports, and recreation equipment, (not listed above)
19               Other personal and portable items
20               Handgun (pistol, revolver)
21               Other firearm (rifle, shotgun)
22               Tools, machines, office equipment
23               Farm or garden produce, plants, fruits, logs
24               Animals - pet or livestock
25               Food or liquor
26               Other
27               Don't know
40               Everything marked in V4326-V4349 was taken directly from respondent
98               Residue
99               Blank or original entry was 01 (cash), 02 (purse), or 03 (wallet)

Answer: This attribute has 2nd item was taken on person. In this attribute 25001 people are under blank or original entry was 01 (cash), 02 (purse), or 03 (wallet).

V4363_1 = 3rd Item taken on person
Value          Label
04               Credit cards, checks, bank cards
05               Cars
06               Other motor vehicle
07               part of motor vehicle, (tire, hubcap, attach tape deck, attached CB radio, etc.)
08               Unattached motor vehicle accessories or equipment (unattached radio, etc.)
09               Gasoline or oil
10               Bicycle or parts
11               TV, Stereo, other household appliances
12               Silver, china, art objects
13               Other house hold furnishings (furniture, rugs, etc.)
14               Portable electronic and photographic gear (Personal stereo, TV, calculator, camera)
15               Clothing, furs, luggage, briefcase
16               Jewelry, watch, keys
17               Collection of stamps, coins, etc.
18               Toys, sports, and recreation equipment, (not listed above)
19               Other personal and portable items
20               Handgun (pistol, revolver)
21               Other firearm (rifle, shotgun)
22               Tools, machines, office equipment
23               Farm or garden produce, plants, fruits, logs
24               Animals - pet or livestock
25               Food or liquor
26               Other
27               Don't know
40               Everything marked in V4326-V4349 was taken directly from respondent
98               Residue
99               Blank or original entry was 01 (cash), 02 (purse), or 03 (wallet)

Answer: This attribute has 3rd item taken on person. After doing analysis on this attribute we found it is also same like V4362_1. All people are under blank original entry was 01 (cash), 02 (purse), or 03 (wallet).

# EconomicImpact_InDirectLoss:
 In this task we have used 5 attributes and 25001 person’s data. We used Simple K-Mean Clustering analysis to analyze the data. We used 12 cluster points. With this clustering analysis we found some answers. Those are mentioned in every attribute’s answers section. 
+ Here, Every Attribute describes the following data: 

VS298 = Approximate to total dollar amount of what someone obtained during (the most recent) incident.

Record estimated amount 0000000-0999996 Amount of total loss related to attempted misuse of personal information

Value                Label
0999998         	 Residue
9999998           Refused
9999999           Don't know
0999999 (M)  	 Out of Scope

Answer: This attribute has information like how much amount victims has lost by indirectly. 23675 people are refused $1999,998 amount. 106 people didn’t know how they lost $16000191.6 amount. 1230 people were lost $5583.57 amount because of misuse their personal information.

VS299 = Of the amount obtained, how much did you personally lose

Record estimated amount 0000000-0999996 Amount of personal loss related to attempted misuse of personal information

Value                  Label
0999998            Residue
9999998            Refused
9999999            Don't know 
0999999 (M)    Out of Scope

Answer: This attribute has information about how amount has lost personally. 24107 peoples are refused $5480352 amount. 796 people are lost ZERO amount. 98 people are lost $2526.20 has lost amount because of their losing personal information.  

VS300 = Amount of additional costs incurred

Record estimated amount 0000000-0999996 Amount of additional cost related to attempted misuse of personal information 

Value                     Label
0999998               Residue
9999998               Refused
9999999               Don't know
0999999 (M)       Out of Scope

Answer: This attribute has how much amount of additional costs incurred. 24906 people are refused $7999992 amount. Only 95 members were got additionally charged amount of $7158.52.

VS301 = How much costs did you incur

Record estimated amount 0000000-0999996 Amount of incurred cost related to attempted misuse of personal information

Value                    Label
0999998               Residue
9999998	     Refused
9999999 	     Don't know
0999999 (M) 	     Out of Scope

Answer: This attribute explains how much costs incur by victims. 23773 people are incurred $3999996 amount. 15 people were refused $9999998.867 amount. 1213 people were incurred with $77.596 amount. 15 members were don’t know $9999998.867 amount.
 
VS358 = Prior identity theft: costs incurred

Value                   Label
01                      $0 - $50
02                      $51 - $100
03                      $101 - $500
04                      $501 - $1000
05                      $1001 - $4999
06                      $5,000 or more
08                      Residue
98                      Refused
99                      Don't know
09 (M)               Out of Scope 

Answer: This attribute has information about costs incurred with prior identity theft. 24801 members were out of scope. 9 people were incurred with $0-$50 amount. 5 members were incurred with $1001-$4999 amount. 91 people were incurred with $101-$500 amount. 95 members were under residue list.

+ 3. Does victims suffered with any emotional distress experience while resolving the problem?

+ Emotional_Distress:

V4526H5_1: CONDTN 6 MO+ DIFFICULT: LEARN, REMEMBER, CONCENTRATE 

Value      Label
1              Yes
2              No
8              Residue
9              Out of universe
-1 (M)      Invalid until 2007 Q1

Answer: This attribute has information about CONDTN 6 MO+ DIFFICULT: LEARN, REMEMBER, CONCENTRATE (START 2007 Q1) incur by victims.23938 members are out of universe.11 members are residue .981 members were not having emotional distress.79 members
are facing with emotional distress.

V4526H6_1 - CONDTN 6 MO+ DIFFICULT: DRESSING, BATHING, GET AROUND HOME 

Value        Label
1 	     Yes
2 	     No
8 	     Residue
9 	     Out of universe
-1 (M) 	Invalid until 2007 Q1
Answer: This attribute has information aboutV4526H6_1 - CONDTN 6 MO+ DIFFICULT: DRESSING, BATHING, GET AROUND HOME (START 2007 Q1) incur by victims.23938 members are out of universe.4 members are residue.1033members were not having emotional
Distress. 26 members are facing with the emotional distress. 

V4526H7_1 - CONDTN 6 MO+ DIFFICULT: GO OUTSIDE HOME TO SHOP OR DR OFFICE (START 2007 Q1) 
Value         Label
1                Yes
2                No
8 	          Residue
9 	        Out of universe
-1 (M) 	      Invalid until 2007 Q1
Answer: This attribute has information about CONDTN 6 MO+ DIFFICULT: GO OUTSIDE HOME TO SHOP OR DR OFFICE incur by victims.23938 members are out of universe.3members are residue.997members were not having emotional distress.63 members are facing with the emotional distress.

# Now I am going to explore some interesting things:

# Financial_Problems:

VS102 - DID YOU CONTACT SOMEONE AT CREDIT CARD COMPANY OR FINANCIAL INSTITUTION ABOUT MISUSE? 

Value        label
01             Yes 
02             No 
08             Residue 
98             Refused 
99             Don't know 
09(M)      Out of Scope
 
Answer: This attribute has information aboutVS102 - did you contact someone at Credit Card Company or financial institution about misuse.23666 members fall in out of scope .1335 members facing with the financial problems.

VS103 - CONTACT SOMEONE AT CREDIT CARD COMPANY OR FINANCIAL INSTITUTION FLAG 

Value          label
0                 Original values for CONTACT_ANYONE was not changed 
1                 Original value for TALK_CREDIT_BUREAU was changed during the literal     response   review. 
9                 TALK_CREDIT_BUREAU was off path and blanked 

Answer: This attribute has information aboutvs103 - contact someone at credit card company or financial institution flag .23666 members fall in the group where the TALK_CREDIT_BUREAU was off path and blanked .91 members have Original value for CONTACT_ANYONE was not changed. 

VS302 - HAVE YOU BEEN SUCCESSFUL IN CLEARING UP FINANCIAL AND CREDIT PROBLEMS

Value            label
01                  Yes 
02                  No 
08                  Residue 
98                  Refused 
99                  Don't know 
09(M)            Out of Scope 

Answer: This attribute has information about VS302 - have you been successful in clearing up financial and credit problems.23666 members fall in out of scope. 1335 members facing with the financial problems.

VS303 - HOW LONG DID IT TAKE YOU TO CLEAR UP FINANCIAL AND CREDIT PROBLEMS

Value              label
01                   One day or less (1-24 hours) 
02                   More than a day, but less than a week (25 hours-6 days) 
03                   At least a week, but less than one month (7-30 days 
04                   One month to less than three months 
05                   Three months to less than six months 
06                   Six months to less than one year 
07                   One year or more 
08                   Residue 
98                   Refused 
99                   Don't know 
09(M)             Out of Scope 

Answer: This attribute has information aboutVS303 - HOW LONG DID IT TAKE YOU TO CLEAR UP FINANCIAL AND CREDIT PROBLEMS. 23666 members fall in out of scope.1335 has One day or less (1-24 hours) TO CLEAR UP FINANCIAL AND CREDIT PROBLEMS

VS304 - HOW MANY HOURS WERE SPENT CLEARING UP FINANCIAL AND CREDIT PROBLEMS

Value               label
09998              Residue (response not provided during original interview) 
99998              Refused 
99999              Don't know 
09999(M)        Out of scope 

Answer: This attribute has information aboutVS304 - HOW MANY HOURS WERE SPENT CLEARING UP FINANCIAL AND CREDIT PROBLEMS. 23666 members fall in out of scope.69 members has refused on how many hours spent clearing up fincial and credit problems .

VS359 - PRIOR IDENTITY THEFT: HOW LONG DID IT TAKE YOU TO CLEAR UP FINANCIAL AND CREDIT PROBLEMS

Value                label
 01                    One day or less (1-24 hours) 
 02                    More than a day, but less than a week (25 hours-6 days  )
 03                    At least a week, but less than one month (7-30 days) 
 04                    One month to less than three months 
 05                    Three months to less than six months 
 06                    Six months to less than one year 
 07                    One year or more 
 08                    Residue
 98                    Refused
 99                    don’t know 
 09 (M)            Out of Scope 

Answer: This attribute has information aboutVS359 - prior identity theft: how long did it take you to clear up financial and credit problems.23673 members fall in out of scope .1328 members fall is residue.

VS360 - PRIOR IDENTITY THEFT: HOW MUCH TIME WAS SPENT TRYING TO CLEAR UP FINANCIAL AND CREDIT PROBLEMS 

Value               label
001                  One day or less (1-24 hours)
002                  More than a day, but less than a week (25 hours-6 days  
003                  At least a week, but less than one month (7-30 days)
004                  One month to less than three months
005                  Three months to less than six months 
006                  Six months to less than one year 
007                  One year or more 
008                  More than five years 
098                  Residue  
998                  Refused
999                  don’t know 
099 (M)          Out of Scope 

Answer. This attribute has information aboutVS360 - prior identity theft: how much time was spent trying to clear up financial and credit problems.23452 members fall in out of scope.

VS363 - ACTIONS TO AVOID IDENTITY THEFT: CHANGED PASSWORDS ON FINANCIAL ACCOUNTS

Value                label
01                     Yes 
02                     No 
08                     Residue 
98                     Refused 
99                     Don't know 
09(M)               Out of Scope
 
Answer: This attribute has information aboutVS363 - actions to avoid identity theft: changed passwords on financial accounts.  7783 members fall in out of scope. 138 members are refused in actions to avoid identity theft .17183 members take the actions to avoid identity theft.

VS010 - DURING THE PAST 12 MONTHS HAVE YOU HAD AT LEAST ONE BANK ACCOUNT

Value                  label
 01                      Yes 
 02                      No 
 08                      Residue 
 98                      Refused 
 99                      Don't know 
 09(M)                Out of Scope
 
Answer: This attribute has information aboutVS010 - DURING THE PAST 12 MONTHS HAVE YOU HAD AT LEAST ONE BANK ACCOUNT. 7783 members fall in out of scope.2150 members were  not having at least one bank account during the past 12 months .15068 members were having at least one bank account during the past 12 months .

VS330 - PRIOR IDENTITY THEFT: STILL EXPERIENCING PROBLEMS

Value                    label
 01                        Yes 
 02                        No 
 08                        Residue 
 98                        Refused 
 99                        Don't know 
09(M)                      Out of Scope 

Answer: This attribute has information aboutvs330 - prior identity theft: still experiencing problems.22053members fall in out of scope.310 members were fall in residue.145 member’s prior identity theft and still experiencing problems.

VS331 - PRIOR IDENTITY THEFT: EXPERIENCED PROBLEMS IN THE PAST YEAR

Value                    label
 01                        Yes 
 02                        No 
 08                        Residue 
 98                        Refused 
 99                        Don't know 
 09(M)                     Out of Scope 

  Answer: This attribute has information aboutvs331 - prior identity theft: experienced problems in the past year.22047members fall in out of scope.310 members were fall in residue.1294 members were not having experienced problems in the past year.

V4482B_1 - COLLAPSED OCCUPATION CODE (START 2001 Q3) 

Value                   label
-1                         Invalid until 2001 Q3 
01                        Management occupations 
02                        Business and financial operations occupations 
03                        Computer and mathematical occupations 
04                        Architecture and engineering occupations 
05                        Life, physical, and social science occupations 
06                        Community and social services occupations 
07                        Social worker 
08                        Health Care Aide 
09                        Legal occupations
10                        Education, training, and library occupations
11                        Preschool (Prekindergarten and kindergarten)
12                        Elementary
13                        Junior high or middle school
14                        High school
15                        College or university
16                        Technical or industrial school
17                        Special education facility
18                        Arts, design, entertainment, sports, and media occupations
19                        Healthcare practitioners and technical occupations
20                        Physician
21                        Nurse
22                        Health Technician
23                        Healthcare support/service occupations
24                        Protective service occupations
25                        Law enforcement officer
26                        Prison or jail guard
27                        Security Guard
28                        Food preparation and serving related occupations
29                        Building and grounds cleaning and maintenance occupations
30                        Personal care and Service occupations
31                        Sales and related occupations
32                        Grocery, convenience, or liquor store clerk
33                        Gas station attendant
34                        Bartender
35                        Office and administrative support occupations
36                        Farming, fishing, and forestry occupations
37                        Construction and extraction occupations
38                        Installation, maintenance, and repair occupations
39                        Production occupations
40                        Transportation and material moving occupations
41                        Bus driver
42                        Taxi cab drivers and chauffeurs
43                        Military specific occupations
44                        Other
99                        Out of universe

Answer: This attribute has information aboutv4483_1 - job located in city/suburb/rural area.16955 members fall in out of universe.22 members are gas station attendant .22 members are having Healthcare support/service occupations.34 members were having Health Care Aide.

# Legal_Problems:

VS315 - EXPERIENCED ANY OF THE FOLLOWING: HAD LEGAL PROBLEMS

Value          label
1                 Response selected
2                 Don't Know
3                 Refused
8                 Residue
9 (M)          Out of Scope

Answer: This attribute has information aboutVS315 - EXPERIENCED ANY OF THE FOLLOWING: HAD LEGAL PROBLEMS.23666 members are out of scope. 9 members are residue.

VS316 - HAD LEGAL PROBLEMS FLAG 

Value           label
0                  Original value for LEGAL_PROBS was not changed 
1                  Original value for LEGAL_PROBS was changed during the literal response review. 
9                  LEGAL_PROBS was off path and blanked 

Answer: This attribute has information aboutVS316 - HAD LEGAL PROBLEMS FLAG .24888 members were having LEGAL_PROBS was off path and blanked.1335 members Original value for LEGAL_PROBS was not changed.

VS353 - PRIOR IDENTITY THEFT: HAD LEGAL PROBLEMS 

Value       label
01	    Yes 
02 	    No 
08 	    Residue 
98 	    Refused 
99 	    Don't know 
09(M)      Out of Scope
 
Answer: This attribute has information aboutvs353 - prior identity theft: had legal problems.24867 members are out of scope .9 members having residue .115 members are not having prior identity theft .10 members having actual prior identity theft.

VS354 - LEGAL PROBLEMS - PRIOR FLAG 

Value     Label
0           Original value for LEGAL_PROB_PRIOR was not changed
1           Original value for LEGAL_PROB_PRIOR was changed during the literal response 
9           LEGAL_PROB_PRIOR was off path and blanked

Answer: This attribute has information aboutvs354 - legal problems - prior flag.24867 member’s legal problem prior was off path and blanked.134 members’ Original value for LEGAL_PROB_PRIOR was not changed.

VS330 - PRIOR IDENTITY THEFT: STILL EXPERIENCING PROBLEMS

Value        Label
01	     Yes
02 	     No 
08 	     Residue 
98 	     Refused 
99 	     Don't know 
09(M)	     Out of Scope

Answer: This attribute has information about vs330 - prior identity theft: still experiencing problems.23347 members having out of scope .3 members are refused .9 members were residue.1673 members were not had prior identity theft .32 members were prior having identity theft and still having experiencing problems.

# Most_Recent:

VS090 - MOST RECENT INCIDENT: MISUSE OR ATTEMPTED MISUSE OF AN EXISTING CREDIT CARD ACCOUNT 

Value          Label
0                 Response not selected
1                 Response selected
2                 Don't Know
3                 Refused
8                 Residue
9 (M)         Out of Scope

Answer :This attribute has information abouts090 - most recent incident: misuse or attempted misuse of an existing credit card account. 24920 members are out of scope .8 members were residue.43 members response was not selected .30 members misuse or attempted misuse of an existing credit card account .

VS091 - MOST RECENT INCIDENT: MISUSE OR ATTEMPTED MISUSE OF AN EXISTING BANK ACCOUNT 

Value              Label
0                      Response not selected
1                      Response selected
2                      Don't Know
3                      Refused
8                      Residue
9 (M)              Out of Scope 

Answer: This attribute has information aboutVS091 - MOST RECENT INCIDENT: MISUSE OR ATTEMPTED MISUSE OF AN EXISTING BANK ACCOUNT. 24920 members are out of scope. 8 members were residue.39 members response was not selected .34 members were having most recent incident: misuse or attempted misuse of an existing bank account.

VS092 - MOST RECENT INCIDENT: MISUSE OR ATTEMPTED MISUSE OF OTHER EXISTING ACCOUNT 

Value               Label
0                      Response not selected
1                      Response selected
2                      Don't Know
3                      Refused
8                      Residue
9 (M)              Out of Scope 

Answer: This attribute has information aboutvs092 - most recent incident: misuse or attempted misuse of other existing account.24920 members are out of scope. 8 members were residue.67 members response was not selected.6 members has misuse or attempted misuse of other existing account.

VS093 - MOST RECENT INCIDENT: MISUSE OR ATTEMPTED MISUSE TO OPEN A NEW ACCOUNT 

Value              Label
0                     Response not selected
1                     Response selected
2                     Don't Know
3                     Refused
8                     Residue
9 (M)             Out of Scope 

Answer: This attribute has information aboutvs093 - most recent incident: misuse or attempted misuse to open a new account. 24920 members are out of scope. 8 members were residue.65 members response was not selected.8 members has misuse or attempted misuse to open a new account.

VS094 - MOST RECENT INCIDENT: MISUSE OR ATTEMPTED MISUSE FOR OTHER FRAUDULENT PURPOSES 

Value              Label
0                     Response not selected
1                     Response selected
2                     Don't Know
3                     Refused
8                     Residue
9 (M)             Out of Scope 

Answer: This attribute has information aboutvs094 - most recent incident: misuse or attempted misuse for other fraudulent purposes24920 members are out of scope. 8 members were residue.68 members response was not selected.4 members misuse or attempted misuse for other fraudulent purposes.

# Code and Application
+ Added Code in Seperate Code Folder
+ Here we use python program to get datasets.
# Code:
+ import sys
+ import random

+ SKIP_INTERVAL = 25

+ def process_input_file(filename, variables, sep='\t', output_size=10, random_lines=False):
+    with open(filename) as fi:
+        variables_indices = []
+       # intialize the lines to skip
+        if random_lines:
+            skip_count = random.randint(1, SKIP_INTERVAL)
+        else:
+            skip_count = 0
+       # process the header -> get the index # of the variables and store them (in order)
+        header = fi.next().split()
+        for v in variables:
+            variables_indices.append(header.index(v))
+       # process the rest of the file
+        line_count = 0
+        for line in fi:
+            if skip_count:
+                skip_count -= 1
+            else:
+                if line_count < output_size+1:
+                    line_data = line.split()
+                    print sep.join([line_data[v] for v in variables_indices])
+                    line_count += 1
+                if random_lines: # re-initialize
+                        skip_count = random.randint(1, SKIP_INTERVAL)
+                else:
+                    break # we need not process more of the file than necessary
+ def main():
+    fname = "D:\\DataSets\\ICPSR_34735\\DS0001\\34735-0001-Data.tsv"
+ # Principal_Person_Sex   
+  process_input_file(fname, ["V2036"], output_size=250, random_lines=True, sep=',')
+ #EconomicImpact_DirectLoss
+    process_input_file(fname, ["V4317_1","V4318_1","V4319_1","V4320_1","V4360_1","V4361_1","V4362_1","V4363_1"], output_size=250, + + + random_lines=True, sep=',')
+ #  EconomicImpact_IndirectLoss
+   process_input_file(fname, ["VS298","VS299","VS300","VS301","VS358"], output_size=250, random_lines=True, sep=',')
+ #  Financial_Problems
+   process_input_file(fname, ["VS102","VS103","VS302","VS303","VS304","VS359","VS360","VS363","VS010","VS330","VS331","V4482B_1"], + + output_size=250, random_lines=True, sep=',')
+ #  Legal_Problems
+  process_input_file(fname, ["VS315","VS316","VS353","VS330","VS331"], output_size=250, random_lines=True, sep=',')
+ # Most_Recent  
+  process_input_file(fname, ["VS090","VS091","VS092","VS093","VS094"], output_size=250, random_lines=True, sep=',')
+ if __name__ == "__main__":
+    main()
+ With the help of the above program we found all datasets which will help to get answers for the Research questions.


# Project Management

+ Our team consists of five members:
+   Chandana Beri 
+   Nagesh Reddy Thum 
+   Shireesha bekkari
+   Ravi Teja Kollipara  
+   Srichand Alapati 

# Project Team, deliverables and checkpoints

# Team Members

     Team Member                Roles and Skills               Contributions
 
   
     CHANDANA BERI              Project Handling               Total project status will be updated and submitted accordingly
                                                               Will handle each and every phase
                                                               Gone through all the roles thoroughly
  
     NAGESH REDDY THUM          Data Analysis, Coding          Data Analysis and Coding
   
     SHIREESHA BEKKARI          Backend	                       Working on WEKA
     
     RAVI TEJA KOLLIPARA        Testing	                       Debugging
   
     SRICHAND ALAPATI	       Data Analysis, Coding          Data Analysis and Coding



# Deliverable and Checkpoints


     Checkpoint date               Expected Deliverable                Responsible team members(s)               Checkpoint results

     15/02/2016                    Update Project Report               CHANDANA BERI, NAGESH THUM                Collected more data
                                   on Data, team, Project                                                        and add Research
                                   Managemen and formulate                                                       questions. 
                                   questions.
                                   
     15/03/2016                    Add Research Questions              CHANDANA BERI                             Added more DATA and                                                                                                              Reasearch questions
     
     11/04/2016                    Update Project Code and Data        NAGESH REDDY THUM, SRICHAND ALAPATI       Initial code/analysis                                   Analysis                                                                  checked in to GITHUB                                                                                                             and Collected Data                                                                                                               for Reasearch                                                                                                                    Questions.
     
     18/04/2016                    Update Datasets                     NAGESH REDDY THUM, SRICHAND ALAPATI       Updated Datasets
                                   
     25/04/2016                    Update Research answers             RAVI TEJA KOLLIPARA, SHIREESHA BEKKARI    Updated Research                                                                                                                 Answers

# Conclusion: 

+ Based on the all the information provided by the victims of identity theft, the conclusions are segregated based on financial   issues, legal issues, direct, indirect loss, emotional distress, most recent issues, and principal of persons. Form these we got most of the women were victims (83%), very less people faced with direct, indirect, financial, legal, most recent, emotional distress issues.
