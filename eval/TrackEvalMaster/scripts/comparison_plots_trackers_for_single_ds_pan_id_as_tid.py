import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import trackeval  # noqa: E402

plots_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'plots_subha_pan_id','trackers_comparison_on_a_dataset'))
tracker_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'trackers','format_for_plots','with_pan_id_as_track_id'))

# dataset = os.path.join('kitti', 'kitti_2d_box_train')
# classes = ['cars', 'pedestrian']

classes = ['car','person','all']

dataset = os.path.join('city_kitti_mots_single_dataset_multi_tracker', 'city_vps_mots')
data_fol = os.path.join(tracker_folder, dataset)
trackers = os.listdir(data_fol)
out_loc = os.path.join(plots_folder, dataset)
for cls in classes:
    trackeval.plotting.plot_compare_trackers(data_fol, trackers, cls, out_loc)


dataset = os.path.join('city_kitti_mots_single_dataset_multi_tracker', 'kitti_step_mots')
data_fol = os.path.join(tracker_folder, dataset)
trackers = os.listdir(data_fol)
out_loc = os.path.join(plots_folder, dataset)
for cls in classes:
    trackeval.plotting.plot_compare_trackers(data_fol, trackers, cls, out_loc)


dataset = os.path.join('city_kitti_mots_single_dataset_multi_tracker', 'waymo_mots')
data_fol = os.path.join(tracker_folder, dataset)
trackers = os.listdir(data_fol)
out_loc = os.path.join(plots_folder, dataset)
for cls in classes:
    trackeval.plotting.plot_compare_trackers(data_fol, trackers, cls, out_loc)
