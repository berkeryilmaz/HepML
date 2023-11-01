#!/usr/bin/env python
#
# Makes a wav file out of owon oscilloscope waveform save file.
# Tested with SDS6062 only.
#
# Used:
# http://bikealive.nl/owon-bin-file-format.html and
# http://bikealive.nl/tl_files/EmbeddedSystems/Test_Measurement/owon/OWON%20Oscilloscope%20PC%20Guidance%20Manual.pdf
#

import sys
from struct import pack, unpack, calcsize



_data_file = 'data/data/5.bin'
output_filename = 'test.wav'

fbytes = open(_data_file, "rb").read()

model_desc = {
'SPBW01' : 'PDS6062S, PDS6062T, PDS7102T',
'SPBW11' : 'HDS2062M',
'SPBW10' : 'HDS2062M-N',
'SPBV01' : 'PDS5022S, MSO5022',
'SPBV10' : 'HDS1022M-N',
'SPBV11' : 'HDS1022M',
'SPBV12' : 'HDS1021M',
'SPBX01' : 'MSO7102, PDS8102T',
'SPBX10' : 'HDS3102M-N',
'SPBM01' : 'MSO8202, PDS8202T',
'SPBS01' : 'SDS6062',
'SPBS02' : 'SDS7102',
'SPBS03' : 'SDS8202',
'SPBS04' : 'SDS9302'
}

# The original file from https://gist.github.com/aniline/c6a48f99c1d7710f9b95 used to
# reserve a 44-byte gap before the data; which however broke decoding of the example input
# files as well as practical application on SDS6062 output. It was therefore removed.

t_fmt = '<3s1s2si'
t_start = 0
t_next = t_start + calcsize(t_fmt)

(_magic, _mtype, _mmodelidx, _flen) = unpack(t_fmt, fbytes[t_start:t_next])
# print _magic, _mtype, _mmodelidx, _flen
print(_magic + _mtype + _mmodelidx)
header = '#Oscilloscope model      : Owon %s\n' % model_desc[_magic + _mtype + _mmodelidx]

t_fmt = '<3sii'
t_start = t_next
t_next = t_start + calcsize(t_fmt)

# Channel meta data header
(_chid, _offtonextch, _memmodel) = unpack(t_fmt, fbytes[t_start:t_next])

_has_deep1 = _offtonextch < 0

# Only for SDS series.
_has_deep = bool (_memmodel & 2)
_is_deep = bool (_memmodel & 1)

header += '#Channel Id             = %s\n' % _chid
header += '#Next channel offset    = %g\n' % abs(_offtonextch)
header += '#From beginning of file = %g\n' % (abs(_offtonextch) + 54 + 3)
header += '#Has deep/extended      = %g\n' % _has_deep1
header += '#Deep memory Present    = %g\n' % _has_deep
header += '#Deep memory Used       = %g\n' % _is_deep

# Channel acquisition spec.

chHs_base = {
    -2: 0.000001,
     -1: 0.000002,
     0: 0.000005,
     1: 0.00001,
     2: 0.000025,
     3: 0.00005,
     4: 0.0001,
     5: 0.00025,
     6: 0.0005,
     7: 0.001,
     8: 0.0025,
     9: 0.005,
     10: 0.01,
     11: 0.025,
     12: 0.05,
     13: 0.1,
     14: 0.25,
     15: 0.5,
     16: 1,
     17: 2.5,
     18: 5,
     19: 10,
     20: 25,
     21: 50,
     22: 100,
     23: 250,
     24: 500,
     25: 1000,
     26: 2500,
     27: 5000,
     28: 10000,
     29: 25000,
     30: 50000,
     31: 100000
     }

chHs = chHs_base

if (_mtype in set(['S','X','W'])):
    chHs.update({
            -1: 0.000002,
             2: 0.00002,
             5: 0.0002,
             8: 0.002,
             11: 0.02,
             14: 0.2,
             17: 2,
             20: 20,
             23: 200,
             26: 2000,
             29: 20000,
             })

