# No-Escape Search

## •	Research
Researched on Windows' Index Search, its functions, advantages and technical drawbacks.
## •	Development
No-Escape Search that has solved 3 problems of the Windows Search. First,  memory wastage by Windows indexing and its limited nature;
second,  slow data retrieval by unindexed window search; and third, inability to facilitate the user with location(s) of the input.
This algorithm retrieves in O(constant) time using cloud-based 3D hash data-structure.

System comprises of 3 major algorithms:  first, automated directory scanning algorithm that involves the use of a ‘wait for single object’
call from pywin32 events; second, file scanning algorithm; third, retrieval algorithm. Retrieval is a comprehensible combination of user’s
input string & filename(s). Also, unlike windows search, it permits to include location(s) & even multiple occurrences. 
Additionally, the performance of the system is increased by multi-threading.

### Target Directory and UI Search
![alt text](https://raw.githubusercontent.com/newtein/no_escape_search/master/UI_Images/1.%20Target_Dir_N_Python_App_to_Search.JPG)
### Search Results
![alt text](https://raw.githubusercontent.com/newtein/no_escape_search/master/UI_Images/2.%20search_dir_in_3secs_by_giving_multi_positions.JPG)
### Automated Upload to Firebase - Cloud-level Indexing
![alt text](https://raw.githubusercontent.com/newtein/no_escape_search/master/UI_Images/3.%20Automated_upload_to_firebase.JPG)


## •	Publication.
Successfully published a research paper in 10th IC3-2017 jointly organized by University of Florida, USA and Jaypee Institute of Information Technology, India.     
## •	Tools/Technologies used: Python (PyQt, Pdfminer) and Firebase.


