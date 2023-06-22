#! /usr/bin/env python

import sys,os,re,logging
import copy,json
from operator import itemgetter

mydir = os.path.abspath(os.getcwd())
mydate = os.popen('date +%F').read().strip()

test_drs=['CMIP6.CMIP.CAS.FGOALS-g3.ssp585.r1i1p1f1.Amon.pr.gn.20190818',
'CMIP6.ScenarioMIP.BCC.BCC-ESM1.ssp370.r1i1p1f1.Amon.tas.gn.20190314',
'CMIP6.ScenarioMIP AerChemMIP.BCC.BCC-ESM1.ssp370.r1i1p1f1.Amon.pr.gn.20190314',
'CMIP6.CMIP.MPI-M.MPI-ESM-1-2-HAM.ssp126.r1i1p1f1.Omon.mlotst.gn.20190627',
'CMIP6.ScenarioMIP AerChemMIP.AWI.AWI-CM-1-1-MR.ssp370.r1i1p1f1.day.tas.gn.20190529',
'CMIP6.ScenarioMIP.MPI-M.MPI-ESM1-2-HR.ssp126.r2i1p1f1.day.tas.gn.20190529',
'CMIP6.ScenarioMIP.MPI-M.MPI-ESM1-2-HR.ssp370.r2i1p1f1.day.pr.gn.20190529',
'CMIP6.PMIP.AWI.AWI-ESM-1-1-LR.piControl.r1i1p1f1.Omon.tos.gn.20200212',
'CMIP6.AerChemMIP.MPI-M.MPI-ESM1-2-HAM.ssp370-lowNTCF.r1i1p1f1.Amon.tas.gn.20190627',
'CMIP6.CDRMIP.CNRM-CERFACS.CNRM-ESM2-1.piControl.r1i1p1f2.Simon.siconc.gr.20181115',
'CMIP6.ScenarioMIP.BCC.BCC-ESM1.ssp370.r1i1p1f1.Amon.tas.gn.20190314']

# Read corrections
casestrs=[]
corrs=[]
for r in open('CMIP6correct.conf','r').readlines():
    if len(r.strip())==0 or re.search('^#',r):
        continue
    #print re.split(' ',r)
    (case,corr)=re.split(' ',r.strip())
    dumcases=re.split(';',re.sub('_',' ',case.strip()))
    casestr=dumcases[0]
    for d in dumcases[1:]:
        casestr += ' and '+d
    #print casestr, corr
    casestrs.append(casestr)
    corrs.append(corr)

# DRS_keys: CMIP6.<mip>.<inst>.<model>.<exp>.<ens>.<frequ>.<var>.<grid>
#print corrs
#sys.exit()
for t in test_drs:
    #print t
    (dum,mip,inst,model,exp,ens,frequ,var,grid,version)=re.split('\.',t)
    for c,n in zip(casestrs,corrs):
        #print t,model,c,n
        #mycase=re.sub('model',model,re.sub('inst',inst,re.sub('exp',exp,re.sub('mip',mip,c))))
        #print c
        mycorr=re.split('=',n)
        #print mycorr
        if (eval(c)):
            #print 'yes',t,c,mycorr[0],mycorr[1]
            if mycorr[0]=='mip':
                mip=re.split('\'',mycorr[1])[1]
            elif mycorr[0]=='model':
                model=re.split('\'',mycorr[1])[1]
            elif mycorr[0]=='inst':
                inst=re.split('\'',mycorr[1])[1]
            elif mycorr[0]=='exp':
                exp=re.split('\'',mycorr[1])[1]
            #eval(mycorr[0])=mycorr[1]
            #print mip,inst,exp,model
        #else:
        #    print 'no',t,c
    print t
    print '   --->  '+dum+'.'+mip+'.'+inst+'.'+model+'.'+exp+'.'+ens+'.'+frequ+'.'+var+'.'+grid+'.'+version

