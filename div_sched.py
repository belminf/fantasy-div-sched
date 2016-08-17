#!/usr/bin/env python3
import argparse

def main():

    # Get arguments
    args = parse_cmd()

    # Set both divisions
    div1 = args.div1
    div2 = args.div2

    # Make sure they are equal size
    if len(div1) != len(div2):
        raise ValueError('Divisions are not the same length')

    # Create schedules
    schedule = []
    for f,a in args.scheduling_funcs:
        schedule.extend(f(div1, div2, a))

    # Print schedules
    for week_num, week_matchups in enumerate(schedule):

        # Make week 1-based
        week_num += 1
        print('WEEK {}'.format(week_num))

        # Print matchups
        for match in week_matchups:
            print('- {} v. {}'.format(*match))

        # Empty line
        print()


    # Print distribution if asked
    if args.distribution:
        print_distribution(schedule, div1, div2)


class SchedulingAction(argparse.Action):

    def __init__(self, option_strings, dest, scheduling_func=None, **kwargs):

        # Require the scheduling function
        if scheduling_func is None:
            raise ValueError('Need scheduling_func')
        self.scheduling_func = scheduling_func

        super(SchedulingAction, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):

        # Add and load scheduling_funcs attribute
        if  'scheduling_funcs' not in namespace:
            setattr(namespace, 'scheduling_funcs', [])
        scheduling_funcs = namespace.scheduling_funcs

        # Check for default
        if not values:
            values = self.default

        # Append this function to the list
        scheduling_funcs.append((self.scheduling_func, values))
        setattr(namespace, 'scheduling_funcs', scheduling_funcs)

def parse_cmd():
    parser = argparse.ArgumentParser(description='Generates schedule for a league with divisional play')

    parser.add_argument(
        '--div1',
        nargs='+',
        metavar='TEAM',
        help='Teams for first division',
    )

    parser.add_argument(
        '--div2',
        nargs='+',
        metavar='TEAM',
        help='Teams for second division',
    )

    parser.add_argument(
        '--inter',
        type=int,
        nargs='+',
        metavar='OFFSET',
        help='Inter-divisional weeks, week count determined by number of offsets, offsets used for pairing up teams from both divisions',
        scheduling_func=get_inter_sched,
        action=SchedulingAction
    )

    parser.add_argument(
        '--intra',
        type=int,
        nargs='?',
        default=1,
        metavar='OFFSET',
        help='Intra-divisional weeks, week count determined by number of teams in a division, if divisons are odd sized offset will be used for an interdivisional matchup pairing to even out the week',
        scheduling_func=get_intra_sched,
        action=SchedulingAction
    )

    parser.add_argument(
        '--distribution',
        action='store_true',
        help='Print scheduling distribution for each team',
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


def get_intra_sched(div1, div2, div_offset=1):

    # Assert divisions are the same size
    assert(len(div1) == len(div2))

    # Save division size
    div_size = len(div1)

    # Create a list of lists to gather weeks of matchups
    weeks = [[] for i in range(div_size)]

    for week_num in range(div_size):

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


def print_distribution(schedule, div1, div2):

    # Initiate distro count dict
    sched_distro = {}
    for team in div1+div2:
        sched_distro[team] = {t:0 for t in div1+div2 if t != team}


    # Loop through the weeks in the schedule
    for w in schedule:

        # Go to each matchup and inc counters
        for m in w:
            sched_distro[m[1]][m[0]] += 1
            sched_distro[m[0]][m[1]] += 1

    # Print results for div1
    for team in sorted(div1):
        print('DIV1: {}'.format(team))

        # Loop through counts
        for other_team in sorted(sched_distro[team].keys()):
            print('- {}: {}'.format(other_team, sched_distro[team][other_team]))

        print()

    # Print results for div2
    for team in sorted(div2):
        print('DIV2: {}'.format(team))

        # Loop through counts
        for other_team in sorted(sched_distro[team].keys()):
            print('- {}: {}'.format(other_team, sched_distro[team][other_team]))

        print()

if __name__ == '__main__':
    main()
