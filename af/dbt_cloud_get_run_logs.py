from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.hooks.base_hook import BaseHook
import requests
import os
import re
from airflow.utils.trigger_rule import TriggerRule
from airflow.models import Variable

class CustomDbtCloudGetRunLogsOperator(BaseOperator):
    template_fields = ('dbt_cloud_run_id', 'dbt_cloud_run_url', 'log_target_directory_path', 'log_file_name')

    @apply_defaults
    def __init__(
            self,
            dbt_cloud_conn_id: str,
            log_type: str,
            log_target_directory_path: str,
            log_file_name: str,
            dbt_cloud_run_id: str = None,  # Optional, defaults to None
            dbt_cloud_run_url: str = None,  # Optional, defaults to None
            trigger_rule: str = TriggerRule.ALL_SUCCESS,  # Add trigger_rule here
            *args, **kwargs
    ) -> None:
        super().__init__(trigger_rule=trigger_rule, *args, **kwargs)  # Pass trigger_rule to super()
        self.dbt_cloud_conn_id = dbt_cloud_conn_id
        self.log_type = log_type
        self.dbt_cloud_run_id = dbt_cloud_run_id
        self.dbt_cloud_run_url = dbt_cloud_run_url
        self.log_target_directory_path = log_target_directory_path+"_"+dbt_cloud_run_id
        self.log_file_name = log_file_name

        # Validate the 'log_type' parameter
        if self.log_type not in ['console_logs', 'debug_logs']:
            raise ValueError("Invalid value for log_type. It must be 'console_logs' or 'debug_logs'.")

        # Ensure either dbt_cloud_run_id or dbt_cloud_run_url is provided
        if not self.dbt_cloud_run_id and not self.dbt_cloud_run_url:
            raise ValueError("Either dbt_cloud_run_id or dbt_cloud_run_url must be provided.")

    def _parse_run_id_from_url(self, url: str) -> str:
        """Parses the dbt Cloud run ID from the given URL using a regular expression."""
        pattern = r'/runs/(\d+)/'
        match = re.search(pattern, url)
        if match:
            return match.group(1)
        else:
            raise ValueError("Run ID not found in the provided URL.")

    def execute(self, context):

        # Determine the run ID based on the inputs
        if not self.dbt_cloud_run_id:
            if not self.dbt_cloud_run_url:
                raise ValueError("Either dbt_cloud_run_id or dbt_cloud_run_url must be provided.")
            self.dbt_cloud_run_id = self._parse_run_id_from_url(self.dbt_cloud_run_url)

        # Retrieve the connection object for dbt cloud
        dbt_cloud_conn = BaseHook.get_connection(self.dbt_cloud_conn_id)

        # Get connection parameters
        #dbt_cloud_tenant = dbt_cloud_conn.host if dbt_cloud_conn.host not in (None, "") else 'cloud.getdbt.com'
        #dbt_cloud_account_id = dbt_cloud_conn.login
        #dbt_cloud_token = dbt_cloud_conn.password
        dbt_cloud_tenant = "hy210.us1.dbt.com"
        dbt_cloud_account_id = "70437463654977"
        dbt_cloud_token = Variable.get("DBT_TKN")

        # Creating the URL endpoint
        endpoint = f'https://{dbt_cloud_tenant}/api/v2/accounts/{dbt_cloud_account_id}/runs/{self.dbt_cloud_run_id}/?include_related=["run_steps","debug_logs"]'

        # Creating the headers
        headers = {'Authorization': f'Token {dbt_cloud_token}'}

        # Make the API Call to get the data
        response = requests.get(endpoint, headers=headers)

        # Check status code
        if response.status_code != 200:
            raise Exception(f"Request failed: {response.text}, API Call made to the following URI: {endpoint}")

        # Turn data into JSON
        data = response.json()

        # Extract logs
        run_steps = data.get('data', {}).get('run_steps', [])

        # define the log file name to output to
        formal_log_file_name = f"{self.dbt_cloud_run_id}_{self.log_file_name}"

        # Initialize an empty list to store logs
        logs = []

        # Determine what type of logs to return
        logs_to_fetch = 'logs' if self.log_type == 'console_logs' else 'debug_logs'

        # Loop through each run_step and extract logs
        for step in run_steps:
            step_logs = step.get(f'{logs_to_fetch}', '')
            logs.append(step_logs)

        # Concatenate all logs into a single string
        concatenated_logs = '\n'.join(logs)

        if not os.path.exists(self.log_target_directory_path):
            # Create the directory if it doesn't exist
            os.makedirs(self.log_target_directory_path)

        # Save the concatenated logs to the specified output file
        with open(self.log_target_directory_path + formal_log_file_name, 'w') as file:
            file.write(concatenated_logs)

        # Logging the completion of the task
        self.log.info(f"Logs saved to {self.log_target_directory_path + formal_log_file_name}")

        import os
        file_name_full = self.log_target_directory_path + formal_log_file_name
        if not os.path.exists(file_name_full):
            raise FileNotFoundError(
                f"Expected log file not found: {file_name_full}. "
                "This usually means the artifact wasn't written locally or task ran on a different worker."
            )
        with open(file_name_full, "r", encoding="utf-8") as f:
            print("------------------------------------------------------------")
            print(f"***** Reading local file: {file_name}")
            for i, line in enumerate(f):
                if i >= max_lines:
                    print(f"... truncated after {max_lines} lines ...")
                    break
                print(line.rstrip("\n"))
            print("------------------------------------------------------------")

        # push XCOM for log name and run id
        context["ti"].xcom_push(key="log_file_path", value=self.log_target_directory_path + formal_log_file_name)
        context["ti"].xcom_push(key="dbt_cloud_run_id", value=self.dbt_cloud_run_id)

        # Output the run ID
        return self.dbt_cloud_run_id
