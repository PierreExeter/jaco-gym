#!/bin/sh
# Slurm flags                                                                                                                                                                              
#SBATCH -p ProdQ                                                                                                                                                                                
#SBATCH -N 16                                                                                                                                                                                     
#SBATCH -t 20:00:00                                                                                                                                                                                 
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
time python train.py --algo a2c --env ReacherBulletEnv-v0 --eval-episodes 10 --seed 0 &> submission_log/log01.run
time python train.py --algo acktr --env ReacherBulletEnv-v0 --eval-episodes 10 --seed 0 &> submission_log/log02.run
time python train.py --algo ppo2 --env ReacherBulletEnv-v0 --eval-episodes 10 --seed 0 &> submission_log/log03.run
time python train.py --algo ddpg --env ReacherBulletEnv-v0 --eval-episodes 10 --seed 0 &> submission_log/log04.run
time python train.py --algo sac --env ReacherBulletEnv-v0 --eval-episodes 10 --seed 0 &> submission_log/log05.run
time python train.py --algo td3 --env ReacherBulletEnv-v0 --eval-episodes 10 --seed 0 &> submission_log/log06.run
time python train.py --algo trpo --env ReacherBulletEnv-v0 --eval-episodes 10 --seed 0 &> submission_log/log07.run

time python train.py --algo a2c --env Reacher1Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log08.run
time python train.py --algo acktr --env Reacher1Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log09.run
time python train.py --algo ppo2 --env Reacher1Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log10.run
time python train.py --algo ddpg --env Reacher1Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log11.run
time python train.py --algo sac --env Reacher1Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log12.run
time python train.py --algo td3 --env Reacher1Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log13.run
time python train.py --algo trpo --env Reacher1Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log14.run

time python train.py --algo a2c --env Reacher2Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log15.run
time python train.py --algo acktr --env Reacher2Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log16.run
time python train.py --algo ppo2 --env Reacher2Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log17.run
time python train.py --algo ddpg --env Reacher2Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log18.run
time python train.py --algo sac --env Reacher2Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log19.run
time python train.py --algo td3 --env Reacher2Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log20.run
time python train.py --algo trpo --env Reacher2Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log21.run

time python train.py --algo a2c --env Reacher3Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log22.run
time python train.py --algo acktr --env Reacher3Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log23.run
time python train.py --algo ppo2 --env Reacher3Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log24.run
time python train.py --algo ddpg --env Reacher3Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log25.run
time python train.py --algo sac --env Reacher3Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log26.run
time python train.py --algo td3 --env Reacher3Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log27.run
time python train.py --algo trpo --env Reacher3Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log28.run

time python train.py --algo a2c --env Reacher4Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log29.run
time python train.py --algo acktr --env Reacher4Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log30.run
time python train.py --algo ppo2 --env Reacher4Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log31.run
time python train.py --algo ddpg --env Reacher4Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log32.run
time python train.py --algo sac --env Reacher4Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log33.run
time python train.py --algo td3 --env Reacher4Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log34.run
time python train.py --algo trpo --env Reacher4Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log35.run

time python train.py --algo a2c --env Reacher5Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log36.run
time python train.py --algo acktr --env Reacher5Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log37.run
time python train.py --algo ppo2 --env Reacher5Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log38.run
time python train.py --algo ddpg --env Reacher5Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log39.run
time python train.py --algo sac --env Reacher5Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log40.run
time python train.py --algo td3 --env Reacher5Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log41.run
time python train.py --algo trpo --env Reacher5Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log42.run

time python train.py --algo a2c --env Reacher6Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log43.run
time python train.py --algo acktr --env Reacher6Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log44.run
time python train.py --algo ppo2 --env Reacher6Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log45.run
time python train.py --algo ddpg --env Reacher6Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log46.run
time python train.py --algo sac --env Reacher6Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log47.run
time python train.py --algo td3 --env Reacher6Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log48.run
time python train.py --algo trpo --env Reacher6Dof-v0 --eval-episodes 10 --seed 0 &> submission_log/log49.run
date
