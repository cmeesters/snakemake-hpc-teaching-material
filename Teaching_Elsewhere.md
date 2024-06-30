# You need to teach this course on an - unknown - cluster?

## Questionaire

This questionaire helps asking the right questions:

- Organization:
    - Who is the contact for organizing this course? 
    - If this is a topical course (e.g. for Bioinformaticicians, Physicist, etc.): Does the organization employ a support scientist for the intended topic? If so, which are the contact details?

- How does the course room look like?
    - How many seats and PC-screens are available?
    - Is there a "Presenter PC"?
    - Is it possible to plug in laptop? HDMI?
    - Which kind the "projector situation" (1 or more?, need to have a key)?
    - Do you need an adaptor for the projector?
    - Which is the OS for participant PCs?
    - Which is the software to log in? (putty, mobaxterm, powershell or plain ssh via Linux - or a terminal on demand)
    - Is 2FA enforced? If so: How?
    - ssh-keys - are they to be prepared?
    - Does the site use course accounts?
    - Will the site prepare login information to be shared with the lecturer? (e.g. featuring login information on login sheets, login slides, etc.)
    - May or should participants bring their own device? If so:
        - Will there be information about it? 
        - Will there be wifi? 
        - Will there be power outlets?
    - Is it possible to do paired programming?

- Cluster Specialties
    - May the course use shared file space for the setup to be copied to? E.g. a workspace? Which are the quota limitations?
    - Are there quotas for the HOME directory (size, file number)?
    - Which compute node scratch mount points are provided (for stage-in/out)?
    - Which editors or IDEs are provided?
    - Which applications are available to display a simple plot (png, jpeg, svg)?
    - Will the course require and / or get a SLURM reservation?
      - if there are dedicated course accounts, the reservation should be made "magnetic" - then the `--reservation` flag is not necessary
    - Which partitions does the cluster provide for SMP programs (any restrictions for such software)?
    - Which partitions does the cluster provide for software (e.g. MPI) using >=1 full nodes?
    - How does the cluster support GPU application resource requests (special partitions? special SLURM flags?)?
    - How long will the course run (number of days)?
      - the "Creators" course will require a minimum of 2 days

- Misc
    - Do colleagues on site want to be trained as trainers?

