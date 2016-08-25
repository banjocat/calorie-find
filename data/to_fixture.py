import csv
import json
import sys

MODEL_NAME = 'calories.food'

def csv_to_json(csv_filename):
    '''
    Takes csv file and creates JSON string
    :param csv_filename: Name of csv file
    :param model_name: Name of app.model of django foramt
    '''
    output = []
    with open(csv_filename) as csv_file:
        data = csv.reader(csv_file, delimiter='^')
        for row in data:
            national_database_pk = row[0].replace('~', '')
            name = row[1].replace('~', '')
            calories = row[3]
            record = {
                    'model': MODEL_NAME,
                    'pk': national_database_pk,
                    'fields': {
                        'name': name,
                        'calories': calories
                        }
                    }
            output.append(record)
    return output


def json_to_file(output):
    '''
    Outputs json to file
    :param output: Json string
    '''
    with open('food_calorie.json', 'w') as calorie_file:
        calorie_file.write(json.dumps(output))


if __name__ == '__main__':
    csv_filename = sys.argv[1]
    calorie_json = csv_to_json(csv_filename)
    json_to_file(calorie_json)

