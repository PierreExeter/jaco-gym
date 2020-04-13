#!/bin/bash

# j=3
for ((j=1;j<9;j+=1))
do
echo "NUMBER OF ENV: $j"

for ((i=0;i<10;i+=1))
do
    echo "a2c $i"
    python train.py --algo a2c --env Pendulum-v0 -n 100000 --seed $i --log-folder logs/a2c/Pendulum-v0_Env_$j/ &> submission_log/log_a2c_0$i.run
    # echo "acktr $i"
    # python train.py --algo acktr --env Pendulum-v0 -n 100000 --seed $i --log-folder logs/acktr/Pendulum-v0_seedExp/ &> submission_log/log_acktr_0$i.run
    # echo "ppo2 $i"
    # python train.py --algo ppo2 --env Pendulum-v0 -n 100000 --seed $i --log-folder logs/ppo2/Pendulum-v0_seedExp/ &> submission_log/log_ppo2_0$i.run
    # echo "ddpg $i"
    # python train.py --algo ddpg --env Pendulum-v0 -n 100000 --seed $i --log-folder logs/ddpg/Pendulum-v0_seedExp/ &> submission_log/log_ddpg_0$i.run
    # echo "sac $i"
    # python train.py --algo sac --env Pendulum-v0 -n 100000 --seed $i --log-folder logs/sac/Pendulum-v0_seedExp/ &> submission_log/log_sac_0$i.run
    # echo "td3 $i"
    # python train.py --algo td3 --env Pendulum-v0 -n 100000 --seed $i --log-folder logs/td3/Pendulum-v0_seedExp/ &> submission_log/log_td3_0$i.run
    # echo "trpo $i"
    # python train.py --algo trpo --env Pendulum-v0 -n 100000 --seed $i --log-folder logs/trpo/Pendulum-v0_seedExp/ &> submission_log/log_trpo_0$i.run
done
done


for ((i=0;i<10;i+=1))
do
    echo "a2c $i"
    python train.py --algo a2c --env Pendulum-v0 -n 100000 --seed $i --log-folder logs/a2c/Pendulum-v0_Env_1_norm/ &> submission_log/log_a2c_0$i.run
done


for ((i=0;i<10;i+=1))
do
    echo "a2c $i"
    python train.py --algo a2c --env Pendulum-v0 -n 100000 --seed $i --log-folder logs/a2c/Pendulum-v0_Env_8_norm/ &> submission_log/log_a2c_0$i.run
done


