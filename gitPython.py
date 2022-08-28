import git

repo_clone_url = "git@github.com:mygithubuser/myrepo.git"
local_repo = "mytestproject"
test_branch = "test-branch"
repo = git.Repo.clone_from(repo_clone_url, local_repo)
checkout = repo.git.checkout('checkout')
# Check out branch test_branch somehow
# write to file in working directory
repo.index.add(["test.txt"])
commit = repo.index.commit("Commit test")
