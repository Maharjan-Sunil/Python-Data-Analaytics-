import datetime

# string_format_date = "2020-08-02"
# datetime_obj = datetime.strptime(string_format_date,'%d%m%y')
# # print(datetime.datetime.now())
# print(datetime_obj)

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B %d %Y"))
