"""3.	Побудувати умовний частотний розподіл для корпусу імен.
 Знайти які перші літери частіше використовуються
 в чоловічих та жіночих іменах."""
from nltk import *
names = corpus.names
freq_analysis = ConditionalFreqDist(
    (fileid, name[0])
    for fileid in names.fileids()
    for name in names.words(fileid))
freq_analysis.plot()
