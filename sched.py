#!/usr/bin/env python3

rival_week = 5
total_weeks = 9

teams_with_rivals = (
    ('B', 'I'),
    ('Dav', 'C'),
    ('DG', 'Dan'),
    ('R', 'L'),
    ('M', 'A'),
)

teams = tuple.__add__(*zip(*teams_with_rivals))

div1,div2 = zip(*teams_with_rivals)



def get_rr_weeks(teams, week_count):
    weeks = []

    # Need teams as a list
    teams = list(teams)

    # Get middle to pivot with
    mid = int(len(teams)/2)

    # Get all the weeks
    for n in range(week_count):

        # Split to two sides
        side1 = teams[:mid]
        side2 = teams[mid:][::-1]

        # Swap sides every other loop
        if n % 2:
            matchups = zip(side1, side2)
        else:
            matchups = zip(side2, side1)

        # print(tuple(matchups))

        # Append to weeks
        weeks.append(tuple(matchups))

        # Rotate team list
        teams.insert(1, teams.pop())

    return weeks

def get_intradiv_weeks(div1, div2, week_counts):
    weeks = []

    # Both divisions should have 5 players
    assert(len(div1) == 5)
    assert(len(div2) == 5)

    division_size = len(div1)

    for inc in range(week_counts):

        this_week = []

        # Division 1
        for n1 in range(division_size):
            n2 = (division_size-n1+inc) % division_size

            # inter division
            if n1 == n2:
                div1_inter = div1[n1]

            # intra division
            elif n1 > n2:
                this_week.append((div1[n1],div1[n2]))

        # Division 2
        for n1 in range(division_size):
            n2 = (division_size-n1+2+inc) % division_size

            # inter division
            if n1 == n2:
                div2_inter = div2[n1]

            # intra division
            elif n1 > n2:
                this_week.append((div2[n1],div2[n2]))

        this_week.append((div1_inter,div2_inter))
        weeks.append(this_week)

    return weeks


def print_stats(schedule, team):
    print("Team: {}".format(team))

    count = {}

    for w in schedule:

        # Find other team
        other_team = None
        for m in w:
            if m[0] == team:
                other_team = m[1]
            elif m[1] == team:
                other_team = m[0]

            if other_team:
                break

        assert(other_team)

        if other_team not in count:
            count[other_team] = 0

        count[other_team] += 1

    for k in sorted(count.keys()):
        print('{} = {}'.format(k, count[k]))

schedule = get_intradiv_weeks(div1, div2, 10)
print_stats(schedule, 'B')
print_stats(schedule, 'D')

# schedule = get_rr_weeks(teams, total_weeks-1)

# Insert rival week
# schedule.insert(rival_week-1,teams_with_rivals)
# print(schedule)
# print_stats(schedule, 'DG')
