def empirical_formula(molecule):
    atoms = count_atoms(molecule)
    min_count = min(atoms.values())
    empirical_formula = ''.join(f"{atom}{count // min_count}" if min_count > 1 else atom for atom, count in atoms.items())
    return empirical_formula

molecule = "C6H12O6"
print("Molecule:", molecule)
print("Empirical Formula:", empirical_formula(molecule))
