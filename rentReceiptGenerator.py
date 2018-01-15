from dateutil.parser import *
from dateutil.rrule import *
from datetime import *
from dateutil.relativedelta import *

BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

title = "RENT RECEIPT"
num_text = "Receipt No: "
date_text = "Date: "
#rs_symbol = unicode(u"\u20B9").encode('utf-8')

rent_amount = raw_input("Rent Amount (only numbers)= ")
if not rent_amount:
	rent_amount = "1"
tenant_name = raw_input("Your Name= ")
if not tenant_name:
	tenant_name = "Demo"
tenant_address = raw_input("Your address= ")
if not tenant_address:
	tenant_address = "Some Address"
is_male = raw_input("Is landlord or landlady? Enter 1 for lord, 2 for lady ");
if not is_male:
	is_male = "2";
if (is_male == "2"):
	ll = "Landlady"
else:
	ll = "Landlord"

ll_name = raw_input(ll+" Name ")
if not ll_name:
	ll_name = "LL"
ll_pan = raw_input(ll+" PAN(press enter to leave blank) ")
ll_address = raw_input(ll+" address(press enter to leave blank) ")
while (not start and not end):
	start = raw_input("Start Date(dd/mm/yyyy)= ")
	start_date = parse(start, dayfirst=True)
	
	end = raw_input("End Date(dd/mm/yyyy)= ")
	end_date = parse(end, dayfirst=True)

	if (not start or not end):
		print "\n\nDates are required. Please enter again. \n\n"

months = list(rrule(MONTHLY, dtstart=start_date, until=end_date+relativedelta(months=+1)))
num = 0
test = 'rr.rtf'
out_file = open(test,'w')
for i in range(len(months[:-1])):
	num = i+1;
	month = months[i]
	next_mon = months[num]
	dt = "{:%d, %b %Y}".format(month);
	dt2 = "{:%d, %b %Y}".format(next_mon+relativedelta(days=-1))
	mt = "{:%b %Y}".format(month);
	text = """
						 {}

										{}{}
										{}{}

Received sum of INR {} from {} towards the rent of property located at {} for the period from {} to {}.




{} ({})
""".format(title, num_text, num, date_text, dt, rent_amount, tenant_name, tenant_address, dt, dt2, ll_name, ll)
	out_file.write(text);
	if (ll_pan):
		out_file.write("PAN Number - "+ll_pan);
	if (ll_address):
		out_file.write("Address - "+ll_address);
	out_file.write("\n\n\n\n");

out_file.close()


