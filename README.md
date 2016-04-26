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

+ 1. Principal_Person_Sex 
+ Here we have used only one attribute that is V2036
+ V2036 - PRINCIPAL PERSON SEX (ALLOCATED)
+ Question:
+ Principal Person - Sex
+ Notes: Variables V2032 through V2041 represent principal person information.
+ Value Label
+ 1 Male
+ 2 Female
+ 8 Residue
+ 9 (M) Out of universe

+ Answer :: 83% is Female
+           17% is male

+ 2. EconomicImpact_DirectLoss and Indirect Loss
+ Here, The attributes describes the following data::
+ V4317_1=OTHER ITEMS ON PERSON.
+ V4318_1= 1ST ATTEMPTED THEFT ITEM ON PERSON.
+ V4319_1 =2ND ATTEMPTED THEFT ITEM ON PERSON 
+ V4320_1 =3RD ATTEMPTED THEFT ITEM ON PERSON
+ V4360_1 =OTHER ITEMS ON PERSON 
+ V4361_1 =1ST ITEM TAKEN ON PERSON 
+ V4362_1 =2ND ITEM TAKEN ON PERSON 
+ V4363_1 =3RD ITEM TAKEN ON PERSON.

+ OUTPUT::
+ V4317_1 - OTHER ITEMS ON PERSON::
+ Question:
+ ASK OR VERIFY -- Was there anything (else) the offender(s) tried to take directly from you, for instance, from your pocket or hands, or something that you were wearing?
+ 1= Yes
+ 2 =No
+ 8 =Residue
+ 9 =(M) Out of universe
+ ANSWER ::9=out of universe(96%)

+ V4318_1 - 1ST ATTEMPTED THEFT ITEM ON PERSON
+ Question:Which items did the offender(s) try to take directly from you?
+ 04= Credit cards, checks, bank cards
+ 05 =Car
+ 06 = Other motor vehicle
+ 07 = Part of motor vehicle, (tire, hubcap, attached tape deck, attached CB radio, etc.)
+ 08 = Gasoline or oil
+ 09 =Bicycle or parts
+ 10 =TV, Stereo, other household appliances
+ 11 =Silver, china, art objects
+ 12 = Other household furnishings (furniture, rugs, etc.)
+ 13 =Personal effect (clothing, jewelry, toys, etc.)
+ 14 =Handgun (pistol, revolver)
+ 15 =Other firearms (rifle, shotgun)
+ 16 = Other
+ 17= Don't know
+ 40 =Tried to take everything marked in item 90 [V4292-V4308] directly from respondent
+ 98 = Residue
+ 99 = Blank or original entry was 01 (cash), 02 (purse), or 03 (wallet)
+ ANSWER ::  99 = Blank or original entry was 01 (cash), 02 (purse), or 03 (wallet)
+ Coder Instructions (96%)
+ V4319_1 - 2ND ATTEMPTED THEFT ITEM ON PERSON
+ Question: Which items did the offender(s) try to take directly from you?
+ Second Incident
+ 04 =Credit cards, checks, bank cards
+ 05 =Car
+ 06 =Other motor vehicle
+ 07 =Part of motor vehicle, (tire, hubcap, attached tape deck, attached CB radio, etc.)
+ 08 =Gasoline or oil
+ 09 =Bicycle or parts
+ 10 =TV, Stereo, other household appliances
+ 11 =Silver, china, art objects
+ 12 =Other household furnishings (furniture, rugs, etc.)
+ 13 =Personal effect (clothing, jewelry, toys, etc.)
+ 14 =Handgun (pistol, revolver)
+ 15 =Other firearms (rifle, shotgun)
+ 16 =Other
+ 17 =Don't know
+ 40 =Tried to take everything marked in item 90 [V4292-V4308] directly from respondent
+ 98 =Residue
+ 99 =Blank or original entry was 01 (cash), 02 (purse), or 03 (wallet)
+ Coder Instructions:
+ DO NOT INCLUDE CASH/PURSE/WALLET. EXCLUDE PROPERTY NOT BELONGING TO RESPONDENT OR OTHER HOUSEHOLD MEMBER
+ ANSWER ::  99 = Blank or original entry was 01 (cash), 02 (purse), or 03 (wallet)
+ Coder Instructions (96%)
+ V4320_1 - 3RD ATTEMPTED THEFT ITEM ON PERSON
+ Question:
+ Which items did the offender(s) try to take directly from you?
+ 04 =Credit cards, checks, bank cards
+ 05 =Car
+ 06 =Other motor vehicle
+ 07 =Part of motor vehicle, (tire, hubcap, attached tape deck, attached CB radio, etc.)
+ 08 =Gasoline or oil
+ 09 =Bicycle or parts
+ 10 =TV, Stereo, other household appliances
+ 11 =Silver, china, art objects
+ 12 =Other household furnishings (furniture, rugs, etc.)
+ 13 =Personal effect (clothing, jewelry, toys, etc.)
+ 14 =Handgun (pistol, revolver)
+ 15 =Other firearms (rifle, shotgun)
+ 16 =Other
+ 17 =Don't know
+ 40 =Tried to take everything marked in item 90 [V4292-V4308] directly from respondent
+ 98 =Residue
+ 99 =Blank or original entry was 01 (cash), 02 (purse), or 03 (wallet)
+ ANSWER ::  99 = Blank or original entry was 01 (cash), 02 (purse), or 03 (wallet)
+ Coder Instructions (96%)
+ 
+ V4360_1 - OTHER ITEMS ON PERSON
+ Location: 1473-1473 (width: 1; decimal: 0)
+ Variable Type: numeric
+ Question:
+ ASK OR VERIFY - Was there anything (else) the offender(s) took directly from you, for instance, from your pocket or hands, or something
+ that you were wearing?
+ Text:
+ Source code: 768
+ Value Label
+ 1= Yes
+ 2= No
+ 8 =Residue
+ 9 (M)= Out of universe
+ ANSWER ::9=out of universe(96%)

