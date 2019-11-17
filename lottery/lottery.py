import random
import xlrd


def lottery_prediction(past_wins, my_tickets):
    win_data = len(past_wins)
    win_tickets = []
    prizes = {'1st Prize': 0, '2nd Prize': 0, '3rd Prize': 0, '4th Prize': 0, '5th Prize': 0, '6th Prize': 0,
              '7th Prize': 0}

    prize_dict = {6: '1st Prize', 60: '2nd Prize', 5: '3rd Prize', 50: '4th Prize', 4: '5th Prize', 40: '6th Prize',
                  3: '7th Prize'}

    while win_data > 0:
        win_data -= 1
        for ticket in my_tickets:
            win_nums = []
            p = 0
            for number in ticket:
                if number in past_wins[win_data][:6]:
                    win_nums.append(number)
            if len(win_nums) == 6:
                p = len(win_nums)
            elif len(win_nums) > 2:
                if past_wins[win_data][-1] in ticket:
                    p = (len(win_nums) + 1) * 10
                else:
                    p = len(win_nums)

            if p > 2:
                win_tickets.append(win_nums)
                print("win_nums {}, my_ticket {}, past_Win_ticket {}".format(win_nums, ticket, past_wins[win_data]))

            if p in prize_dict.keys():
                prizes[prize_dict[p]] += 1

    return prizes


"""
my_tickets = [[14, 45, 28, 40, 13, 26],
              [14, 45, 28, 40, 13, 30],
              [43, 35, 40, 17, 37, 19],
              [43, 35, 40, 66, 77, 88]]
past_wins = []
for i in range(10):
    past_wins.append(random.sample(range(1, 50), 7))

print(past_wins)


past_wins = [[14, 45, 28, 40, 13, 30, 26],
             [27, 11, 10, 19, 33, 17, 1],
             [43, 35, 40, 17, 37, 16, 19]]

"""

workbook = xlrd.open_workbook("past_wins.xls")
past_wins_sheet = workbook.sheet_by_index(0)
past_wins_count = past_wins_sheet.nrows
my_tickets_sheet = workbook.sheet_by_index(1)
my_tickets_count = my_tickets_sheet.nrows

past_wins = []

for i in range(1, past_wins_count):
    temp = past_wins_sheet.row_values(i)
    past_wins.append([int(x) for x in temp])

my_tickets = []

for i in range(1, my_tickets_count):
    temp = my_tickets_sheet.row_values(i)
    my_tickets.append([int(x) for x in temp])


prize = lottery_prediction(past_wins, my_tickets)
print(prize)
print(my_tickets)