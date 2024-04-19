# You need to teach this course on an - unknown - cluster?

## Questionaire

This questionaire helps asking the right questions:

- Organization:
    - Who is the contact for organizing this course? 

- How does the course room look like?
    - How many seats and PC-screens are available?
    - Is there a "Presenter PC"?
    - Is it possible to plug in Laptop? HDMI?
    - Which kind the "projector situation" (1 or more, need to have a key)?
    - Do you need an adaptor for the projector?
    - Which is the OS for participant PCs?
    - Which is the software to log in? (putty, mobaxterm, powershell or plain ssh via Linux - or a terminal on demand)
    - Is 2FA enforced? Is so: How?
    - ssh-keys - are they to be prepared?
    - Does the site require course accounts?
    - Is it possible to do paired programming?

- Cluster Specialties
    - May the course use shared file space for the setup to be copied to? E.g. a workspace? Which are the quota limitations?
    - Which editors or IDEs are provided?
    - Which applications are available to display a simple plot (png, jpeg, svg)?
    - Will the course require and / or get a SLURM reservation?
      - if there are dedicated course accounts, the reservation should be made "magnetic" - then the `--reservation` flag is not necessary
    - How long will the course run (number of days)?
      - the "Creators" course will require a minimum of 2 days

- Misc
    - Do colleagues on site want to be trained as trainers?

