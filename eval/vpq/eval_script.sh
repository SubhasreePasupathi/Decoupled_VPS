export PYTHONPATH=$PYTHONPATH:`pwd`
python3 tools/eval_vpq.py \
  --submit_dir /home/subha/vpq_computation/psp_pcan_pans_unified \
  --truth_dir /home/subha/vpq_computation/panoptic_video/ \
  --pan_gt_json_file /home/subha/vpq_computation/panoptic_gt_val_city_vps.json

