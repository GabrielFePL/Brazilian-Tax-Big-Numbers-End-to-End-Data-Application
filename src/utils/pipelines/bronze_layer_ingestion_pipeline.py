%pip install --upgrade databricks-sdk==0.49.0
%restart_python

from databricks.sdk.service.jobs import JobSettings as Job
from databricks.sdk import WorkspaceClient

notebook_path = "/Workspace/Users/gabriel.larocca@programmers.com.br/Brazilian-Tax-Big-Numbers-End-to-End-Data-Application/src/notebooks/bronze_ingestion/iterative_executor"
cluster_id = "0712-134023-cru7s9r5"

Brazilian_Tax_Big_Numbers_Bronze_Layer_Ingestion = Job.from_dict(
    {
        "name": "Brazilian Tax Big Numbers Bronze Layer Ingestion",
        "tasks": [
            {
                "task_key": "Dynamic_Bronze_Layer_Ingestion",
                "notebook_task": {
                    "notebook_path": notebook_path,
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": cluster_id,
            },
        ],
        "tags": {
            "Brazilian_Tax_Big_Numbers": "",
            "Bronze_Layer_Ingestion": "",
        },
        "queue": {
            "enabled": True,
        },
    }
)

w = WorkspaceClient()
j = w.jobs.create(**Brazilian_Tax_Big_Numbers_Bronze_Layer_Ingestion.as_shallow_dict())

print(f"View the job at {w.config.host}/#job/{j.job_id}\n")
