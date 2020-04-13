#!/bin/sh
# Slurm flags                                                                                                                                                                              
#SBATCH -p ProdQ                                                                                                                                                                                
#SBATCH -N 4                                                                                                                                                                                     
#SBATCH -t 10:00:00                                                                                                                                                                                 
#SBATCH -A ucd01                                                                                                                                                                                        
#SBATCH -o submission_log/output.txt                                                                                                                                                                                                          
# Mail me on job start & end                                                                                                                                                                            
#SBATCH --mail-user=pierre.aumjaud@ucd.ie                                                                                                                                    
#SBATCH --mail-type=BEGIN,END  

cd $SLURM_SUBMIT_DIR

# Load software                                                                                                                                                                                                                
module load conda/2
source activate base_G5
module load cuda/10.0

# Run code                                                                                                                                                                                    
date
# time ./optimise_hyperparameter_pendulum.sh
time ./run_experiments_pendulum.sh
date
