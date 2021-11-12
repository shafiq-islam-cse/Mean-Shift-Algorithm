import mean_shift as ms

data = get_data_from_somewhere()
mean_shifter = ms.MeanShift()
mean_shift_result = mean_shifter.cluster(data, kernel_bandwidth = 10)

original_points =  mean_shift_result.original_points
shifted_points = mean_shift_result.shifted_points
cluster_assignments = mean_shift_result.cluster_ids

# If you want to use multivariate gaussian kernel
# By default it uses unviariate gaussian kernel
# Make sure the dimensions of 'data' and the kernel match
mean_shifter = ms.MeanShift(kernel='multivariate_gaussian')
mean_shift_result = mean_shifter.cluster(data, kernel_bandwidth = [10,20,30])