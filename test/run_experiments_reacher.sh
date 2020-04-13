#!/bin/bash


for ((i=0;i<10;i+=1))
do
    # echo "1"
    # python train.py --algo a2c --env ReacherBulletEnv-v0 --eval-episodes 10 --seed $i &> submission_log/log01.run
    # echo "2"
    # python train.py --algo acktr --env ReacherBulletEnv-v0 --eval-episodes 10 --seed $i &> submission_log/log02.run 
    echo "PPO $i"
    python train.py --algo ppo2 --env Reacher2Dof-v0 --seed $i --log-folder logs/ppo2/Reacher2Dof-v0_Env_8_norm/ &> submission_log/log_ppo_0$i.run
    # echo "4"
    # python train.py --algo ddpg --env ReacherBulletEnv-v0 --eval-episodes 10 --seed $i &> submission_log/log04.run
    # echo "5"
    # python train.py --algo sac --env ReacherBulletEnv-v0 -n 10000 --seed $i &> submission_log/log05.run
    # echo "6"
    # python train.py --algo td3 --env ReacherBulletEnv-v0 --eval-episodes 10 --seed $i &> submission_log/log06.run
    # echo "7"
    # python train.py --algo trpo --env ReacherBulletEnv-v0 --eval-episodes 10 --seed $i &> submission_log/log07.run
    # echo "6"
done

