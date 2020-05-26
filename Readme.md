# Vim DevOps code interview

### Goal
Create a script to clean up old database snapshots.
We have couple of Databases and each one has some backups/snapshots.  
 


### What we have
- API server https://5dbf2fb9e295da001400b4cc.mockapi.io with rest API
    - list all snapshots:
    ```
    GET /api/v1/snapshots
    ```
   - get snapshot by `id`
    ```
    GET /api/v1/snapshots/:id
    ```
    - delete snapshot by `id`
    ```
    DELETE /api/v1/snapshots/:id
    ```
    <aside class="warning">
    :exclamation: after removing snapshot there is no way to bring it back
    </aside>

### Exercise
- Create a script that leaves 2 latest backups/snapshots of each DB, written on Python3
- Create Dockerfile for this script 
- Make a pull request with your answer to this repo.


## Good luck!
