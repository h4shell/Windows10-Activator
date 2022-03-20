#Python 3

import os


def crack():
    print ("Installazione PRODUCT KEY: W269N-WFGWX-YVC9B-4J6C9-T83GX")
    os.system("slmgr.vbs /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
    print ("Registrazione ai servizi Microsoft")
    os.system("slmgr.vbs /skms kms.lotro.cc")
    print ("Riavvio servizio di verifica")
    os.system("slmgr.vbs /ato")
    print("Attivazione avvenuta con successo")
crack()

#Tutti i diritti riservati a h4shell