if (_mtype == 'V'):
    chHs.update({
            -1: 0.0000025,
             2: 0.000025,
             5: 0.00025,
             8: 0.0025,
             11: 0.025,
             14: 0.25,
             17: 2.5,
             20: 25,
             23: 250,
             26: 2500,
             29: 25000
             })

chVv = {
    0: 0.002,
    1: 0.005,
    2: 0.01,
    3: 0.02,
    4: 0.05,
    5: 0.1,
    6: 0.2,
    7: 0.5,
    8: 1,
    9: 2,
    10: 5,
    11: 10,
    12: 20,
    13: 50,
    14: 100,
    15: 200,
    16: 500,
    17: 1000,
    18: 2000,
    19: 5000,
    20: 10000
    }


t_fmt = '<iiiiiiiifiif'
t_start = t_next
t_next = t_start + calcsize(t_fmt)

(_draw_offs, _screen_points, _sample_size,
 _slow_ltr_size, _tbaseidx, _vzero, _vbaseidx,
 _attenuation, _timegap, _active_samp_freq,
 _active_cycle, _mv_per_unit) = unpack(t_fmt, fbytes[t_start:t_next])


header += '#Draw Offset            = %g\n' % _draw_offs
header += '#Num of screen points   = %g\n' % _screen_points
header += '#Sample size            = %g\n' % _sample_size
header += '#Slow scan ltr size     = %g\n' % _slow_ltr_size
#header += '#Timebase (ms)          = %g\n' % chHs[_tbaseidx]
header += '#Zero sample offset vol = %g\n' % _vzero
#header += '#Voltage base (V)       = %g\n' % chVv[_vbaseidx]
#header += '#Attenuation            = %g\n' % pow(10, _attenuation)
header += '#Time gap (erroneous) (us)= %g\n' % _timegap
header += '#Active Sample freq (Hz)= %g\n' % _active_samp_freq
header += '#Active Cycle (us)      = %g\n' % _active_cycle
header += '#Voltage/sample level (mV)= %g\n' % _mv_per_unit
header += '#time voltage\n'

t_start = t_next
t_next = t_start + _sample_size

#
# Dump single channel, 8bit MS .wav file.
# Sample rate is 'wired' in - normally ok. Only one cannot try
# resample and play if its audio
#

# To unsigned array
#output_filename = sys.argv[2]
_data = map(lambda x: 0x80+(unpack('<b', x)[0]), fbytes[t_start:t_next])
if output_filename.endswith('.dat'):
    import numpy as np
    y = np.array(_data)
    #y = np.convolve(np.array(_data),np.array([.25, .5, .25]))  ##
    x = np.linspace(0,1,len(y))
    with open(output_filename, 'w') as output:
        output.write(header)
        np.savetxt(output, zip(x,y), fmt="%.6e")
elif output_filename.endswith('.wav'):
    print (header)

    # KLUDGE, 15 units on screen, timebase is time per unit
    # There is nothing in _active_samp_freq.
    _sample_rate = 250000

    ## Wave format
    chunk_head_fmt = '<4si'
    fmt_subchunk_fmt = '<hhiihh'
    wave_chunk = '4s'
    data_fmt = ''

    ## Defaults taken from from another wave file
    fmt_head = pack(fmt_subchunk_fmt, 0x1, 0x1, _sample_rate, _sample_rate, 0x1, 0x8)
    fmt = pack(chunk_head_fmt, 'fmt ', len(fmt_head)) + fmt_head
    data = pack(chunk_head_fmt, 'data', _sample_size) + bytearray(_data)

    wave_chunk = 'WAVE' + fmt + data
    riff_chunk = pack(chunk_head_fmt, 'RIFF', len(wave_chunk)) + wave_chunk

    f = open (output_filename, "w")
    f.write(riff_chunk)
    f.close()