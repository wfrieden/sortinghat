# sortinghat
Sort a population into groups to maximize diversity of skills

CSV file structure:
Column 1 - Names, Columns 2+ - Skills/Info to Diversify

Specify the number of groups

How the code works: 

1. Hamming Distance for Skillset Diversity
The Hamming distance is a measure used to compare two strings of equal length and counts the number of positions at which the corresponding elements (or characters) are different. In this context, it's used to compare the skillsets of individuals.

Each skill is treated as a binary variable (True/False or 1/0).
For two individuals, the Hamming distance is the count of skills where one has the skill (1) and the other does not (0), divided by the total number of skills.
This measure is calculated between every pair of individuals, resulting in a diversity matrix. A higher value indicates greater diversity between two individuals.

2. Diversity Contribution
For each individual, their diversity contribution is calculated as the sum of Hamming distances between them and all other individuals. This value represents how much diversity an individual brings to the group.

3. Round-Robin Assignment
Individuals are sorted in descending order of their diversity contributions (those bringing the most diversity are sorted first). They are then assigned to teams in a round-robin fashion:

The first individual in the sorted list is assigned to Team 1, the second to Team 2, the third to Team 3, and then back to Team 1, and so on.
This method ensures a balanced distribution of team members based on their diversity contributions.
This process continues until all individuals are assigned to a team.
