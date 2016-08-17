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



def get_inter_sched(div1, div2, div_offsets):

    # Assert divisions are the same size
    assert(len(div1) == len(div2))

    # Create a list of lists to gather weeks of matchups
    weeks = [[] for i in range(len(div_offsets))]

    # Save division size
    div_size = len(div1)

    # Loop offsets, each is for a week
    for week_num in range(len(div_offsets)):
        offset = div_offsets[week_num]

        # Loop through teams and add matchups
        for i in range(div_size):

            # Get division indexes
            n1 = i
            n2 = (i+offset) % div_size

            # Append to week schedule
            weeks[week_num].append((div1[n1],div2[n2]))

    return weeks

def get_odd_intra_sched(div1, div2, week_count, div_offset=1):

    # Assert divisions are the same size
    assert(len(div1) == len(div2))

    # Create a list of lists to gather weeks of matchups
    weeks = [[] for i in range(week_count)]

    # Save division size
    div_size = len(div1)

    for week_num in range(week_count):

        # Loop through both divisions
        for i in range(div_size):

            # Division indexes
            n1 = (week_num-i) % div_size
            n2 = ((week_num-i)+ div_offset) % div_size

            # Div1: Inter
            if n1 == i:
                div1_inter = div1[n1]

            # Div1: Intra
            elif n1 < i:
                weeks[week_num].append((div1[i],div1[n1]))

            # Div2: Inter
            if n2 == i:
                div2_inter = div2[n2]

            # Div2: Intra
            elif n2 < i:
                weeks[week_num].append((div2[i],div2[n2]))

        # Add the interdivisional game
        weeks[week_num].append((div1_inter,div2_inter))

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

schedule = get_inter_sched(div1, div2, (1,2,1))
print schedule
print_stats(schedule, 'B')
# print_stats(schedule, 'D')

# schedule = get_rr_weeks(teams, total_weeks-1)

# Insert rival week
# schedule.insert(rival_week-1,teams_with_rivals)
# print(schedule)
# print_stats(schedule, 'DG')
