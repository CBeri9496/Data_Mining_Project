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
  
     NAGESH REDDY THUM          Data Analysis                  Data Analysis
   
     SHIREESHA BEKKARI          Backend	                       Working on WEKA
     
     RAVI TEJA KOLLIPARA        Testing	                       Debugging
   
     SRICHAND ALAPATI	        Frontend                       Coding



# Deliverable and Checkpoints


     Checkpoint date               Expected Deliverable                Responsible team members(s)               Checkpoint results

     15/02/2016                    Update Project Report               CHANDANA BERI, NAGESH THUM                Collected more data
                                   on Data, team, Project                                                        and add Research
                                   Managemen and formulate                                                       questions. 
                                   questions.
                                   
     15/03/2016                    Add Research Questions              CHANDANA BERI                             Added more DATA and                                                                                                              Reasearch questions
     
     11/04/2016                    Update Project Code and Data        NAGESH REDDY THUM, SRICHAND ALAPATI       Initial code/analysis                                   Analysis                                                                  checked in to GITHUB                                                                                                             and Collected Data                                                                                                               for Reasearch                                                                                                                    Questions.
     
     18/04/2016                    Execute Program and get output      SHIREESHA BEKKARI, SRICHAND ALAPATI,      Testing and Get Project
                                   and Debugging                       RAVI TEJA KOLLIPARA                       Output
                                   
     25/04/2016                    Prepare full project report         CHANDANA BERI                             Full Project report
                                                                                                                 completed

