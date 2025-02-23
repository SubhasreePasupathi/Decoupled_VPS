export PYTHONPATH=$PYTHONPATH:`pwd`
python3 tools/eval_vpq.py \
  --submit_dir /home/subha/Videos/Evaluate/eval_VPS_Pcan_important/vpq_computation/sseg_bs_dm_cv_vpq/sseg_bs_dm_pans_unified \
  --truth_dir /home/subha/Videos/datasets/city_vps_val_after_running_scripts/val/panoptic_video \
  --pan_gt_json_file /home/subha/Videos/datasets/city_vps_val_after_running_scripts/panoptic_gt_val_city_vps.json

