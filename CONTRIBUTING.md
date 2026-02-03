# How to Contribute

We'd love to accept your patches and contributions to this project. There are
just a few small guidelines you need to follow.

## Contributor License Agreement

Contributions to this project must be accompanied by a Contributor License
Agreement (CLA). You (or your employer) retain the copyright to your contribution;
this simply gives us permission to use and redistribute your contributions as
part of the project. Head over to <https://cla.developers.google.com/> to see
your current agreements on file or to sign a new one.

You generally only need to submit a CLA once, so if you've already submitted one
(even if it was for a different project), you probably don't need to do it
again.

## Code reviews

All submissions, including submissions by project members, require review. We
use GitHub pull requests for this purpose. Consult
[GitHub Help](https://help.github.com/articles/about-pull-requests/) for more
information on using pull requests.

## Community Guidelines

This project follows
[Google's Open Source Community Guidelines](https://opensource.google/conduct/).

## Pull Requests

If you are Google partner, please make sure not to add sensitive data on GitHub when performing the following actions:
* Extending the ontology types through a pull request
* Opening an issue
* Asking a question

Sensitive data is considered anything in any of the following categories:
* **Buildings:** name, location, street address, information about floors/rooms/zones within the building, etc.
* **Devices/Equipment:** name, id, location, etc.
* **Other:** project id, subscription names, etc.

### Enabling Auto-GUID Generation for PRs
1. In your individual fork, navigate to `Settings > Actions > General` and ensure your settings under each header are as follows:
    * Under “Actions Permissions,” please select “Allow all actions and reusable workflows”
    * Under “Workflow Permissions,” please select “Read and write permissions” and check the box next to “Allow GitHub Actions to create and approve pull requests”

2. Click the gray “Save” button at the bottom of the page to preserve the changes

3. Once your Settings are saved, in your individual fork, navigate to `Actions`
    * Click the green button that says “I understand my workflows, go ahead and enable them” to fully enable (if you do not see this button, it is likely the workflows are already enabled and no further action is required)

