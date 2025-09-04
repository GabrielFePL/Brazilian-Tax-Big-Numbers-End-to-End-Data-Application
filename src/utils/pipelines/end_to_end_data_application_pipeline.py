%pip install --upgrade databricks-sdk==0.49.0
%restart_python

from databricks.sdk.service.jobs import JobSettings as Job
from databricks.sdk import WorkspaceClient

data_sources_job_id = 195760046131130
bronze_layer_job_id = 579424215489695
silver_layer_job_id = 758015953526002
gold_layer_job_id = 321296144214882

Brazilian_Tax_Big_Numbers_End_To_End_Data_Pipeline = Job.from_dict(
    {
        "name": "Brazilian Tax Big Numbers End To End Data Pipeline",
        "tasks": [
            {
                "task_key": "Data_Sources_Ingestion",
                "run_job_task": {
                    "job_id": data_sources_job_id,
                },
            },
            {
                "task_key": "Bronze_Layer_Ingestion",
                "depends_on": [
                    {
                        "task_key": "Data_Sources_Ingestion",
                    },
                ],
                "run_job_task": {
                    "job_id": bronze_layer_job_id,
                },
            },
            {
                "task_key": "Silver_Layer_Transformation",
                "depends_on": [
                    {
                        "task_key": "Bronze_Layer_Ingestion",
                    },
                ],
                "run_job_task": {
                    "job_id": silver_layer_job_id,
                },
            },
            {
                "task_key": "Gold_Layer_Data_Modeling",
                "depends_on": [
                    {
                        "task_key": "Silver_Layer_Transformation",
                    },
                ],
                "run_job_task": {
                    "job_id": gold_layer_job_id,
                },
            },
        ],
        "tags": {
            "Brazilian_Tax_Big_Numbers": "",
            "End_To_End_Data_Pipeline": "",
        },
        "queue": {
            "enabled": True,
        },
    }
)


w = WorkspaceClient()
j = w.jobs.create(**Brazilian_Tax_Big_Numbers_End_To_End_Data_Pipeline.as_shallow_dict())

print(f"View the job at {w.config.host}/#job/{j.job_id}\n")
