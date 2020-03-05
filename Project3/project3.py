import re
import datetime
import os
from collections import Counter
import datetime

# Checking if file is on disk
FILE_NAME = "/Users/jeromeporter/Desktop/Spring 2020/TCMG_412/project3.log"
if os.path.exists(FILE_NAME):
    print('File found: Parsing has begun\n')
    #Open file from local disk
    fh = open(FILE_NAME)    
else:
    print('File not found... Downloading now....')
    url_path = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    local_file, headers = urlretrieve(url_path, local_file) 
    #Open file from local disk
    fh = open(url_path)    

# Variables
Errors = []
jan = []
feb = []
mar = []
apr = []
may = []
jun = []
jul = []
aug = []
sep = []
oct94 = []
oct95 = []
nov94 = []
dec94 = []
line_cnt = 0
Redirect = []
things = []
bad_lines = 0
months = ['October', 'November', 'December', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September']


# REGEX Expressions
regex = re.compile(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*")
regex_error = re.compile('[4][\d]{2}')
regex_redir = re.compile('[3][\d]{2}')

jan_file = open('January.txt', 'w')
feb_file = open('February.txt', 'w')
mar_file = open('March.txt', 'w')
apr_file = open('April.txt', 'w')
may_file = open('May.txt', 'w')
jun_file = open('June.txt', 'w')
jul_file = open('July.txt', 'w')
aug_file = open('August.txt', 'w')
sep_file = open('September.txt', 'w')
oct_file = open('October.txt', 'w')
nov_file = open('November.txt', 'w')
dec_file = open('December', 'w')

request = []
# DATE SEARCH and Store in 'Date'
Dates = []
FILENAME = []
for line in fh:
    #Line counter
    line_cnt += 1
    request.append(line)
    split = re.split(regex, line)
    if len(split) >= 8:
        #Date 
        date = (split[1])
        Dates.append(date)
        #Filename
        fn = (split[4])
        things.append(fn)
        error_code = (split[6])
        if '3' in error_code[0]:
        #er = re.search(regex_error, error_code)
            Errors.append(error_code)
        elif '4' in error_code[0]:
            Redirect.append(error_code)
    else:
        bad_lines += 1
        
#Calculate error percentage
error_percentage = ((len(Errors) / line_cnt)) * 100
er_per = round(error_percentage, 2)

# Calculate redirect percentage
redirect_percentage = (len(Redirect) / line_cnt) * 100
re_per = round(redirect_percentage, 2)

#Convert dates to datetime
dates_list = [datetime.datetime.strptime(date, '%d/%b/%Y').date() for date in Dates]

# Find Max and Min files requested
fn_cnt = Counter(things)
max_file = max(zip(fn_cnt.values(), fn_cnt.keys()))
maximum = max(fn_cnt.values())
min_file = min(zip(fn_cnt.values(), fn_cnt.keys()))

# Printing information
print(f'Total lines: {line_cnt}\n')
#print(f'Errors: {len(Errors)}\n')
#print(f'Dates: {len(Dates)}\n')
#print(f'Redirects: {len(Redirect)}\n')
print(f'Bad Lines: {bad_lines}\n')
print(f'Most requested file: {max_file}')
print(f'Least requested file: {min_file}\n')
print(f'{er_per}% of requests were not successful\n')
print(f'{re_per}% of requests were redirected\n')


for x in Dates:
    if 'Jan' in x:
        jan.append(x)
    elif 'Feb' in x:
        feb.append(x)
    elif 'Mar' in x:
        mar.append(x)
    elif 'Apr' in x:
        apr.append(x)
    elif 'May' in x:
        may.append(x)
    elif 'Jun' in x:
        jun.append(x)
    elif 'Jul' in x:
        jul.append(x)
    elif 'Aug' in x:
        aug.append(x)
    elif 'Sep' in x:
        sep.append(x)
    elif 'Oct'  in x:
        oct94.append(x)
    elif 'Nov' in x:
        nov94.append(x)
    elif 'Dec' in x:
        dec94.append(x)
    
    
    
# Lengths of list for each month
jan1 = len(jan)
feb1 = len(feb)
mar1 = len(mar)
apr1 = len(apr)
may1 = len(may)
jun1 = len(jul)
jul1 =len(jul)
aug1 = len(aug)
sep1 = len(sep)
oct1 = len(oct94)
#oct2 = len(oct95)
nov1 = len(nov94)
dec1 = len(dec94)

#Request averages per day and week
week_avg = (line_cnt) / 52
week_avg_rnd = int(week_avg)
day_avg = (line_cnt) / 365
day_avg_rnd = int(day_avg)

#print(f'There were {oct1} requests in the month of {months[0]}')
print(f'There were {nov1} requests in the month of {months[1]}, 1994')
print(f'There were {dec1} requests in the month of {months[2]}, 1994')
print(f'There were {jan1} requests in the month of {months[3]}')
print(f'There were {feb1} requests in the month of {months[4]}')
print(f'There were {mar1} requests in the month of {months[5]}')
print(f'There were {apr1} requests in the month of {months[6]}')
print(f'There were {may1} requests in the month of {months[7]}')
print(f'There were {jun1} requests in the month of {months[-4]}')
print(f'There were {jul1} requests in the month of {months[-3]}')
print(f'There were {aug1} requests in the month of {months[-2]}')
print(f'There were {sep1} requests in the month of {months[-1]}')
print(f'There were {oct1} requests in the month of {months[0]}')
print(f'There were {nov1} requests in the month of {months[1]}')
print(f'There were {dec1} requests in the month of {months[2]}\n')

print(f'The average number of requests per week is: {week_avg_rnd}')
print(f'The average number of requests per day is: {day_avg_rnd}')





# Writing files to disk

#for x in request:
 #   if 'Jan' in x:
  #      jan_file.write(f'{x}\n')
 #   elif 'Feb' in x:
  #      feb_file.write(f'{x}\n')
 #   elif 'Mar' in x:
 #       mar_file.write(f'{x}\n')
 #   elif 'Apr' in x:
 #       apr_file.write(f'{x}\n')
 #   elif 'May' in x:
   #     may_file.write(f'{x}\n')
  #  elif 'Jun' in x:
   #     jun_file.write(f'{x}\n')
  #  elif 'Jul' in x:
  #      jul_file.write(f'{x}\n')
 #   elif 'Aug' in x:
 #       aug_file.write(f'{x}\n')
 #   elif 'Sep' in x:
#        sep_file.write(f'{x}\n')
#    elif 'Oct'  in x:
  #      oct_file.write(f'{x}\n')
  #  elif 'Nov' in x:
 #       nov_file.write(f'{x}\n')
 #   elif 'Dec' in x:
 #       dec_file.write(f'{x}\n')
#    else:
#