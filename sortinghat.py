from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import pdist, squareform
import numpy as np
from itertools import combinations
import pandas as pd

# Specify the file, refer to the one in the folder as an example. All that matters is that the names are the first column
# and all info to sort with is in the subsequent columns
file_path = 'Prior Experience Survey Survey Student Analysis Report.csv'
groups = 3
data = pd.read_csv(file_path)

# Function to calculate the diversity based on skillset
def calculate_skillset_diversity(data):
    skill_data = data.iloc[:, 2:]  # Extracting the skill-related columns
    diversity_matrix = pairwise_distances(skill_data, metric='hamming')
    return diversity_matrix


def assign_to_teams_all_inclusive(data, diversity_matrix, team_size, groups):
    n = len(data)
    teams = {i: [] for i in range(groups)}

    # List of all indices
    all_indices = list(range(n))

    # Sort indices by their potential contribution to diversity (sum of distances to all other points)
    diversity_contributions = [sum(diversity_matrix[i]) for i in all_indices]
    sorted_indices = sorted(all_indices, key=lambda i: diversity_contributions[i], reverse=True)

    # Assign each individual to a team in a round-robin fashion until all are assigned
    for idx, i in enumerate(sorted_indices):
        team_number = idx % groups
        teams[team_number].append(i)

    # Convert indices to actual data
    assigned_teams_all_inclusive = {k: data.iloc[v] for k, v in teams.items()}
    return assigned_teams_all_inclusive

# Calculate skillset diversity
diversity_matrix = calculate_skillset_diversity(data)

# Calculating team size
total_individuals = len(data)
team_size = total_individuals // 3

# Reassign to teams with the new logic
assigned_teams_evenly = assign_to_teams_all_inclusive(data, diversity_matrix, team_size, groups)

# Output the teams
for team, members in assigned_teams_evenly.items():
    print(f"Team {team + 1}:")
    print(members)
    print()

# Combine all teams into one DataFrame with an additional column for team assignment
team1_df = assigned_teams_evenly[0].assign(Team='Team 1')
team2_df = assigned_teams_evenly[1].assign(Team='Team 2')
team3_df = assigned_teams_evenly[2].assign(Team='Team 3')

combined_teams_df = pd.concat([team1_df, team2_df, team3_df])

# Define file path for the CSV
csv_file_path = 'Assigned_Teams.csv'

# Save to CSV
combined_teams_df.to_csv(csv_file_path, index=False)

csv_file_path
