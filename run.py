import requests
import central_oauth
import json

# Set your credentials.
client_id = ""
client_secret = ""

# Get the stuff you need
jwt, tenant_id, tenant_type, data_region = central_oauth.Authenticate.auth(client_id, client_secret)

def makerequest():
    sql = """
    -- running_processes_windows_sophos
    SELECT
    -- Device ID DETAILS
    meta_hostname, meta_ip_address,
    -- Query Details
    query_name, cmdline, file_size, gid, global_rep,
    global_rep_data, local_rep, local_rep_data, ml_score, ml_score_data,
    name, parent, parent_name, parent_path, parent_sophos_pid,
    path, pid, pua_score, sha1, sha256,
    sophos_pid, time, uid, username,
    -- Decoration
    meta_boot_time, meta_eid, meta_endpoint_type,
    meta_ip_mask, meta_mac_address, meta_os_name, meta_os_platform, meta_os_type,
    meta_os_version, meta_public_ip, meta_query_pack_version, meta_username,
    --- Generic
    calendar_time, counter, epoch, host_identifier, numerics
    osquery_action, unix_time,
    -- Data Lake
    customer_id, endpoint_id, upload_size
    FROM xdr_data
    WHERE query_name = 'running_processes_windows_sophos'
    """

    requestdata = {
        "adHocQuery": {
            "template": sql
            }
        }

    data = json.dumps(requestdata, indent=2)
    # use the api_creds to go to the correct URL
    u = f'{data_region}/xdr-query/v1/queries/runs'
    # Set the headers.
    h = {
        'Authorization': f'Bearer {jwt}',
        'X-Tenant-ID': f'{tenant_id}'
        }
    # Run the initial request
    r = requests.post(u, headers=h, data=data)
    print(r.json())


def getjob():
    # use the api_creds to go to the correct URL
    u = f'{data_region}/xdr-query/v1/queries/runs/bdebb8cd-da41-4802-889d-64ac62f93c80'
    # Set the headers.
    h = {
        'Authorization': f'Bearer {jwt}',
        'X-Tenant-ID': f'{tenant_id}'
        }
    # Run the initial request
    r = requests.get(u, headers=h)
    print(r.json())


def getresults():
    # use the api_creds to go to the correct URL
    u = f'{data_region}/xdr-query/v1/queries/runs/bdebb8cd-da41-4802-889d-64ac62f93c80/results?maxSize=1000'
    # Set the headers.
    h = {
        'Authorization': f'Bearer {jwt}',
        'X-Tenant-ID': f'{tenant_id}'
        }
    # Run the initial request
    r = requests.get(u, headers=h)
    print(r.json())
