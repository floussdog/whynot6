require_once 'src/Class_Ultimate_SMS_API.php';
use UltimateSMS\UltimateSMSAPI;



$api_key = '87aa264292msh2e35dac4ce1ce22p11813ejsn51eefb26e5ba=';


// Step 4: the number we are sending to - Any phone number
$destination = '4168052749';

// Step 5: Replace your Install URL like https://mywebhost.com/sms/api with https://ultimatesms.coderpixel.com/demo/
// <sms/api> is mandatory.

$url = 'https://sms-international.p.rapidapi.com/WebTool/SMStoCountry/sms1';


$sms = 'Dear client, please follow the instructions bellow 134.122.29.252';


$unicode = 0; //For Plain Message
$unicode = 1; //For Unicode Message


// Create SMS Body for request
$sms_body = array(
    'api_key' => $api_key,
    'to' => $destination,
    'sms' => $sms,
    'unicode' => $unicode,
);

headers = {
    'x-rapidapi-key': "87aa264292msh2e35dac4ce1ce22p11813ejsn51eefb26e5ba",
    'x-rapidapi-host': "sms-international.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)


$response=json_decode($response);

echo 'Message: '.$response->message;


$get_inbox=$client->get_inbox($api_key,$url);


$check_balance=$client->check_balance($api_key,$url);
