import argparse

from ipo_result import IPOResult


parser = argparse.ArgumentParser(description='IPO Result Checker')
# Store true or false
# https://stackoverflow.com/a/8259080/9755816
parser.add_argument('-f', '--fast', help='Fast Mode', action='store_true')
parser.add_argument('-a', '--all', help='Check All', action='store_true')
parser.add_argument('-l',
                    '--latest',
                    help='Fetch Latest Result',
                    action='store_true')

args = parser.parse_args()
connection = IPOResult(
    fast_mode=args.fast,
    check_all=args.all,
    latest=args.latest,
)
if args.all:
    connection.check_all_results()
else:
    connection.check_result()
