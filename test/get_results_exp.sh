#!/bin/bash


# j=3
# for ((j=3;j<9;j+=1))
# do
# echo "NUMBER OF ENV: $j"

for ((i=1;i<11;i+=1))
do
    echo "a2c $i"
    python enjoy.py --algo a2c --env Reacher2Dof-v0 -f logs/a2c/Reacher2Dof-v0_Env_8_norm/ --exp-id $i --no-render -n 15000
    python plot_results.py -f logs/a2c/Reacher2Dof-v0_Env_8_norm/a2c/Reacher2Dof-v0_$i/

    echo "acktr $i"
    python enjoy.py --algo acktr --env Reacher2Dof-v0 -f logs/acktr/Reacher2Dof-v0_Env_8_norm/ --exp-id $i --no-render -n 15000
    python plot_results.py -f logs/acktr/Reacher2Dof-v0_Env_8_norm/acktr/Reacher2Dof-v0_$i/

    echo "ddpg $i"
    python enjoy.py --algo ddpg --env Reacher2Dof-v0 -f logs/ddpg/Reacher2Dof-v0_Env_8_norm/ --exp-id $i --no-render -n 15000
    python plot_results.py -f logs/ddpg/Reacher2Dof-v0_Env_8_norm/ddpg/Reacher2Dof-v0_$i/

    echo "ppo2 $i"
    python enjoy.py --algo ppo2 --env Reacher2Dof-v0 -f logs/ppo2/Reacher2Dof-v0_Env_8_norm/ --exp-id $i --no-render -n 15000
    python plot_results.py -f logs/ppo2/Reacher2Dof-v0_Env_8_norm/ppo2/Reacher2Dof-v0_$i/

    echo "sac $i"
    python enjoy.py --algo sac --env Reacher2Dof-v0 -f logs/sac/Reacher2Dof-v0_Env_8_norm/ --exp-id $i --no-render -n 15000
    python plot_results.py -f logs/sac/Reacher2Dof-v0_Env_8_norm/sac/Reacher2Dof-v0_$i/

    echo "td3 $i"
    python enjoy.py --algo td3 --env Reacher2Dof-v0 -f logs/td3/Reacher2Dof-v0_Env_8_norm/ --exp-id $i --no-render -n 15000
    python plot_results.py -f logs/td3/Reacher2Dof-v0_Env_8_norm/td3/Reacher2Dof-v0_$i/

    echo "trpo $i"
    python enjoy.py --algo trpo --env Reacher2Dof-v0 -f logs/trpo/Reacher2Dof-v0_Env_8_norm/ --exp-id $i --no-render -n 15000
    python plot_results.py -f logs/trpo/Reacher2Dof-v0_Env_8_norm/trpo/Reacher2Dof-v0_$i/

done
# done


    # echo "ppo2 $i"
    # python enjoy.py --algo a2c --env Pendulum-v0 -f logs/a2c/Pendulum-v0_Env_1 --exp-id $i --no-render -n 20000
    # python plot_results.py -f logs/a2c/Pendulum-v0_Env_1/a2c/Pendulum-v0_$i/