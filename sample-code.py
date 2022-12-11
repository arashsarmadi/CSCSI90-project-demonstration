filename = "C:\Data-Science\CS90\Project\input.csv"

file = open(filename, 'r')

for line in file:
    print(line)

#Unnecessary iteration (code quality)
data = set(["A", "B", "C", "D", "E"])
for ii in data:
    if ii == "D":
        print("found items")

def find_string_noncompliant():
    data = set(["sampleString1", "sampleString2", "sampleString3"])
    # Noncompliant: a loop is used to access a single item.
    for i in data:
        if i == "sampleString1":
            print("found item")

#Improper error handiling (security)
def division(a,b):
    try:
        return int(a)/int(b)
    except Exception:
        pass

#Insecure temporary file (security)
import tempfile
with open(tempfile.mktemp(), "w+") as f:
    f.write('Hello')

#AWS client not reused in a Lambda function (security)
import boto3
def lambda_handler(event, context):

    client = boto3.client('s3')
    return client.list_buckets()


#Hardcoded credentials (security)
my_key = 'thiskeyisnotreal'
boto3.session.Session(aws_secret_access_key=my_key)


#Complex code hart to maintain (Code Quality)
my_list = [i for i in [j for j in range(100) if j%2 == 0] if i%4 == 0]