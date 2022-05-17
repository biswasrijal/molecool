"""Provide the primary functions."""
import numpy as np

def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format).

    Replace this function and doc string for your own project.

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from.

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution.
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())

def zen(with_attribution=True):
    quote = """Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested."""
    
    if with_attribution:
      quote += "\n\tTim Peters"

    return quote

def open_pdb(f_loc):
    with open(f_loc) as f:
        data = f.readlines()
    c = []
    sym = []
    for l in data:
        if 'ATOM' in l[0:6] or 'HETATM' in l[0:6]:
            sym.append(l[76:79].strip())
            c2 = [float(x) for x in l[30:55].split()]
            c.append(c2)
    coords = np.array(c)
    return sym, coords

def write_xyz(file_location, symbols, coordinates):
    
    # Write an xyz file given a file location, symbols, and coordinates.
    num_atoms = len(symbols)
    
    if num_atoms != len(coordinates):
        raise ValueError(f"write_xyz : the number of symbols ({num_atoms}) and number of coordinates ({len(coordinates)}) must be the same to write xyz file!")
    
    with open(file_location, 'w+') as f:
        f.write('{}\n'.format(num_atoms))
        f.write('XYZ file\n')
        
        for i in range(num_atoms):
            f.write('{}\t{}\t{}\t{}\n'.format(symbols[i], 
                                              coordinates[i,0], coordinates[i,1], coordinates[i,2]))
