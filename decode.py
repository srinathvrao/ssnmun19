
import urllib.parse

file1 = open("questions.data","r+")
#file2 = open("que.txt",w+)
url = file1.read()
# url = """Do%20you%20think%20the%20feminist%20movement%20is%20going%20in%20the%20right%20direction%3F%20Where%20do%20you%20see%20women%20in%20the%20next%2020%20years%2C%20going%20by%20the%20current%20trends.%20Is%20it%20true%20that%20infertility%20is%20inevitable%20for%20women%20in%20powerful%20positions%20due%20to%20stress%3F
# Body%20and%20Mind"""
newstr=urllib.parse.unquote(url)

with open("que.doc", "wb") as myfile:
    myfile.write(newstr.encode("utf-8"))

#print(newstr)