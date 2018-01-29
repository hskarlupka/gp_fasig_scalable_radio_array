#!/usr/bin/env python
energies = ['5e6', '1e7', '2e7', '5e7']
amplification = '1e4'
detector = "51"
number = "100"
threshold = "1"

with open('fasig_scalable_radio_array.dag', 'w') as f:
    f.write('RETRY ALL_NODES 1000\n')
    f.write('SCRIPT POST ALL_NODES post_script.py /data/user/hskarlupka/gp_fasig_scalable_radio_array $JOB\n')
    f.write('VARS ALL_NODES amplification="{}"\n'.format(amplification))
    f.write('VARS ALL_NODES detector="{}"\n'.format(detector))
    f.write('VARS ALL_NODES number="{}"\n'.format(number))
    f.write('VARS ALL_NODES threshold="{}"\n'.format(threshold))
    for energy in energies:
        for i in xrange(0, 1000):
            f.write('JOB {}_{} fasig_scalable_radio_array.submit\n'.format(energy, i))
            f.write('VARS {}_{} energy="{}"\n'.format(energy, i, energy))
            f.write('VARS {}_{} num="{}"\n'.format(energy, i, i))
