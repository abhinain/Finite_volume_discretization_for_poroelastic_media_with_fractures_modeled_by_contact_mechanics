"""
Main run script for running example 4.
"""
import setup_4
import models

mesh_args = {'mesh_size_frac': 0.5, 'mesh_size_min': 0.1 * 0.1, 'mesh_size_bound': 0.8}
# Mesh size in paper: 
# mesh_args = {'mesh_size_frac': 0.2, 'mesh_size_min': 0.001}

run_name = 'example_4'
setup = setup_4.Example4Setup(mesh_args, run_name)

models.run_biot(setup)
