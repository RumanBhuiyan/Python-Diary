import sys,os

if len(sys.argv) != 4 :
    raise Exception('command should be: python3 myprj.py <cid> <jid> <ltr_code>')

def make_prj(CID,JID,LTR_CODE,prj_file):
    with open(prj_file,'a') as file:
        file.writelines([
            f'JOBNAME="{CID.upper()}{JID.upper()}{LTR_CODE}"\n',
            'DEPROF="C:\\ISIS\\userisis\\Ppde.prf"\n',
            f'DOCDEF="C:\\ISIS\\docdef\\{CID.upper()}{JID.upper()}{LTR_CODE}.dfa"\n',
            f'LINEDATA="C:\\ISIS\\data\\{CID.upper()}{JID.upper()}{LTR_CODE}.DAT"\n',
            f'OUTPUT="C:\\ISIS\\afpds\\{CID.upper()}{JID.upper()}{LTR_CODE}.afp"\n',
            'HSTSAVE=""\n',
            'STICKERFILENAME="C:\\ISIS\\afpds\\"\n',
            f'$PREFIX="{CID}{JID}{LTR_CODE}"\n',
            '$PROCDATE="07192021"\n',
            '$JOB_SEL="s"\n'
        ])

if __name__ == '__main__':
    CID = sys.argv[1]
    JID = sys.argv[2]
    LTR_CODE = sys.argv[3]
    prj_file = f'{CID.upper()}{JID.upper()}{LTR_CODE}.prj'

    if os.path.exists(prj_file):
        raise Exception(f'{prj_file} file already exists')
    else :
        make_prj(CID,JID,LTR_CODE,prj_file)

  

# How to use it : 
# As I added the path 'C:\Users\DSI\PythonScripts' in environment variables so
# now if i start typing myprj and hit tab then computer will autocomplete the python
# file name searching this file from those paths that i added in path variables.

# step - 01 : Navigate into the directory where you wanna create the prj file
# step - 02 : run the command, python3 myprj.py <CID> <JID> <LTR_CODE> 
#                example : python3 myprj.py mfcu dl 110
# stpe - 03 : MFCUDL110.prj file will be created into that directory.