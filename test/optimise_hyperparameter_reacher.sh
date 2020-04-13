#!/bin/bash

python train.py --algo ppo2 --env Reacher2Dof-v0 -n 1000000 --log-folder logs/ppo2/Reacher2Dof-v0_1_opti_1M_100trials/ -optimize --n-trials 100 --n-jobs -1 --sampler tpe --pruner median  &> submission_log/log_Reacher2Dof-v0_ppo2_opti_1M_100trials.run
# python train.py --algo a2c --env Pendulum-v0 -n 100000 -optimize --n-trials 100 --n-jobs -1 --sampler tpe --pruner median
# python train.py --algo acktr --env Pendulum-v0 -n 100000 -optimize --n-trials 100 --n-jobs -1 --sampler tpe --pruner median
# python train.py --algo ppo2 --env Pendulum-v0 -n 100000 -optimize --n-trials 100 --n-jobs -1 --sampler tpe --pruner median
# python train.py --algo ddpg --env Pendulum-v0 -n 100000 -optimize --n-trials 100 --n-jobs -1 --sampler tpe --pruner median
# python train.py --algo sac --env Pendulum-v0 -n 100000 -optimize --n-trials 100 --n-jobs -1 --sampler tpe --pruner median
# python train.py --algo td3 --env Pendulum-v0 -n 100000 -optimize --n-trials 100 --n-jobs -1 --sampler tpe --pruner median
# python train.py --algo ppo2 --env Pendulum-v0 -n 100000 -optimize --n-trials 100 --n-jobs -1 --sampler tpe --pruner median
# python train.py --algo trpo --env Pendulum-v0 -n 100000 -optimize --n-trials 100 --n-jobs -1 --sampler tpe --pruner median

