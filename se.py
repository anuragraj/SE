#
# Copyright © 2019 Ronald C. Beavis
# Licensed under Apache License, Version 2.0, January 2004
#

import time
import sys
import datetime
from load_spectra import load_spectra
from load_kernel import read_kernel
from load_params import load_params
from perform_ids import perform_ids
from display_ids import simple_display

start = time.time()
job_stats = {}
job_stats['Date'] = str(datetime.datetime.now())
params = {'fragment mass tolerance': 400,
	'parent mass tolerance': 20,
	'p mods':{'C':[57021]},
	'v mods':{'M':[15995]}}
(params,ret) = load_params(sys.argv,params)
if not ret:
	exit()

spectra = load_spectra(params['spectra file'])
job_stats['S-dimension'] = len(spectra)

(kernel,spectrum_list,k) = read_kernel(params['kernel file'],spectra,params)
job_stats['K-dimension'] = k
job_stats['KS-intersection'] = len(kernel)

job_stats['Load time'] = time.time()-start
start = time.time()
(ids,scores) = perform_ids(spectra,kernel,spectrum_list,params)
job_stats['Search time'] = time.time()-start

simple_display(ids,scores,spectra,kernel,job_stats,params)