+ V4361_1 - 1ST ITEM TAKEN ON PERSON
+ Question:
+ Which items did the offender(s) take directly from you?
+ First Incident
+ Value Label
+ Property
+ 04= Credit cards, checks, bank cards Vehicle or parts
+ 05 =Car
+ 06 =Other motor vehicle
+ 07 =Part of motor vehicle (tire, hubcap, attached tape deck, attached CB radio, etc.
+ 08 =Unattached motor vehicle accessories or equipment (unattached radio, etc.)
+ 09 =Gasoline or oil
+ 10 =Bicycle or parts
+ Household furnishings
+ 11 =TV, stereo, other household appliances
+ 12 =Silver china, art objects
+ 13 =Other household furnishings (furniture, rugs, etc.)
+ Personal Effects
+ Value Label
+ 14 =Portable electronic and photographic gear (Personal stereo, TV, calculator, camera, etc.)
+ 15 =Clothing, furs, luggage, briefcase
+ 16 =Jewelry, watch, keys
+ 17 =Collection of stamps, coins, etc.
+ 18 =Toys, sports, and recreation equipment, (not listed above)
+ 19 =Other personal and portable items Firearms
+ 20 =Handgun (pistol, revolver)
+ 21 =Other firearm (rifle, shotgun)
+ Miscellaneous
+ 22 =Tools, machines, office equipment
+ 23 =Farm or garden produce, plants, fruits, logs
+ 24 =Animals - pet or livestock
+ 25 =Food or liquor
+ 26 =Other
+ 27 =Don't know
+ 40 =Everything marked in V4326-V4349 was taken directly from respondent
+ 98 =Residue
+ 99 =Blank or original entry was 01 (cash), 02 (purse), or 03 (wallet)
+ ANSWER ::  99 = Blank or original entry was 01 (cash), 02 (purse), or 03 (wallet)
+ Coder Instructions (96%)
+ V4362_1 - 2ND ITEM TAKEN ON PERSON
+ Question:
+ Which items did the offender(s) take directly from you?
+ Second Incident::
+ Property
+ 04= Credit cards, checks, bank cards Vehicle or parts
+ 05= Car
+ 06 =Other motor vehicle
+ 07 =Part of motor vehicle (tire, hubcap, attached tape deck, attached CB radio, etc.
+ 08 =Unattached motor vehicle accessories or equipment (unattached radio, etc.)
+ 09 =Gasoline or oil
+ 10 =Bicycle or parts Household furnishings
+ 11 =TV, stereo, other household appliances
+ 12 =Silver china, art objects
+ 13 =Other household furnishings (furniture, rugs, etc.) Personal effects
+ 14 =Portable electronic and photographic gear (Personal stereo, TV, calculator, camera, etc.)
+ 15 =Clothing, furs, luggage, briefcase
+ 16 =Jewelry, watch, keys
+ 17 =Collection of stamps, coins, etc.
+ 18 =Toys, sports, and recreation equipment, (not listed above)
+ 19 =Other personal and portable items
Firearms
+ 20 =Handgun (pistol, revolver)
+ 21 =Other firearm (rifle, shotgun)
Miscellaneous
+ 22 =Tools, machines, office equipment
+ 23 =Farm or garden produce, plants, fruits, logs
+ 24 =Animals - pet or livestock
+ 25 =Food or liquor
+ 26 =Other
+ 27 =Don't know
+ 40 =Everything marked in V4326-V4349 was taken directly from respondent
+ 98 =Residue
+ 99 =Blank or original entry was 01 (cash), 02 (purse), or 03 (wallet)
+ ANSWER ::  99 = Blank or original entry was 01 (cash), 02 (purse), or 03 (wallet)
+ Coder Instructions (96%)
+ V4363_1 - 3RD ITEM TAKEN ON PERSON
+ Question:
+ Which items did the offender(s) take directly from you?
+ Property
+ 04 =Credit cards, checks, bank cards
+ Vehicle or parts
+ 05 =Car
+ 06 =Other motor vehicle
+ 07 =Part of motor vehicle (tire, hubcap, attached tape deck, attached CB radio, etc.
+ 08 =Unattached motor vehicle accessories or equipment (unattached radio, etc.)
+ 09 =Gasoline or oil
+ 10 =Bicycle or parts
+ Household furnishings
+ 11 =TV, stereo, other household appliances
+ 12 =Silver china, art objects
+ 13 =Other household furnishings (furniture, rugs, etc.)
+ Personal effects
+ 14 =Portable electronic and photographic gear (Personal stereo, TV, calculator, camera, etc.)
+ 15 =Clothing, furs, luggage, briefcase
+ 16 =Jewelry, watch, keys
+ 17 =Collection of stamps, coins, etc.
+ 18 =Toys, sports, and recreation equipment, (not listed above)
+ 19 =Other personal and portable items
+ Firearms
+ 20 =Handgun (pistol, revolver)
+ 21 =Other firearm (rifle, shotgun)
+ Miscellaneous
+ 22 =Tools, machines, office equipment
+ 23 =Farm or garden produce, plants, fruits, logs
+ 24 =Animals - pet or livestock
+ 25 =Food or liquor
+ 26 =Other
+ 27 =Don't know
+ 40 =Everything marked in V4326-V4349 was taken directly from respondent
+ 98 =Residue
+ 99 =Blank or original entry was 01 (cash), 02 (purse), or 03 (wallet).
+ ANSWER ::  99 = Blank or original entry was 01 (cash), 02 (purse), or 03 (wallet)
+ (96%)

+ EconomicImpact_InDirectLoss
+ VS298 - APPROXIMATE TOTAL DOLLAR AMOUNT OF WHAT SOMEONE OBTAINED DURING (THE MOST RECENT/THE) INCIDENT?
+ Question:
+ What is the approximate total dollar value of what someone obtained during (the most recent/the) incident of the misuse or attempted misuse of your personal information? Include the value of goods, services, credit, loans, cash, and anything else the person may have obtained.
+ Value Label
+ 0999998 Residue
+ 9999998 Refused
+ 9999999 Don't know
+ 0999999 (M) Out of Scope
+ Answer:: 94% of people don’t know during (the most recent/the) incident of the misuse or attempted misuse of your personal information (99999999)
+ VS299 - OF THE AMOUNT OBTAINED, HOW MUCH DID YOU PERSONALLY LOSE?
+ Question: Of this ($ Total Loss) that was obtained during (the most recent/the) misuse of your personal information, how much of that money did you personally lose? That is, how much did you lose that was not covered or reimbursed by insurance or a credit card company?
+ Value Label
+ 0999998 Residue
+ 9999998 Refused
+ 9999999 Don't know
+ 0999999 (M) Out of Scope
+ Answer:: 94% of the people don’t know(9999999) during (the most recent/the) misuse of your personal information, how much of that money did you personally lose
+ VS300 - AMOUNT OF ADDITIONAL COSTS INCURRED
+ Question:
+ Other than the costs you already told me about, ($ Personal Loss) how much, IF ANY, additional costs did YOU incur as a result of (the most recent/the) misuse or attempted misuse of your personal information? Include costs for things such as legal fees, bounced check fees, and any miscellaneous expenses, such as postage, phone calls, or notary fees. Do not include lost wages.
+ Value Label
+ 0999998 Residue
+ 9999998 Refused
+ 9999999 Don't know
+ 0999999 (M) Out of Scope
+ Answer:: 94% of the people don’t know(9999999) misuse or attempted misuse of  personal information.
+ VS301 - HOW MUCH COSTS DID YOU INCUR?
+ Question:
+ How much, IF ANY, costs did you incur during (the most recent/the) misuse or attempted misuse of your personal information? Include costs for things such as legal fees, bounced check fees, and any miscellaneous expenses, such as postage, phone calls, or notary fees.Do not include lost wages.
+ Value=== Label
+ 0999998 Residue
+ 9999998 Refused
+ 9999999 Don't know
+ Answer:: 94% of the people don’t know(9999999) costs incur during (the most recent/the) misuse or attempted misuse of personal information
+ VS358 - PRIOR IDENTITY THEFT: COSTS INCURRED
+ Question:
+ How much, IF ANY, costs did you incur from the incident or incidents of identity theft that occurred more than a year ago? Include cost for things such as legal fees, bounced check fees, and any miscellaneous expenses, such as postage, phone calls, or notary fees. Do not include lost wages or loss covered by your credit card company, insurance company, or other organization.
+ Value - Label
+ 01        $0 - $50
+ 02        $51 - $100
+ 03        $101 - $500
+ 04        $501 - $1000
+ 05        $1001 - $4999
+ 06        $5,000 or more
+ 08       Residue
+ 98       Refused
+ 99       Don't know
+ 09       (M) Out of Scope
+ Answer:: 94% of the people out of scope(9) costs did  incur from the incident or incidents of identity theft that occurred more than a year ago

+ 3. Emotional Distress




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
