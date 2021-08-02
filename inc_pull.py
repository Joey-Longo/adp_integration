from snow_post import send_to_snow, export_tickets


post_url = 'https://onepointnonprod.service-now.com/api/now/table/u_adp_import_table'

# New tickets from ADP
tickets = export_tickets()

# Iterate through generator and send to ServiceNow
# Below is test parsing from json and is unfinished
for t in tickets:
    if t['u_status'] == 'Closed':
        t.update({'u_close_code': 'Closed/Resolved by Caller', 'u_close_notes': 'Closed in ADP'})
    if t['u_clientid'] == 'ukcust000':
        t.update({'u_clientid': 'Acacia Research Corp'})
    else:
        t.update({'u_clientid': 'Boyd'})
    print(f'this would send: {t}')
#       send_to_snow('post', post_url, t)
