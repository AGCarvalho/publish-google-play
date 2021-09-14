## <center> Script to publish project into Google Play</center>

This is a simple script to publish a bundle into google play using <i>androidpublisher v3</i>.

#### Obs:
 Is required to insert GOOGLE_APPLICATION_CREDENTIALS into local env 

### Arguments

### Package
<code>"-p", "--package"</code>

It can be found as an argument <b><i>applicationId</i></b> in the <b><i>build.gradle</i></b> file.

### Bundle
<code>"-b", "--bundle"</code>

Path of bundle to upload.

### Track
<code>"-t", "--track"</code>

Set launch tracks, examples:
 * "alpha"
 * "beta"
 * "internal"
 * "production"
    
Google Reference: https://developers.google.com/android-publisher/tracks

### Status
<code>"-s", "--status"</code> <b><i>default = "completed</i></b>
Project status, examples:
* "draft"
* "complete"

### Release
<code>"-r", "--release"</code> <b><i>default = False</i></b>

Flag to generate release
