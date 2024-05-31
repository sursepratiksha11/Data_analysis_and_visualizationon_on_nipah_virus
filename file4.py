import matplotlib.pyplot as plt

def generate_graph():
    # Data
    states = ['Kerala', 'West Bengal', 'Perak', 'Negeri Sembilan', 'Selangor', 'Pahang', 'Kuala Lumpur', 'Sarawak', 'Faridpur', 'Tangail', 'Rajbari', 'Kushtia', 'Jhalokati', 'Naogaon', 'Manikganj', 'Gopalganj', 'Mymensingh', 'Joypurhat', 'Chandpur', 'Khulna', 'Magura', 'Satkhira', 'Rangpur', 'Yunnan', 'Hunnan']
    species = ['Cynopterus brachyotis', 'Cynopterus brachyotis', 'Cynopterus brachyotis', 'Cynopterus brachyotis', 'Cynopterus brachyotis', 'Cynopterus brachyotis', 'Cynopterus brachyotis', 'Cynopterus brachyotis', 'Pteropus mediusb', 'Pteropus mediusb', 'Pteropus mediusb', 'Pteropus mediusb', 'Pteropus mediusb', 'Pteropus mediusb', 'Pteropus mediusb', 'Pteropus mediusb', 'Pteropus mediusb', 'Pteropus mediusb', 'Pteropus mediusb', 'Pteropus mediusb', 'Pteropus mediusb', 'Pteropus mediusb', 'Pteropus mediusb', 'Megaderma lyra', 'Hipposideros larvatus', 'Cynopterus sphinx']

    # Create a dictionary to store species found in each state
    state_species = {
        'Kerala': ['Cynopterus brachyotis', 'Taphozous melanopogon', 'Cynopterus sphinx', 'Megaderma lyra'],
        'West Bengal': ['Cynopterus brachyotis', 'Cynopterus sphinx'],
        'Perak': ['Cynopterus brachyotis', 'Megaerops ecaudatus', 'Hipposideros larvatus', 'Eonycteris spelaea'],
        'Negeri Sembilan': ['Cynopterus brachyotis'],
        'Selangor': ['Cynopterus brachyotis'],
        'Pahang': ['Cynopterus brachyotis'],
        'Kuala Lumpur': ['Cynopterus brachyotis'],
        'Sarawak': ['Cynopterus brachyotis'],
        'Faridpur': ['Pteropus mediusb', 'Hipposideros larvatus'],
        'Tangail': ['Pteropus mediusb'],
        'Rajbari': ['Pteropus mediusb'],
        'Kushtia': ['Pteropus mediusb'],
        'Jhalokati': ['Pteropus mediusb'],
        'Naogaon': ['Pteropus mediusb'],
        'Manikganj': ['Pteropus mediusb'],
        'Gopalganj': ['Pteropus mediusb'],
        'Mymensingh': ['Pteropus mediusb'],
        'Joypurhat': ['Pteropus mediusb'],
        'Chandpur': ['Pteropus mediusb', 'Hipposideros larvatus'],
        'Khulna': ['Pteropus mediusb'],
        'Magura': ['Pteropus mediusb'],
        'Satkhira': ['Pteropus mediusb'],
        'Rangpur': ['Pteropus mediusb'],
        'Yunnan': ['Megaderma lyra', 'Hipposideros larvatus', 'Cynopterus sphinx'],
        'Hunnan': ['Megaderma lyra', 'Hipposideros larvatus', 'Cynopterus sphinx']
    }

    # Create a dictionary to map states to countries
    state_countries = {
        'Kerala': 'India',
        'West Bengal': 'India',
        'Perak': 'Malaysia',
        'Negeri Sembilan': 'Malaysia',
        'Selangor': 'Malaysia',
        'Pahang': 'Malaysia',
        'Kuala Lumpur': 'Malaysia',
        'Sarawak': 'Malaysia',
        'Faridpur': 'Bangladesh',
        'Tangail': 'Bangladesh',
        'Rajbari': 'Bangladesh',
        'Kushtia': 'Bangladesh',
        'Jhalokati': 'Bangladesh',
        'Naogaon': 'Bangladesh',
        'Manikganj': 'Bangladesh',
        'Gopalganj': 'Bangladesh',
        'Mymensingh': 'Bangladesh',
        'Joypurhat': 'Bangladesh',
        'Chandpur': 'Bangladesh',
        'Khulna': 'Bangladesh',
        'Magura': 'Bangladesh',
        'Satkhira': 'Bangladesh',
        'Rangpur': 'Bangladesh',
        'Yunnan': 'China',
        'Hunnan': 'China'
    }

    # Plot
    plt.figure(figsize=(12, 6))
    for state, species_list in state_species.items():
        y_values = [states.index(state) + 1] * len(species_list)  # Adjust y-values to place points at different heights
        plt.scatter(species_list, y_values, color='skyblue', marker='o')

    # Add labels to y-axis ticks to indicate the countries
    yticks_labels = [f"{state} ({state_countries[state]})" for state in states]
    plt.yticks(range(1, len(states) + 1), yticks_labels)

    plt.title('Bat Species Distribution Across States')
    plt.xlabel('Bat Species')
    plt.ylabel('State (Country)')
    plt.grid(True)
    plt.show()

# Uncomment the below line to test the generate_graph function independently
generate_graph()
