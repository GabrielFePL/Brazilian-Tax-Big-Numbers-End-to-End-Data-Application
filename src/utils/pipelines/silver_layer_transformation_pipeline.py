%pip install --upgrade databricks-sdk==0.49.0
%restart_python

from databricks.sdk.service.jobs import JobSettings as Job
from databricks.sdk import WorkspaceClient

workspace_path = "/Workspace/Users/gabriel.larocca@programmers.com.br/Brazilian-Tax-Big-Numbers-End-to-End-Data-Application/src/notebooks/silver_transformations"
cluster_id = "0712-134023-cru7s9r5"

Brazilian_Tax_Big_Numbers_Silver_Transformations = Job.from_dict(
    {
        "name": "Brazilian Tax Big Numbers Silver Transformations",
        "tasks": [
            {
                "task_key": "Assets_Debts_Donations_Transformation_And_Aggregation",
                "notebook_task": {
                    "notebook_path": f"{workspace_path}/transformation_and_aggregation_assets_debts_donations",
                    "source": "WORKSPACE",
                },
            },
            {
                "task_key": "Earnings_Transformation_And_Aggregation",
                "depends_on": [
                    {
                        "task_key": "Assets_Debts_Donations_Transformation_And_Aggregation",
                    },
                ],
                "notebook_task": {
                    "notebook_path": f"{workspace_path}/transformation_and_aggregation_earnings",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": cluster_id,
            },
            {
                "task_key": "State_And_Capital_Transformation_And_Aggregation",
                "depends_on": [
                    {
                        "task_key": "Earnings_Transformation_And_Aggregation",
                    },
                ],
                "notebook_task": {
                    "notebook_path": f"{workspace_path}/transformation_and_aggregation_state_and_capital_of_declarants_residence",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": cluster_id,
            },
            {
                "task_key": "Annual_Calculation_Base_Range_Transformation",
                "depends_on": [
                    {
                        "task_key": "State_And_Capital_Transformation_And_Aggregation",
                    },
                ],
                "notebook_task": {
                    "notebook_path": f"{workspace_path}/transformation_annual_calculation_base_range",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": cluster_id,
            },
            {
                "task_key": "Donation_Range_And_Inheritance_Transformation",
                "depends_on": [
                    {
                        "task_key": "Annual_Calculation_Base_Range_Transformation",
                    },
                ],
                "notebook_task": {
                    "notebook_path": f"{workspace_path}/transformation_donation_range_and_inheritance",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": cluster_id,
            },
            {
                "task_key": "Fiscal_Status_Transformation",
                "depends_on": [
                    {
                        "task_key": "Donation_Range_And_Inheritance_Transformation",
                    },
                ],
                "notebook_task": {
                    "notebook_path": f"{workspace_path}/transformation_fiscal_status",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": cluster_id,
            },
            {
                "task_key": "Form_Type_Transformation",
                "depends_on": [
                    {
                        "task_key": "Fiscal_Status_Transformation",
                    },
                ],
                "notebook_task": {
                    "notebook_path": f"{workspace_path}/transformation_form_type",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": cluster_id,
            },
            {
                "task_key": "Gender_And_Age_Range_Transformation",
                "depends_on": [
                    {
                        "task_key": "Form_Type_Transformation",
                    },
                ],
                "notebook_task": {
                    "notebook_path": f"{workspace_path}/transformation_gender_and_age_range",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": cluster_id,
            },
            {
                "task_key": "Gender_And_Salary_Range_Transformation",
                "depends_on": [
                    {
                        "task_key": "Gender_And_Age_Range_Transformation",
                    },
                ],
                "notebook_task": {
                    "notebook_path": f"{workspace_path}/transformation_gender_and_salary_range",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": cluster_id,
            },
            {
                "task_key": "Gender_And_Statement_Type_Transformation",
                "depends_on": [
                    {
                        "task_key": "Gender_And_Salary_Range_Transformation",
                    },
                ],
                "notebook_task": {
                    "notebook_path": f"{workspace_path}/transformation_gender_and_statement_type",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": cluster_id,
            },
            {
                "task_key": "Main_Occupation_Transformation",
                "depends_on": [
                    {
                        "task_key": "Gender_And_Statement_Type_Transformation",
                    },
                ],
                "notebook_task": {
                    "notebook_path": f"{workspace_path}/transformation_main_occupation",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": cluster_id,
            },
            {
                "task_key": "Municipality_And_Form_Type_Transformation",
                "depends_on": [
                    {
                        "task_key": "Main_Occupation_Transformation",
                    },
                ],
                "notebook_task": {
                    "notebook_path": f"{workspace_path}/transformation_municipality_and_form_type",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": cluster_id,
            },
            {
                "task_key": "Nature_Of_Occupation_Transformation",
                "depends_on": [
                    {
                        "task_key": "Municipality_And_Form_Type_Transformation",
                    },
                ],
                "notebook_task": {
                    "notebook_path": f"{workspace_path}/transformation_nature_of_occupation",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": cluster_id,
            },
            {
                "task_key": "Recipients_Of_Profits_And_Dividends_Income_Transformation",
                "depends_on": [
                    {
                        "task_key": "Nature_Of_Occupation_Transformation",
                    },
                ],
                "notebook_task": {
                    "notebook_path": f"{workspace_path}/transformation_recipients_of_profits_and_dividends_income_from_partners_and_sole_proprietors_of_microenterprises_by_main_occupation",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": cluster_id,
            },
        ],
        "tags": {
            "Brazilian_Tax_Big_Numbers": "",
            "Silver_Layer_Transformation": "",
        },
        "queue": {
            "enabled": True,
        },
        "performance_target": "STANDARD",
    }
)

w = WorkspaceClient()
j = w.jobs.create(**Brazilian_Tax_Big_Numbers_Silver_Transformations.as_shallow_dict())

print(f"View the job at {w.config.host}/#job/{j.job_id}\n")
