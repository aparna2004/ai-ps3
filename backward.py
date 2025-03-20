# Define the HMM parameters
emission_probs = {
    "H": {"A": -2.322, "C": -1.737, "G": -1.737, "T": -2.322},
    "L": {"A": -1.737, "C": -2.322, "G": -2.322, "T": -1.737}
}

transition_probs = {
    "H": {"H": -1, "L": -1},
    "L": {"H": -1.322, "L": -0.737}
}

states = ["H", "L"]
start_probs = {"H": -1, "L": -1}

# Input sequence
input_str = "GGCACTGAA"
input_list = list(input_str)

# Initialize Viterbi result dictionary
vit_res = {}

# Step 1: Initialization for the first character
v_init_H = start_probs["H"] + emission_probs["H"][input_str[0]]
v_init_L = start_probs["L"] + emission_probs["L"][input_str[0]]
vit_res[0] = {"H": v_init_H, "L": v_init_L}

# Step 2: Recursion - Fill the Viterbi table
for i in range(1, len(input_str)):
    # Initialize temporary dictionary for current position
    temp_dict = {state: 0 for state in states}
    vit_res[i] = temp_dict

# Compute probabilities for each position and state
for i in range(1, len(input_str)):
    for j in range(len(states)):
        current_state = states[j]
        # Emission probability for current state and observation
        term1 = emission_probs[current_state][input_str[i]]
        
        # Calculate maximum probability from previous states
        lis = [
            vit_res[i-1][states[k]] + transition_probs[states[k]][current_state]
            for k in range(len(states))
        ]
        maximum = max(lis)
        
        # Final probability for current state at position i
        final_res = round(term1 + maximum, 6)
        vit_res[i][current_state] = final_res

# Step 3: Extract probabilities for H and L states
h_lis = []
l_lis = []

for key in vit_res.keys():
    val = vit_res[key]
    h_lis.append(val["H"])
    l_lis.append(val["L"])

# Step 4: Print the Viterbi table
print("States", end="\t\t")
for key in vit_res.keys():
    char = input_str[key]
    print(char, end="\t\t")
print("\n")

print("H", end="\t\t")
for h in h_lis:
    print(h, end="\t\t")
print("\n\n")

print("L", end="\t\t")
for l in l_lis:
    print(l, end="\t\t")
print("\n")

# Step 5: Determine the most likely path
max_path = []
print("\nPATH SEQUENCE")
for i in range(len(h_lis)):
    if h_lis[i] > l_lis[i]:
        max_path.append("H")
    else:
        max_path.append("L")
print(max_path)
