# No-Escape Search (Published)
## Design and Implementation of Cloud-Based Directory Content Search Algorithm

### IEEE-Xplore
Manuscript is available   <a href="http://ieeexplore.ieee.org/document/8284288/" target="_blank">
          here </a>

### Git-Page
Published Web-Page is available <a href="https://newtein.github.io/no_escape_search/" target="_blank"> here.</a>


## •	Research
Researched on Windows' Index Search, its functions, advantages and technical drawbacks.
## •	Development

#### •	Tools/Technologies used: 
Python (PyQt, Pdfminer) and Firebase.

No-Escape Search that has solved 3 problems of the Windows Search. First,  memory wastage by Windows indexing and its limited nature;
second,  slow data retrieval by unindexed window search; and third, inability to facilitate the user with location(s) of the input.
This algorithm retrieves in O(constant) time using cloud-based 3D hash data-structure.

### Designed 3D Hash Data-Structure
<center>
  <img src="https://raw.githubusercontent.com/newtein/no_escape_search/master/UI_Images/3dhash2.JPG" width="500"/>
</center>

### Hash stored in hierarchical key-value pairs at Google Firebase cloud
![alt text](https://raw.githubusercontent.com/newtein/no_escape_search/master/UI_Images/hash_table_data.JPG)

System comprises of 3 major algorithms:  first, automated directory scanning algorithm that involves the use of a ‘wait for single object’
call from pywin32 events; second, file scanning algorithm; third, retrieval algorithm. Retrieval is a comprehensible combination of user’s
input string & filename(s). Also, unlike windows search, it permits to include location(s) & even multiple occurrences. 
Additionally, the performance of the system is increased by multi-threading.

### Target Directory and UI Search
![alt text](https://raw.githubusercontent.com/newtein/no_escape_search/master/UI_Images/1.%20Target_Dir_N_Python_App_to_Search.JPG)
### Search Results for create
![alt text](https://raw.githubusercontent.com/newtein/no_escape_search/master/UI_Images/2.%20search_dir_in_3secs_by_giving_multi_positions.JPG)
### Search Results for multiple terms
![alt text](https://raw.githubusercontent.com/newtein/no_escape_search/master/UI_Images/intersection.JPG)

### Automated Upload to Firebase - Cloud-level Indexing
![alt text](https://raw.githubusercontent.com/newtein/no_escape_search/master/UI_Images/3.%20Automated_upload_to_firebase.JPG)

### Flowchart of Automated Directory Scanning Algorithm
<center>
  <img src="https://raw.githubusercontent.com/newtein/no_escape_search/master/UI_Images/Figure-2.jpg" width="350"/>
</center>

### Flowchart of Retrieval algorithm
![alt text](https://raw.githubusercontent.com/newtein/no_escape_search/master/UI_Images/Figure-3.jpg)


## •	Publication.
Successfully published a research paper in 10th IC3-2017 jointly organized by University of Florida, USA and Jaypee Institute of Information Technology, India.     



