"""
While the Chicago Cubs were ecstatic with their 2016 World Series championship, they were eliminated from the playoffs in 2017. Looking ahead to 2018 they are beginning to embrace the more data-driven analysis of player’s values known as Sabermetrics.

For example, a player’s batting average is calculated by dividing the total number of base hits by the total number of official at-bats. One limitation of using the batting average to evaluate players is that it treats all hits equally, rather than taking into account doubles, triples or home runs. For this reason, analysts often prefer to consider what is known as the slugging percentage, which distinguishes between different hit outcomes. To calculate the slugging percentage, the total number of bases of all hits is divided by the total numbers of time at bat, that did not result in walks, or at-bats.
More specifically, an at-bat can earn , , , or

bases (these are referred to as official at-bats). Furthermore, some at-bats, such as those that result in a base-on-balls (i.e., a “walk”) are not considered in either the player’s batting average or slugging percentage.

For example, if a player hits a triple (
 bases), strikes out ( bases), and hits a double ( bases), their slugging percentage would be
. If a player hits a single ( base), walks, and hits a home run ( bases), the slugging level would be
. Notice that in this case, the denominator is two, not three, because the walk does not count towards the slugging percentage.
Input

The input is composed of two lines. The first line contains a single positive integer
() that specifies the number of at-bats. The second line contains integers, separated by spaces, each describing one of those at-bats. Strike-outs, singles, doubles, triples, and home runs are represented as 0, 1, 2, 3, 4, respectively. Walks are represented as -1. You may assume that there will always be at least one official at-bat (i.e., at least one at-bat will not be a walk).
Output

Display the player’s slugging percentage as a real number, accurate to within an absolute or relative error of
. We recommend that you do not round the value that you calculate
"""
def calculate_slugging_percentage(n, at_bats):
    total_bases = 0
    official_at_bats = 0
    
    for outcome in at_bats:
        if outcome == -1:
            continue  # Skip walks
        total_bases += outcome
        official_at_bats += 1
    
    slugging_percentage = total_bases / official_at_bats
    return slugging_percentage

n = int(input().strip())
at_bats = list(map(int, input().strip().split()))

result = calculate_slugging_percentage(n, at_bats)
print(result)

