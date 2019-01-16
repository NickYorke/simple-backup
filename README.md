# simple-backup
A simple backup script written in Python that only copies new or updated files. It will create and mirror subdirectory structures as well.

## Usage
- Update the config.ini file with the Source directory you want to backup and the Backup directory that will be used.
- Run backup.py.

## Example Output
```
*******************
*  CONFIGURATION  *
*******************

Source Directory: H:\simple-backup\backup-Source
Backup Directory: H:\simple-backup\backup-Target

*******************
*  BACKUP: START  *
*******************

- BI Overview.docx
- img001.JPG
- README.txt

**********************
*  BACKUP: COMPLETE  *
**********************

Run time:       0.94 seconds.
Files compared: 3
Files copied:   3
                3058828 bytes.
                
Press <ENTER> to continue
```
  
## Future Updates
- Remove files from the Backup directory that are no longer found in the Source directory to keep the two synchronized.
- Allow multiple Source directories and the ability to ignore configured subdirectories.
