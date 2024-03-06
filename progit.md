## Version Control
- Version control (VCS)is a system that records changes to a fIle or set of files over time so the users can recall specific version later
- to colloborate with developers and using Centralized version control systems were developed (CVCSs)
- (DVCS) Distributed version control systems is when users can fully miror the repository and its full history. Beneficial if server dies during group projects to restore files/

## Short History of Git
- Linux kernel maintenance (1991–2002), changes to the software were passed around as patches and archived files. 
- In 2002, the Linux kernel project began using a proprietary DVCS called
BitKeeper.
- In 2005, the relationship between the community that developed the Linux kernel and the commercial company that developed BitKeeper broke down.
### goals for new system
- Speed
- Simple design
- Strong support for non-linear development (thousands of parallel branches)
-  Fully distributed
- Able to handle large projects like the Linux kernel efficiently (speed and data size)
## What is Git
- When storing data is stores its like a series of snapshots of a minature filesystem. 
- When you commit or save, git stores a reference to that snapshot.

- You can use giti when your offline or off VPN
-  Git stores everything in its database not by file name but by the hash value of its contents.
## The three states
- Git has three main states that your files can reside in: modified,
staged, and committed:
16
-  Modified means that you have changed the file but have not committed it to your database yet.
- Staged means that you have marked a modified file in its current version to go into your next commit snapshot.
-  Committed means that the data is safely stored in your local database.

- The working tree is a single checkout of one version of the project. These files are pulled out of the
compressed database in the Git directory and placed on disk for you to use or modify.
- The staging area is a file, generally contained in your Git directory, that stores information about
what will go into your next commit. 
- The Git directory is where Git stores the metadata and object database for your project. This is the
most important part of Git, and it is what is copied when you clone a repository from another
computer.

- sudo apt install git-all
