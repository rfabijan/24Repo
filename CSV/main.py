import csv

def transform_user_detail(csv_file_name):
    new_user_data = []

    with open(csv_file_name) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')

        for user in reader:
            transformations = []
            transformations.append(user[1])
            transformations.append(user[2])
            transformations.append(user[-2])
            new_user_data.append(transformations)

    return new_user_data


def writeToCSV(old_user_data = 'user_details.csv', transformed_user_data = 'new_user_data.csv'):
    new_user_data = transform_user_detail(old_user_data)

    with open(transformed_user_data, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(new_user_data )


writeToCSV()
# transform_user_detail('user_details.csv')
# with open('user_details.csv') as file:
#     reader = csv.reader(file)
#
#     for row in reader:
#         print(row)

