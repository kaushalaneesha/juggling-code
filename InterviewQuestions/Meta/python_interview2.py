# Python questions from this interview: https://leetcode.com/discuss/interview-question/2071096/Meta-or-Dublin-or-Data-Engineer-(Reject)
import csv
import random
import time

# read file contents and print 3 column from file
def read_csv(file, column_count = 3):
    columns = [[] for i in range(3)]
    with open("/Users/anek/Documents/Interview Questions/Pratice/InterviewQuestions/Meta/test.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            for i in range(3): # Get the first 3 columns
                columns[i].append(row[i])
    return columns

print(read_csv("test.csv"))

# simulate real time feed
def real_time_feed_simulator(data_source):
    while True:
        data = random.choice(data_source)
        yield data
        time.sleep(1)

data_source = ["data1", "data2", "data3"]
for data in real_time_feed_simulator(data_source):
    print(data)

