#!/bin/bash

# Please adjust these settings according to your needs.
#SBATCH --account=ds_ga_1012-2025sp
#SBATCH --partition=c12m85-a100-1
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=4:00:00
#SBATCH --mem=32GB
#SBATCH --gres=gpu:1
#SBATCH --job-name=truthfulqa
#SBATCH --mail-type=ALL
#SBATCH --mail-user=js11052@nyu.edu
#SBATCH --output="truthfulqa_3c.out"
#SBATCH --error=truthfulqa_3c.err

module purge
cd /scratch/js11052/nlu_s25/hw3/
OVERLAY_FILE=/scratch/js11052/overlay-25GB-500K.ext3:rw
SINGULARITY_IMAGE=/scratch/js11052/cuda11.4.2-cudnn8.2.4-devel-ubuntu20.04.3.sif

singularity exec --nv \
		--bind /scratch/js11052/ \
	    --overlay $OVERLAY_FILE $SINGULARITY_IMAGE \
	    /bin/bash -c "
		source /ext3/miniconda3/etc/profile.d/conda.sh
		conda activate
		cd /scratch/js11052/nlu_s25/hw3/
		bash hpc/run_3c.sh
	"