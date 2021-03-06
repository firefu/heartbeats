#!/usr/bin/env python
from math import ceil
from os import system

def fmt_ext_args(s):
	prog, args = s.split(' ',1)
	return prog + " -x " + args.replace(' ','+')

suite1 = {
	'name': 'sf2',
	'thread_num': 4,
	'init_core': 4,
	'init_freq': 2,
	'programs': [
		fmt_ext_args("co -d step_heuristics"),
		fmt_ext_args("co -d uncoordinated_heuristics"),
		fmt_ext_args("co -d core_p_controller"),
		"fs",
		"fs2",
		"ca",
		fmt_ext_args("co -d core_heuristics"),
		fmt_ext_args("co -d freq_heuristics"),
		fmt_ext_args("co -d machine_state_p_controller -p 2"),
		fmt_ext_args("co -d machine_state_p_controller -p 5"),
		fmt_ext_args("co -d machine_state_p_controller -p 20"),
		fmt_ext_args("co -d machine_state_histeresis_p_controller -p 2"),
		fmt_ext_args("co -d machine_state_histeresis_p_controller -p 5"),
		fmt_ext_args("co -d machine_state_histeresis_p_controller -p 20"),
	],
	'repetitions': 5,
	'hr_min_max_pairs': [(7, 9), (4, 5), (5, 6), (8, 9), (8, 10), (4, 6), (9, 10), (4, 7), (9, 11), (10, 12), (11, 13), (10, 11), (7, 8), (10, 13), (11, 12), (8, 11), (6, 7), (5, 7), (6, 8), (6, 9)]
}
suite2 = suite1.copy()
suite2['name'] = 'sf1'
suite2['init_freq'] = 1
suite_ctl = {
	'name': 'ctl',
	'thread_num': 4,
	'init_core': 4,
	'init_freq': 2,
	'programs': [
		fmt_ext_args("co -d step_heuristics"),
		fmt_ext_args("co -d uncoordinated_heuristics"),
		fmt_ext_args("co -d core_p_controller -p 0.02"),
		fmt_ext_args("co -d core_p_controller -p 0.2"),
		fmt_ext_args("co -d machine_state_p_controller -p 2"),
		fmt_ext_args("co -d machine_state_p_controller -p 5"),
		fmt_ext_args("co -d machine_state_p_controller -p 20"),
		fmt_ext_args("co -d machine_state_histeresis_p_controller -p 2"),
		fmt_ext_args("co -d machine_state_histeresis_p_controller -p 5"),
		fmt_ext_args("co -d machine_state_histeresis_p_controller -p 20"),
		fmt_ext_args("co -d machine_state_pseudo_pi_controller -p 2 -q 0.5"),
		fmt_ext_args("co -d machine_state_pseudo_pi_controller -p 2 -q -0.5"),
		fmt_ext_args("co -d machine_state_pseudo_pi_controller -p 5 -q 1"),
		fmt_ext_args("co -d machine_state_pseudo_pi_controller -p 5 -q -1"),
		fmt_ext_args("co -d machine_state_pseudo_pi_controller -p 5 -q 2"),
		fmt_ext_args("co -d machine_state_pseudo_pi_controller -p 5 -q -2"),
	],
	'repetitions': 3,
	'hr_min_max_pairs': [(7, 9), (4, 5), (8, 9), (8, 10), (9, 11), (10, 12), (6, 7)]
}
macbook_pairs0 = [(1.8,1.85), (1,2), (2, 2.1), (2.9, 3), (1.5, 1.6)]
macbook_pairs1 = [(2.9, 3), (2,2.1)]
suite_ctl_macbook = suite_ctl.copy()
suite_ctl_macbook['name'] = 'ctlmb'
suite_ctl_macbook['hr_min_max_pairs'] = macbook_pairs1
suite_compare_bothness_mb = {
	'name': 'bo2',
	'thread_num': 4,
	'init_core': 4,
	'init_freq': 2,
	'programs': [
		"both",
		fmt_ext_args("co -d step_heuristics"),
		fmt_ext_args("co -d uncoordinated_heuristics"),
		"fs",
		"ca",
	],
	'repetitions': 3,
	'hr_min_max_pairs': macbook_pairs0
}
suite_compare_bothness_mb2 = {
	'name': 'bo2+',
	'thread_num': 4,
	'init_core': 4,
	'init_freq': 2,
	'programs': [
		"both",
		fmt_ext_args("co -d step_heuristics"),
		fmt_ext_args("co -d uncoordinated_heuristics"),
		"fs",
		"ca",
	],
	'repetitions': 3,
	'hr_min_max_pairs': [(2.9, 3), (3.2,3.25)]
}

