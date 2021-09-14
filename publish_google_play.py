import argparse
from googleapiclient.discovery import build

'''
    Is required to insert GOOGLE_APPLICATION_CREDENTIALS into local env 
    LINUX=.bashrc
'''

def start_edit(service):
    print("Starting Edit Process..")
    result_edit = service.edits().insert(
        body={},
        packageName=args.package).execute()
    return result_edit['id']

def send_bundle_to_package_explorer(service, edit_id):
    print("Sending bundle to explorer..")
    bundle_response = service.edits().bundles().upload(
        editId = edit_id,
        packageName=args.package,
        media_body=args.bundle, 
        media_mime_type="application/octet-stream").execute()
    return bundle_response['versionCode']

def create_release(service, edit_id, version_code):
    if (not args.release): return
    print("Creating release..")
    service.edits().tracks().update(
        editId=edit_id, 
        track=args.track, 
        packageName=args.package, 
        body={u'releases': [{
            u'versionCodes': [str(version_code)],
            u'status': args.status,
            # u'status': u'draft',
            # u'status': u'completed',
        }]}).execute()

def commit_changes(service, edit_id):
    print("Commiting changes..")
    service.edits().commit(
        editId=edit_id, 
        packageName=args.package).execute()

def main():
    with build('androidpublisher', 'v3') as service:
        edit_id = start_edit(service)
        version_code = send_bundle_to_package_explorer(service, edit_id)
        create_release(service, edit_id, version_code)
        commit_changes(service, edit_id)

def arg_parser():
    parser = argparse.ArgumentParser()
    required = parser.add_argument_group('required arguments')
    required.add_argument("-p", "--package", help="Package name", required=True)
    required.add_argument("-b", "--bundle", help="Path of bundle", required=True)
    required.add_argument("-t", "--track", help="Track to publish", required=True)
    required.add_argument("-s", "--status", help="Status of project", default= "completed")
    required.add_argument("-r", "--release", help="Create Release", default= False)
    return parser.parse_args()

if __name__ == '__main__':
    args = arg_parser()
    main()