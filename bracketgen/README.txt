Bracket generator for sports tournaments.

Things
- Teams (and ranks)
- Away/Home (from georgia or not from georgia)
- Times
- Courts / Distances between courts
- Pools

All-or-nothing constraints:
- No team can play more than one game in a timeslot
- Teams can't play three games back to back*
- Teams can't play back to back games in different venues*

Preferred constraints:
- Away teams don't have to ref the last match of the last day
- Teams with morning games the following day don't have to ref the last match
- Back to back games are in the same building (minimize distance)
  - Minimizing area overall would be great in general... having localized matches is good.
  - Weight increases exponentially with sum of distances.
- Teams don't play teams from their same club on the first day
- *Preferably* crossover matches aren't third in a row games, but this is preferred over waiting to play
