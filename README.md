# relion_to_cryosparc2
Export coordinates from Relion to Cryosparc2

This is useful if you are working with cryolo or other package which finds particles on your micrographs but you want to do the whole processing in Cryosparc using exactly the same coordinates used in Relion.

# workflow
1. Import coodrdinates to Relion
2. Extract particles using Relion (in particular if you are using cryolo and helical picking)
3. Export coordinates from Relion using this script:
  3a. Chose the particles.star from Extract job.
  3b. In Cryosparc2 use import a particle stack.
  3c. As Particle meta path choose the star file which was the output from the script
  3d. Chose the Micrographs from the CTF job.
  
In case of problems:
  * file name in star file is not corresponding to the name in cryosparc, rerun the script with proper file extention (e.g. _patch_aligned_doseweighted.mrc)
  * GPU based extraction doesn't work. Try using only CPU.
  * any other problems? let me know.
