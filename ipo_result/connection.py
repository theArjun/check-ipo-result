import csv
import json
import logging
import sys
from collections import OrderedDict

import requests
from prettytable import PrettyTable
from yaspin import yaspin

from .constants import (
    BOID_FILE_PATH,
    COMPANIES_LIST_PATH,
    RESULT_CHECK_URL,
    SCRIP_LIST,
)


logging.basicConfig(
    level=logging.DEBUG,
    filename='requests.log',
    filemode='a',  # Append
    format='%(name)s - %(levelname)s - %(message)s')


class IPOResult:

    def __init__(self,
                 fast_mode=False,
                 check_all=False,
                 latest=False,
                 *args,
                 **kwargs):
        self.fast_mode = fast_mode
        self.latest = latest
        if not fast_mode:
            self.check_all = check_all

    def get_companies_list(self, write_to_file=True):
        if self.fast_mode:
            with open(COMPANIES_LIST_PATH, 'r') as fp:
                companies_list = json.load(fp)  # Reading from file
        else:
            with yaspin(color='green') as sp:
                response = requests.get(SCRIP_LIST).json()
                _list = response.get('body')
                companies_list = OrderedDict()
                for index, data in enumerate(_list):
                    _id = data.get('id')
                    companies_list[str(index + 1)] = {
                        'name': data.get('name'),
                        'scrip': data.get('scrip'),
                        'value': _id
                    }
                if write_to_file:
                    with open('companies.json', 'w') as fp:
                        fp.write(json.dumps(companies_list, indent=4))
                sp.ok('Companies fetched.')
        return companies_list

    def check_individual_result(
        self,
        company_key,
        boid_key,
    ):

        payload = json.dumps({
            'companyShareId': str(company_key),
            'boid': str(boid_key)
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.request('POST',
                                    RESULT_CHECK_URL,
                                    headers=headers,
                                    data=payload)
        response_json = response.json()
        logging.debug('Response: {}'.format(response_json))
        return response_json.get('success'), response_json.get('message')

    def check_result(self):
        companies_list = self.get_companies_list()
        if not self.latest:
            for c_value, c_name in companies_list.items():
                print(f'{c_value}. {c_name["name"]}')

            company_index = input('\nEnter company index: ').strip()
            chosen_company = companies_list.get(company_index)
            if chosen_company is None:
                print('Invalid input. exiting...')
                sys.exit()
        else:
            # Last item of dictionary
            chosen_company = next(reversed(companies_list.values()))

        company_key = chosen_company['value']
        company_name = chosen_company['name']

        print(f'\nSelected company: {company_name}\n')

        table = PrettyTable(['Name', 'Boid', 'Result', 'Remarks'])

        file = open(BOID_FILE_PATH, 'r')
        csv_file = csv.reader(file)
        # Exclude header
        next(csv_file)
        for row in csv_file:
            boid_key = row[1].strip()
            name = row[0]
            result, message = self.check_individual_result(
                company_key,
                boid_key,
            )
            result_message = 'Alloted' if result else 'Not Alloted'
            table.add_row([name, boid_key, result_message, message])

        print(table)

    def check_all_results(self):
        companies_list = self.get_companies_list()
        table = PrettyTable(['Name', 'Boid', 'Alloted Companies'])

        file = open(BOID_FILE_PATH, 'r')
        csv_file = csv.reader(file)
        # Exclude header
        next(csv_file)

        with yaspin(color='green') as sp:
            for row in csv_file:
                boid_key = row[1].strip()
                name = row[0]
                user_results = []
                for index, company in companies_list.items():
                    result, message = self.check_individual_result(
                        company['value'],
                        boid_key,
                    )
                    if result:
                        # Assuming only integer in string is alloted quantity.
                        numbers = [
                            int(word) for word in message.split()
                            if word.isdigit()
                        ]
                        alloted_quantity = numbers[0] if len(
                            numbers) > 0 else 0
                        user_results.append(
                            f"{company['scrip']} ({alloted_quantity})")
                sp.write(f'{name} searching complete.')
                if user_results:
                    alloted_list = ', '.join(user_results)
                else:
                    alloted_list = 'None'

                table.add_row([name, boid_key, alloted_list])
            sp.ok("✔")

            print(table)
