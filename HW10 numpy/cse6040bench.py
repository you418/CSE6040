#!/usr/bin/env python3

from timeit import timeit
from statistics import mean, median, stdev

def benchit(code, scope=globals(), min_time=0.2, trials=5, verbose=True):
	repeats = 1
	calibrating = True
	times = []
	while calibrating:
		for trial in range(trials):
			t = timeit(code, globals=scope, number=repeats)
			times.append(t)
		if t < min_time:
			repeats *= 10
			times = []
		calibrating = t < min_time
	assert t >= min_time
	total_time = sum(times)
	times_per_run = [t/repeats for t in times]
	results = {'code': code,
	           'trials': trials,
			   'repeats': repeats,
			   'trial_times': times,
			   'total_time': sum(times),
			   'times_per_run': times_per_run,
			   'min_time_per_run': min(times_per_run),
			   'max_time_per_run': max(times_per_run),
			   'mean_time_per_run': mean(times_per_run),
			   'stdev_time_per_run': stdev(times_per_run)}
	if verbose:
		print(f"Timing result: ({trials} trials) x ({repeats} runs) in {total_time} secs")
		print(f"==> {results['mean_time_per_run']} secs per run")
	return results

# eof
