import dagshub
import mlflow
from chestcancer.constants import *

def init_dagshub(repo_owner: str, repo_name: str):
    """
    Initialize DAGsHub for MLflow tracking.

    Args:
        repo_owner (str): Owner of the DAGsHub repository.
        repo_name (str): Name of the DAGsHub repository.
    """
    dagshub.init(repo_owner=repo_owner, repo_name=repo_name, mlflow=True)
    mlflow.set_tracking_uri(f"https://dagshub.com/{REPO_OWNER}/{REPO_NAME}.mlflow")
    