import os
import numpy as np
import matplotlib.pyplot as plt
"""Provide the primary functions."""
atomic_weights = {
    'H': 1.00784,
    'C': 12.0107,
    'N': 14.0067,
    'O': 15.999,
    'P': 30.973762,
    'F': 18.998403,
    'Cl': 35.453,
    'Br': 79.904,
}

atom_colors = {
    'H': 'white',
    'C': '#D3D3D3',
    'N': '#add8e6',
    'O': 'red',
    'P': '#FFA500',
    'F': '#FFFFE0',
    'Cl': '#98FB98',
    'Br': '#F4A460',
    'S': 'yellow'
}



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


"""
Functions for manipulating pdb files.
"""

"""
functions for manipulating xyz files.
"""

def open_xyz(file_location):

    # Open an xyz file and return symbols and coordinates.
    xyz_file = np.genfromtxt(fname=file_location, skip_header=2, dtype="unicode")
    symbols = xyz_file[:, 0]
    coords = xyz_file[:, 1:]
    coords = coords.astype(np.float)
    return symbols, coords


def write_xyz(file_location, symbols, coordinates):

    num_atoms = len(symbols)

    if num_atoms != len(coordinates):
        raise ValueError(
            f"write_xyz : the number of symbols ({num_atoms}) and number of coordinates ({len(coordinates)}) must be the same to write xyz file!"
        )

    with open(file_location, "w+") as f:
        f.write("{}\n".format(num_atoms))
        f.write("XYZ file\n")

        for i in range(num_atoms):
            f.write(
                "{}\t{}\t{}\t{}\n".format(
                    symbols[i], coordinates[i, 0], coordinates[i, 1], coordinates[i, 2]
                )
            )


def calculate_distance(rA, rB):
    """Calculate the distance between two points.

    Parameters
    ----------
    rA, rB : np.ndarray
        The coordinates of each point.

    Returns
    -------
    distance : float
        The distance between the two points.

    Examples
    --------
    >>> r1 = np.array([0, 0, 0])
    >>> r2 = np.array([0, 0.1, 0])
    >>> calculate_distance(r1, r2)
    0.1
    """
    dist_vec = rA - rB
    distance = np.linalg.norm(dist_vec)

    return distance

def calculate_angle(rA, rB, rC, degrees=False):
    AB = rB - rA
    BC = rB - rC
    theta=np.arccos(np.dot(AB, BC)/(np.linalg.norm(AB)*np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta

"""
Functions for visualization of molecules
"""

def draw_molecule(coordinates, symbols, draw_bonds=None, save_location=None, dpi=300):

    # Create figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Get colors - based on atom name
    colors = []
    for atom in symbols:
        colors.append(atom_colors[atom])

    size = np.array(plt.rcParams["lines.markersize"] ** 2) * 200 / (len(coordinates))

    ax.scatter(
        coordinates[:, 0],
        coordinates[:, 1],
        coordinates[:, 2],
        marker="o",
        edgecolors="k",
        facecolors=colors,
        alpha=1,
        s=size,
    )

    # Draw bonds
    if draw_bonds:
        for atoms, bond_length in draw_bonds.items():
            atom1 = atoms[0]

def bond_histogram(bond_list, save_location=None, dpi=300, graph_min=0, graph_max=2):
    lengths = []
    for atoms, bond_length in bond_list.items():
        lengths.append(bond_length)
    
    bins = np.linspace(graph_min, graph_max)
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    plt.xlabel('Bond Length (angstrom)')
    plt.ylabel('Number of Bonds')
    
    ax.hist(lengths, bins=bins)
    
    # Save figure
    if save_location:
        plt.savefig(save_location, dpi=dpi)
    
    return ax

"""
Functions for molecule analysis
"""

def build_bond_list(coordinates, max_bond=1.5, min_bond=0):
    """
    Build a list of bonds in a set of coordinates based on a distance criteria.

    Parameters
    ----------
    coordinates: np.ndarray
        The coordinates of the atoms to analyze in an (natoms, ndim) array.

    max_bond: float, optional
        The maximum distance for two atoms to be considered bonded.

    min_bond: float, optional
        The minimum distance for two atoms to be considered bonded.

    Returns
    -------
    bonds: dict
        A dictionary containing bonded atoms with atom pairs as keys and the distance between the atoms as the value.
    """

    # Find the bonds in a molecule (set of coordinates) based on distance criteria.
    bonds = {}
    num_atoms = len(coordinates)

    for atom1 in range(num_atoms):
        for atom2 in range(atom1, num_atoms):
            distance = calculate_distance(coordinates[atom1], coordinates[atom2])
            if distance > min_bond and distance < max_bond:
                bonds[(atom1, atom2)] = distance

    return bonds
