# batch
Balance the chemical equation and generate a printable form

## How this works
```
.
|_ batch.yaml                       # input the information of the compounds in this file
|_ gen.py                           # then run this script to generate the printable form
|_ sampleIDs.yaml                   # generated automatically
|_ outputs/
    |_ 20250101-CaNiSe3,CsSe2,BiNiPO14,BiNiO1.xlsx   # An example output file(form to print)
```

## Example of batch.yaml
The program is set to handle only the first yaml document in `batch.yaml`.
> These are imaginary reactions for demonstration purposes
```yaml
---
date: 2025-01-01
reactions: 
    - CaO + Ni + Se ->  CaNiSe0.9O 0.5g       # mass can be writed behind a compound
    - 0.1g Cs + Se -> CsSe                    # or in front of a compound
    - Bi2O3 0.1145g+Ni+P+Bi -> Bi0.9NiPO 0.7g # Only the mass on the far left is used
    # Add notes below the reaction
    - |
        Bi2O3 + NiO + Ni + Bi -> BiNiO2 0.5g
        12h->1200->6h->1200-> -121            # Add notes, such as the reaction condition
        use the Ni from Ponyville             # Another note
---
# ... eailer reactions
date: 2024-12-31
# ...
```

# TODO
version 0.2.0 goals:
- [] Give the error range