#6-24
suite_foone1 = {
	'name': 'foone',
	'thread_num': 4,
	'init_core': 4,
	'init_freq': 3,
	'programs': [
		fmt_ext_args("co -d step_heuristics"),
		fmt_ext_args("co -d uncoordinated_heuristics"),
		"fs",
		"fs2",
		"ca",
		fmt_ext_args("co -d dummy_control"),
		fmt_ext_args("co -d core_heuristics"),
		fmt_ext_args("co -d freq_heuristics"),
		fmt_ext_args("co -d core_p_controller -p 0.02"),
		fmt_ext_args("co -d core_p_controller -p 0.2"),
		fmt_ext_args("co -d machine_state_p_controller -p 2"),
		fmt_ext_args("co -d machine_state_p_controller -p 5"),
		fmt_ext_args("co -d machine_state_histeresis_p_controller -p 2"),
		fmt_ext_args("co -d machine_state_histeresis_p_controller -p 5"),
		fmt_ext_args("co -d machine_state_pseudo_pi_controller -p 2 -q 0.5"),
		fmt_ext_args("co -d machine_state_pseudo_pi_controller -p 2 -q -0.5"),
		fmt_ext_args("co -d machine_state_pseudo_pi_controller -p 5 -q 1"),
		fmt_ext_args("co -d machine_state_pseudo_pi_controller -p 5 -q -1"),
	],
	'repetitions': 3,
	'hr_min_max_pairs': [(18,19), (19,20), (12,12.5), (11,13), (17,20)]
}
suite_foone2 = {
	'name': 'foone2',
	'thread_num': 4,
	'init_core': 1,
	'init_freq': 2,
	'programs': [
		fmt_ext_args("co -d step_heuristics"),
		fmt_ext_args("co -d uncoordinated_heuristics"),
		"fs",
		"fs2",
		"ca",
		fmt_ext_args("co -d dummy_control"),
		fmt_ext_args("co -d core_heuristics"),
		fmt_ext_args("co -d freq_heuristics"),
		fmt_ext_args("co -d core_p_controller -p 0.02"),
		fmt_ext_args("co -d core_p_controller -p 0.2"),
		fmt_ext_args("co -d machine_state_p_controller -p 2"),
		fmt_ext_args("co -d machine_state_p_controller -p 5"),
		fmt_ext_args("co -d machine_state_histeresis_p_controller -p 2"),
		fmt_ext_args("co -d machine_state_histeresis_p_controller -p 5"),
		fmt_ext_args("co -d machine_state_pseudo_pi_controller -p 2 -q 0.5"),
		fmt_ext_args("co -d machine_state_pseudo_pi_controller -p 2 -q -0.5"),
		fmt_ext_args("co -d machine_state_pseudo_pi_controller -p 5 -q 1"),
		fmt_ext_args("co -d machine_state_pseudo_pi_controller -p 5 -q -1"),
	],
	'repetitions': 3,
	'hr_min_max_pairs': [(18,19), (19,20), (12,12.5), (11,13), (17,20)]
}

suite_compare_bothness_dusk = {
	'name': 'bo2dusk',
	'thread_num': 4,
	'init_core': 4,
	'init_freq': 2,
	'programs': [
		"both",
		fmt_ext_args("co -d step_heuristics"),
		fmt_ext_args("co -d uncoordinated_heuristics"),
		"fs",
		"ca",
	],
	'repetitions': 5,
	'hr_min_max_pairs': [(7, 9), (4, 5), (8, 9), (8, 10), (9, 11), (10, 12), (6, 7)]
}

suites = [
	suite_compare_bothness_dusk,
#	suite_foone1,
#	suite_foone2,
#	suite_compare_bothness_mb2,
#	suite_compare_bothness_mb,
#	suite_ctl_macbook
#	suite_ctl,
#	suite1,
#	suite2
]


#hr_range_step_pairs = [ (1,1), (2,1), (3,2) ]
#for hrrange, hrstep in hr_range_step_pairs:
#	for i in xrange(int(ceil(float(hrmaxlimit - hrminlimit)/hrstep))):
#		hrmin = hrminlimit + i*hrstep
#		hrmax = hrmin + hrrange
#		hr_min_max_pairs.append((hrmin, hrmax))
#print hr_min_max_pairs
#exit(1)

for suite in suites:
	suitename = suite['name']
	thread_num = suite['thread_num']
	init_core = suite['init_core']
	init_freq = suite['init_freq']
	programs = suite['programs']
	repetitions = suite['repetitions']
	hr_min_max_pairs = suite['hr_min_max_pairs']
	for counter in xrange(1, repetitions+1):
		for hrmin, hrmax in hr_min_max_pairs:
			for progname in programs:
				cmd = "sh test4.sh -m %05.2f -M %05.2f -t %d -a 0-%d -f %d -p %s -c %s-%d" % (hrmin, hrmax, thread_num, init_core-1, init_freq, progname, suitename, counter)
				print cmd
				status = system(cmd)
				if status != 0:
					print "test execution failed! aborting..."
					exit(2)

