Generates schedule for leagues with two divisions

For help:

    $ ./div_sched.py --help

***Note:*** Offsets are used to matchup inter-divisional teams.

# Examples
## 10 teams in a 14 week league

* Week 1: Inter-division with matchup offset 1
* Week 2-6: 4 Intra-division games, 1 inter-division with matchup offset 2
* Week 7: Inter-division with matchup offset 3
* Week 8,9: Inter-division with matchup offset 0 ("rivals")
* Week 10-14: 4 Inter-division games, 1 inter-division with matchup offset 4

Schedule distribution:

* 2x games against teams in your division
* 2x games against one team in the other division (inter-divisional rival)
* 1x game against the other 4 teams in the other division

Command:

    $ ./div_sched.py --div1 Bel David DG Ro Migs --div2 Irv Clint Dan Lauren AG --inter 1 --intra 2 --inter 3 0 0 --intra 4 --distribution

## 12 teams in a 16 week league
This is a league with an even number of division teams so no need for an offset for intra-divisional weeks.

* Week 1-5: Intra-division games
* Week 6-11: Inter-division games with matchup offsets 0 through 5 (all teams in the other division)
* Week 12-16: Intra-division games

Schedule distribution:

* 2x games against teams in your division
* 1x game against teams in the other division
 
Command:

    $ ./div_sched.py --div1 Tito Frank Igor Dan Saber Gamal --div2 DG Mo AG Bel John Peter --intra --inter 0 1 2 3 4 5 --intra  --distribution

# Requirements
Python 3+

# Notes
* Since I'm focusing on fantasy sports use case, not distinguishing between home and away games.
