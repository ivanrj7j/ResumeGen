from github import Github
from github.Auth import Token
from ..models.project import Project

class GithubExtractor:
    def __init__(self, apiKey:str):
        """
        Initializes the githubExtractor instance with the provided GitHub API key.
        Args:
            apiKey (str): The GitHub API key used for authentication.
        Attributes:
            client (Github): An authenticated GitHub client instance.
        """

        self.client = Github(Token(apiKey))
        
    def getProjectDetail(self, projectURL:str):
        """
        Retrieves detailed information about a GitHub project using its URL.

        Args:
            projectURL (str): The full name (e.g., 'owner/repo') of the GitHub repository.

        Returns:
            Repository: An object representing the GitHub repository details.

        Raises:
            github.GithubException.UnknownObjectException: If the repository does not exist or is inaccessible.
            github.GithubException.BadCredentialsException: If authentication fails.
        """
        repository = self.client.get_repo(projectURL)
        return Project(repository.name, repository.description, [], f"https://github.com/{projectURL}")
    
    def getUserProjects(self, userName:str):
        if userName.startswith("https://github.com/"):
            userName = userName.replace("https://github.com/", "").strip()

        user = self.client.get_user(userName)
        repositories = user.get_repos()
        for repo in repositories:
            url = "/".join(repo.url.split("/")[-2:])
            yield self.getProjectDetail(url)