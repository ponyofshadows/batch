# created by: ponyofshadows
# Balance the chemical equation and generate a printable form

from enum import Enum, auto
from shadowslib import (
    data.io.load_yaml_first_doc
)



# Constants-------------------------------------#
# Reference: iupac.qmul.ac.uk/AtWt/
class MolarMass(Enum):
    # Period 1
    H = '1.0080'       # Hydrogen
    He = '4.002602'    # Helium
    
    # Period 2
    Li = '6.94'        # Lithium
    Be = '9.0121831'   # Beryllium
    B = '10.81'        # Boron
    C = '12.011'       # Carbon
    N = '14.007'       # Nitrogen
    O = '15.999'       # Oxygen
    F = '18.998403162' # Fluorine
    Ne = '20.1797'     # Neon
    
    # Period 3
    Na = '22.98976928' # Sodiumprint(result)  
    Mg = '24.305'      # Magnesium
    Al = '26.9815384'  # Aluminium
    Si = '28.085'      # Silicon
    P = '30.973761998' # Phosphorus
    S = '32.06'        # Sulfur
    Cl = '35.45'       # Chlorine
    Ar = '39.95'       # Argon
    
    # Period 4
    K = '39.0983'     # Potassium
    Ca = '40.078'     # Calcium
    Sc = '44.955907'  # Scandium
    Ti = '47.867'     # Titanium
    V = '50.9415'     # Vanadium
    Cr = '51.9961'    # Chromium
    Mn = '54.938043'  # Manganese
    Fe = '55.845'     # Iron
    Co = '58.933194'  # Cobalt
    Ni = '58.6934'    # Nickel
    Cu = '63.546'     # Copper
    Zn = '65.38'      # Zinc
    Ga = '69.723'     # Gallium
    Ge = '72.630'     # Germanium
    As = '74.921595'  # Arsenic
    Se = '78.971'     # Selenium
    Br = '79.904'     # Bromine
    Kr = '83.798'     # Krypton
    
    # Period 5
    Rb = '85.4678'    # Rubidium
    Sr = '87.62'      # Strontium
    Y = '88.905838'   # Yttrium
    Zr = '91.222'     # Zirconium
    Nb = '92.90637'   # Niobium
    Mo = '95.95'      # Molybdenum
    Ru = '101.07'     # Ruthenium
    Rh = '102.90549'  # Rhodium
    Pd = '106.42'     # Palladium
    Ag = '107.8682'   # Silver
    Cd = '112.414'    # Cadmium
    In = '114.818'    # Indium
    Sn = '118.710'    # Tin
    Sb = '121.760'    # Antimony
    Te = '127.60'     # Tellurium
    I = '126.90447'   # Iodine
    Xe = '131.293'    # Xenon
    
    # Period 6
    Cs = '132.90545196' # Caesium
    Ba = '137.327'      # Barium
    La = '138.90547'    # Lanthanum
    Ce = '140.116'      # Cerium
    Pr = '140.90766'  # Praseodymium
    Nd = '144.242'    # Neodymium
    Sm = '150.36'     # Samarium
    Eu = '151.964'    # Europium
    Gd = '157.249'    # Gadolinium
    Tb = '158.925354' # Terbium
    Dy = '162.500'    # Dysprosium
    Ho = '164.930329' # Holmium
    Er = '167.259'    # Erbium
    Tm = '168.934219' # Thulium
    Yb = '173.045'    # Ytterbium
    Lu = '174.96669'  # Lutetium
    Hf = '178.486'    # Hafnium
    Ta = '180.94788'  # Tantalum
    W = '183.84'      # Tungsten
    Re = '186.207'    # Rhenium
    Os = '190.23'     # Osmium
    Ir = '192.217'    # Iridium
    Pt = '195.084'    # Platinum
    Au = '196.966570' # Gold
    Hg = '200.592'    # Mercury
    Tl = '204.38'     # Thallium
    Pb = '207.2'      # Lead
    Bi = '208.98040'  # Bismuth

    # Period 7
    Th = '232.0377'   # Thorium
    Pa = '231.03588'  # Protactinium
    U = '238.02891'   # Uranium
# Functions ---------------------------------------------------#
def modify_temp_contorl_statement(note_first_line):
    """
    [util, used in next func]
    Modify the first line of the note(may be the temperature control statement.)
    - complete the Celsius symbol (insert before a '->' if there is a number before it)
    - change '->' to right arrow 
    """
    parts = note_first_line.split("->")
    if len(parts) > 1:
        modified_parts = []
        for part in parts[:-1]:
            part = part.strip()
            if part[-1].isdigit():
                part += "°C"
            modified_parts.append(part+ "→")
        modified_parts.append("→ " + parts[-1].strip())
        return join(modified_parts)
    else:
        return note_first_line.strip()
    
def split_raw_reaction_info(raw_reaction_info):
    """
    [used in main]
    Read a reaction from the raw reaction info, whose 
    first line is the reaction and the rest are notes.
    """
    reaction = raw_reaction_info[0].strip()
    note = "\n".join(raw_reaction_info[1:]) if len(raw_reaction_info) > 1 else ""
    return reaction, note


def read_raw_reaction(raw_reaction):
class Compound:
def balancing_equation(compounds, input_mass):
def calculate_mass(stoichiometry, relative_molecular_mass):
def save_printable_form(sheet):
def save_sampleIDs(sheet):
    
# Main----------------------------------------------#
def main():
    doc = load_yaml_first_doc("./batch.yaml")
    sheet = {}

    sheet['date'] = doc["date"]
    sheet['reactions'] = []
    
    for raw_reaction_info in doc["reactions"]:
        reaction = {
                "compound_names" : [],
                "relative_molecular_mass" : [],
                "balance_info" : None,
                "stoichiometry" : None,
                "mass" : [],
                "note" : ""
                }
        raw_reaction, note = split_raw_reaction_info(raw_reaction_info)
        reaction['note'] = note

        input_mass = []
        compounds, input_mass = read_raw_reaction(raw_reaction)
        reaction["compound_names"] = [compound.name for compound in compounds]
        reaction["relative_molecular_mass"] = [compound.relative_molecular_mass for compound in compounds]
        reaction["balance_info"], reaction["stoichiometry"] = balancing_equation(compounds, input_mass)
        reaction["mass"] = calculate_mass(reaction["stoichiometry"], reaction["relative_molecular_mass"])
        
        sheet['reactions'].append(reaction)

    save_printable_form(sheet)
    save_sampleIDs(sheet)
        

if __name__ == "__main__":
    main()
#---------------------------------------------------#
