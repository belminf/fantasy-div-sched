#!/usr/bin/env python3
import argparse

def main():
    args = parse_cmd()

    # Testing teams
    teams_with_rivals = (
        ('B', 'I'),
        ('Dav', 'C'),
        ('DG', 'Dan'),
        ('R', 'L'),
        ('M', 'A'),
    )
    div1,div2 = zip(*teams_with_rivals)
    from pprint import pprint
    pprint(div1)
    pprint(div2)

    # Schedule
    schedule = []

    # Week 1
    schedule.extend(get_inter_sched(div1, div2, (1,)))

    # Weeks 2,3,4,5,6
    schedule.extend(get_odd_intra_sched(div1, div2, 5, 2))

    # Weeks 7,8,9
    schedule.extend(get_inter_sched(div1, div2, (3,0,0)))

    # Weeks 10,11,12,13,14
    schedule.extend(get_odd_intra_sched(div1, div2, 5, 4))

    # Check distribution
    print_sched_distro(schedule, 'B')
    print_sched_distro(schedule, 'Dan')


def parse_cmd():
    parser = argparse.ArgumentParser(description='Generates schedule for a league with divisional play')

    parser.add_argument(
        '--div1',
        nargs='+',
        metavar='TEAM',
        type=argparse.FileType('r'),
        help='Teams for first division',
    )

    parser.add_argument(
        '--div2',
        nargs='+',
        metavar='TEAM',
        type=argparse.FileType('r'),
        help='Teams for second division',
    )

    parser.add_argument(
        '--inter',
        type=int,
        nargs='+',
        metavar='OFFSET',
        help='Inter-divisional weeks, week count determined by number of offsets, offsets used for pairing up teams from both divisions',
    )

    parser.add_argument(
        '--intra',
        type=int,
        nargs='?',
        default=1,
        metavar='OFFSET',
        help='Intra-divisional weeks, week count determined by number of teams in a division, if divisons are odd sized offset will be used for an interdivisional matchup pairing to even out the week',
    )

    return parser.parse_args()


def get_inter_sched(div1, div2, div_offsets):

    # Assert divisions are the same size
    assert(len(div1) == len(div2))

    # Save division size
    div_size = len(div1)

    # Create a list of lists to gather weeks of matchups
    weeks = [[] for i in range(len(div_offsets))]

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


def get_odd_intra_sched(div1, div2, div_offset=1):

    # Assert divisions are the same size
    assert(len(div1) == len(div2))

    # Save division size
    div_size = len(div1)

    # Create a list of lists to gather weeks of matchups
    weeks = [[] for i in range(div_size)]

    for week_num in range(week_count):

        # Loop through both divisions
        for x1 in range(div_size):

            # Division indexes
            y1 = (week_num-x1) % div_size
            x2 = (x1+div_offset) % div_size
            y2 = (week_num-x1+div_offset) % div_size

            # Intradivision
            if x1 == y1:
                weeks[week_num].append((div1[x1],div2[x2]))

            # Interdivision
            else:

                # Div1
                if x1 > y1:
                    weeks[week_num].append((div1[x1],div1[y1]))

                # Div2
                if x2 > y2:
                    weeks[week_num].append((div2[x2],div2[y2]))

    return weeks


def print_sched_distro(schedule, team):
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

if __name__ == '__main__':
    main()
