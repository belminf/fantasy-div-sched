Generates schedule for leagues with two divisions

For help:

    $ ./div_sched.py --help

'''Note:''' Offsets are used to matchup inter-divisional teams.

# Example
Example for a 10 team and 14 week league, that would result in a schedule where you play your division mates 2x each, the other division teams 1x each, and one inter-divisional rival an extra time:

* Week 1: Inter-division with matchup offset 1
* Week 2-6: 4 Intra-division games, 1 inter-division with matchup offset 2
* Week 7: Inter-division with matchup offset 3
* Week 8,9: Inter-division with matchup offset 0 ("rivals")
* Week 10-14: 4 Inter-division games, 1 inter-division with matchup offset 4

The command will look like:

    $ ./div_sched.py --div1 Bel David DG Ro Migs --div2 Irv Clint Dan Lauren AG --inter 1 --intra 2 --inter 3 0 0 --intra 4 --distribution

# Requirements
Python 3+

# Notes
* Only tested it with odd numbered (5, 7, etc.) divisions
