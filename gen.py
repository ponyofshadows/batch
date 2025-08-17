# created by: ponyofshadows
# Balance the chemical equation and generate a printable form

from enum import Enum, auto
import re
from shadowslib import (
    data.io.load_yaml_first_doc
    data.string.to_number
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
def modify_temp_contorl_statement(note: str) -> str:
    """
    [used in main]
    Modify the temperature control statement in the note.
    - complete the Celsius symbol (insert before a '->' if there is a number before it)
    - change '->' to right arrow 
    """
    parts = note.split("->")
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
        return note.strip()
    
def split_raw_reaction_info(raw_reaction_info: str) -> str,str:
    """
    [used in main]
    Read a reaction from the raw reaction info, whose 
    first line is the reaction and the rest are notes.
    """
    reaction = raw_reaction_info[0].strip()
    note = "\n".join(raw_reaction_info[1:]) if len(raw_reaction_info) > 1 else ""
    return reaction, note

class Substance:
    def __init__(self, formula, elements_stoichiometry=None, relative_molecular_mass=None):
        self.formula = formula
        self.elements_stoichiometry = elements_stoichiometry
        self.relative_molecular_mass = relative_molecular_mass
    def parse_formula(self):
        """
        [used in main]
        Parse the chemical formula to extract elements and their stoichiometry.
        The formula is expected to be in the format: "Na2Se", "Na1.1FeO", "Ba3(PO4)2"
        """
        pattern = r'([A-Z][a-z]*|\d+\.?\d*|[()])'
        words = re.findall(pattern, self.formula)
        end_match = len(matches) - 1
        # read from back to front
        i = end_match
        current_element = None
        current_num = 1
        current_multiplier = 1
        while i>=0:
            word = words[i]
            if word.isdigit():
                current_num = to_number(word)
            elif word == ")":
                current_multiplier = current_num
                current_num = 1
            elif word[0].isupper():
                self.elements_stoichiometry[word] = current_num * current_multiplier
                current_num = 1
            elif word == "(":
                current_multiplier = 1
                current_num = 1        # not necessary if the user do as the rule


    def calculate_relative_molecular_mass(self):
        """
        [used in main]
        Calculate the relative molecular mass of the substance.
        The relative molecular mass is calculated by summing the molar masses of its elements.
        """
        return sum([MolarMass[self.elements[i]].value * self.element_stoichiometry[i] for i in range(len(self.elements))])
        
        
class Reaction:
    def __init__(self, reactants=[],products=[],balance_info=None, stoichiometry=None, mass=None, Note=None)
        self.reactants = reactants
        self.products = products
        self.balance_info = balance_info
        self.stoichiometry = stoichiometry
        self.mass = mass
        self.note = Note
    @classmethod
    def read_raw_reaction(cls, raw_reaction: str) -> list[Substance],list[Substance],str:
        """ [used in main]
        Read a raw reaction string and return the reactants, products, and input mass list.
        The raw reaction string is expected to be in the format:
        "Bi2O3 + NiO + Ni + Bi -> Bi0.9NiO2 0.5g"
        """
        substances = {}
        substances["reactants"] = []
        substances["products"] = []
        input_mass_list = []

        words = re.split(r"\s+|(\+|->)", raw_reaction)
        current_formula_type = "reactants"
        current_formula = None
        current_mass = None
        def consume_formula_and_mass_value():
            substances[current_substance_type].append(
                Substance(
                    formula=current_formula,
                    elements=[],
                    element_stoichiometry=[],
                    relative_molecular_mass=None
                )
            )
            input_mass_list.append(current_mass)
            current_formula = None
            current_mass = None
        for word in words:
            if word == "->":
                if current_formula != None:
                    consume_formula_and_mass_value()
                current_formula_type = "products"
            elif word == "+":
                if current_formula != None:
                    consume_formula_and_mass_value()
            elif re.fullmatch(r"\d+g", word):
                current_mass = to_number(word[:-1])  # remove 'g' and convert to number
                if current_substance != None:
                    consume_formula_and_mass_value()
            elif word[0].isupper():
                if current_formula != None:
                    consume_formula_and_mass_value()
                current_formula = word
                if current_mass != None
                    consume_formula_and_mass_value()
            
            return (
                substances["reactants"],
                substances["products"],
                input_mass_list
            )
    def balancing_equation(self):
        """
        [used in main]
        Balance the chemical equation.
        The balance_info will prompt the resaon if the equation is not balanced.
        ---
        - The number of unknowns is equal to the number of reactants and products minus 1
        - The number of equations is equal to the number of elements in the reaction
        ⬇️
        - every element corresponds to a list of coefficients whose number is equal to the number of reactants and products
        - In some cases, there is a positive solution only when the number of unknowns is greater than the number of linearly independent equations
        """

    def calculate_mass(self, input_mass_list: list):
        """
        [used in main]
        Calculate the mass of each substance in the reaction
        based on the input mass list.
        """
        self.mass = []
        input_mass_index = 0
        for substance in self.reactants + self.products:
            if input_mass_list[input_mass_index] is not None:
                equation_mole_num = input_mass_list[i] / substance.relative_molecular_mass
                break
            input_mass_index += 1
        i = 0
        for substance in self.reactants + self.products:
            if i == input_mass_index:
                self.mass.append(input_mass_list[i])
            else:
                self.mass.append(equation_mole_num * self.stoichiometry[i] * substance.relative_molecular_mass)

class Sheet:
    date = None
    reactions =[]
    @classmethod
    def append(cls, reaction):
    @classmethod
    def save_printable_form(cls):
    @classmethod
    def save_sampleIDs(cls):
    
# Main----------------------------------------------#
def main():
    doc = load_yaml_first_doc("./batch.yaml")

    Sheet.date = doc["date"]
    
    for raw_reaction_info in doc["reactions"]:
        reaction = Reaction(
            substances=[],
            balance_info=None,
            stoichiometry=None,
            note=None
        )
        raw_reaction, note = split_raw_reaction_info(raw_reaction_info)
        reaction.note = modify_temp_contorl_statement(note)

        input_mass_list = []
        reaction.reactants, reaction.products, input_mass_list = Reaction.read_raw_reaction(raw_reaction)
        for substance in reaction.reactants + reaction.products:
            substance.parse_formula()
            substance.calculate_relative_molecular_mass()
        reaction.balancing_equation(input_mass)
        reaction.calculate_mass()
        Sheet.append(reaction)

    Sheet.save_printable_form()
    Sheet.save_sampleIDs()

if __name__ == "__main__":
    main()
#---------------------------------------------------#
